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
from types import ModuleType, FunctionType
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

from .route import ClassRoute, ensure_route_params, HTTP_METHODS

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
        _route_modules = self._get_route_modules(_tree_container)
        self.register_routes(_route_modules)

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

    def _get_route_modules__partial(
        self, tree_container: TreeContainer, parent_dir: Path, self_uri: str
    ) -> dict[str, ModuleType]:
        routes: dict[str, ModuleType] = {}

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

            routes[self_uri] = module

        for subdir in tree_container["subdir"]:
            out = self._get_route_modules__partial(
                subdir,
                parent_dir.joinpath(subdir["dir"]),
                self_uri + str(subdir["dir"]) + "/",
            )
            routes = {**routes.copy(), **out}

        return routes

    def _get_route_modules(
        self, tree_container: TreeContainer
    ) -> dict[str, ModuleType]:
        return self._get_route_modules__partial(tree_container, self.parent_dir, "/")

    def register_routes(self, routes: dict[str, ModuleType]):
        # [(route_uri, HTTP_METHOD, func)]
        funcs: list[tuple[str, str, FunctionType]] = []

        for route_uri, module in routes.items():

            # Try searching for 'Route' class
            route_class = getattr(module, "Route", None)
            if route_class and inspect.isclass(route_class):

                if issubclass(route_class, ClassRoute):
                    class_funcs = route_class().get_funcs()
                    funcs.extend([(route_uri, _m, _f) for _m, _f in class_funcs])
                else:
                    raise Exception("'Route' class must be an subclass of 'ClassRoute'")

            #  Route class not found, try searching for functions instead
            else:
                for method in HTTP_METHODS:
                    _func: FunctionType | None = getattr(module, method.lower(), None)
                    if _func:
                        funcs.append((route_uri, method, _func))

        for route_uri, method, func in funcs:
            params = ensure_route_params(func)
            params["methods"] = [method]

            self.add_api_route(route_uri, func, **params)
            print(
                f"[DirRouter] Registered Route '{method}' {route_uri} -> {func} {params['status_code']}"
            )
