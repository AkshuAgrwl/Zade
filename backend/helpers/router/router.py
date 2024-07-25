from __future__ import annotations
from typing import (
    Any,
    Callable,
    Dict,
    List,
    Optional,
    Sequence,
    Type,
    Union,
    TYPE_CHECKING,
)
from .types import TreeContainer

import os
import sys
import inspect
import importlib.util
from pathlib import Path

from fastapi.responses import JSONResponse
from fastapi.datastructures import Default
from fastapi.utils import generate_unique_id
from fastapi.routing import APIRoute, APIRouter

from .route import ClassRoute

if TYPE_CHECKING:
    from enum import Enum

    from starlette.routing import BaseRoute
    from starlette.responses import Response
    from starlette.types import ASGIApp, Lifespan
    from fastapi import params


class DirRouter(APIRouter):
    def __init__(
        self,
        parent_dir: Path,
        *,
        prefix: str = "",
        tags: Optional[List[Union[str, Enum]]] = None,
        dependencies: Optional[Sequence[params.Depends]] = None,
        default_response_class: Type[Response] = Default(JSONResponse),
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        callbacks: Optional[List[BaseRoute]] = None,
        routes: Optional[List[BaseRoute]] = None,
        redirect_slashes: bool = True,
        default: Optional[ASGIApp] = None,
        dependency_overrides_provider: Optional[Any] = None,
        route_class: Type[APIRoute] = APIRoute,
        on_startup: Optional[Sequence[Callable[[], Any]]] = None,
        on_shutdown: Optional[Sequence[Callable[[], Any]]] = None,
        lifespan: Optional[Lifespan[Any]] = None,
        deprecated: Optional[bool] = None,
        include_in_schema: bool = True,
        generate_unique_id_function: Callable[[APIRoute], str] = Default(
            generate_unique_id
        ),
    ) -> None:
        super().__init__(
            prefix=prefix,
            tags=tags,
            dependencies=dependencies,
            default_response_class=default_response_class,
            responses=responses,
            callbacks=callbacks,
            routes=routes,
            redirect_slashes=redirect_slashes,
            default=default,
            dependency_overrides_provider=dependency_overrides_provider,
            route_class=route_class,
            on_startup=on_startup,
            on_shutdown=on_shutdown,
            lifespan=lifespan,
            deprecated=deprecated,
            include_in_schema=include_in_schema,
            generate_unique_id_function=generate_unique_id_function,
        )

        self.parent_dir = parent_dir
        _tree_container = self._generate_tree(parent_dir)
        _gen_routes = self._generate_routes(_tree_container)
        self._register_routes(_gen_routes)

    def _generate_tree(self, directory: Path) -> TreeContainer:
        container: TreeContainer = {
            "dir": directory.relative_to(directory.parent),
            "files": [],
            "subdir": [],
        }

        for item in directory.iterdir():
            if item.is_file():
                container["files"].append(item.relative_to(directory))
            elif item.is_dir():
                container["subdir"].append(self._generate_tree(item))

        return container

    def _generate_routes__partial(
        self, tree_container: TreeContainer, parent_dir: Path, self_uri: str
    ) -> dict[str, Type[ClassRoute]]:
        routes: dict[str, Type[ClassRoute]] = {}

        if "route.py" in [str(x) for x in tree_container["files"]]:
            module_name = (
                parent_dir.joinpath("route")
                .relative_to(os.getcwd())
                .as_posix()
                .replace("/", ".")
            )
            file_path = parent_dir.joinpath("route.py")

            spec = importlib.util.spec_from_file_location(module_name, file_path)
            if not spec:
                raise Exception("Some error occured while trying to import routes")
            module = importlib.util.module_from_spec(spec)
            sys.modules[module_name] = module
            if not spec.loader:
                raise Exception("Some error occured while trying to load routes")
            spec.loader.exec_module(module)

            route_class = getattr(module, "Route", None)
            if not inspect.isclass(route_class):
                raise Exception(f"Cannot find 'Route' class in {module_name}")
            if not issubclass(route_class, ClassRoute):
                raise Exception(
                    f"'Route' class in {module_name} must be a subclass of 'ClassRoute'"
                )

            routes[self_uri] = route_class

        for subdir in tree_container["subdir"]:
            out = self._generate_routes__partial(
                subdir,
                parent_dir.joinpath(subdir["dir"]),
                self_uri + str(subdir["dir"]) + "/",
            )
            routes = {**routes.copy(), **out}

        return routes

    def _generate_routes(
        self, tree_container: TreeContainer
    ) -> dict[str, Type[ClassRoute]]:
        return self._generate_routes__partial(tree_container, self.parent_dir, "/")

    def _register_routes(self, routes: dict[str, Type[ClassRoute]]):
        for route_uri, class_route_instance in routes.items():
            class_route_instance().register_routes(self, route_uri=route_uri)
