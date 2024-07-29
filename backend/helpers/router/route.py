from __future__ import annotations
from typing import (
    Any,
    Callable,
    List,
    Dict,
    Optional,
    Sequence,
    Type,
    Union,
    TYPE_CHECKING,
)

from starlette.responses import JSONResponse
from fastapi.routing import APIRoute
from fastapi.datastructures import Default
from fastapi.utils import generate_unique_id

if TYPE_CHECKING:
    from enum import Enum

    from fastapi import params
    from starlette.routing import BaseRoute
    from starlette.responses import Response
    from fastapi import APIRouter
    from fastapi.types import DecoratedCallable, IncEx


def route_params(
    *,
    response_model: Any = Default(None),
    status_code: Optional[int] = None,
    tags: Optional[List[Union[str, Enum]]] = None,
    dependencies: Optional[Sequence[params.Depends]] = None,
    summary: Optional[str] = None,
    description: Optional[str] = None,
    response_description: str = "Successful Response",
    responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
    deprecated: Optional[bool] = None,
    operation_id: Optional[str] = None,
    response_model_include: Optional[IncEx] = None,
    response_model_exclude: Optional[IncEx] = None,
    response_model_by_alias: bool = True,
    response_model_exclude_unset: bool = False,
    response_model_exclude_defaults: bool = False,
    response_model_exclude_none: bool = False,
    include_in_schema: bool = True,
    response_class: Type[Response] = Default(JSONResponse),
    name: Optional[str] = None,
    callbacks: Optional[List[BaseRoute]] = None,
    openapi_extra: Optional[Dict[str, Any]] = None,
    generate_unique_id_function: Callable[[APIRoute], str] = Default(
        generate_unique_id
    ),
) -> Callable[[DecoratedCallable], DecoratedCallable]:
    def decorator(func: DecoratedCallable) -> DecoratedCallable:
        kwargs = {
            "response_model": response_model,
            "status_code": status_code,
            "tags": tags,
            "dependencies": dependencies,
            "summary": summary,
            "description": description,
            "response_description": response_description,
            "responses": responses,
            "deprecated": deprecated,
            "operation_id": operation_id,
            "response_model_include": response_model_include,
            "response_model_exclude": response_model_exclude,
            "response_model_by_alias": response_model_by_alias,
            "response_model_exclude_unset": response_model_exclude_unset,
            "response_model_exclude_defaults": response_model_exclude_defaults,
            "response_model_exclude_none": response_model_exclude_none,
            "include_in_schema": include_in_schema,
            "response_class": response_class,
            "name": name,
            "callbacks": callbacks,
            "openapi_extra": openapi_extra,
            "generate_unique_id_function": generate_unique_id_function,
        }
        setattr(func, "__classroute_param_meta__", kwargs)
        return func

    return decorator


class ClassRoute:
    __DEFAULT_PARAM_META__ = {
        "response_model": Default(None),
        "status_code": None,
        "tags": None,
        "dependencies": None,
        "summary": None,
        "description": None,
        "response_description": "Successful Response",
        "responses": None,
        "deprecated": None,
        "operation_id": None,
        "response_model_include": None,
        "response_model_exclude": None,
        "response_model_by_alias": True,
        "response_model_exclude_unset": False,
        "response_model_exclude_defaults": False,
        "response_model_exclude_none": False,
        "include_in_schema": True,
        "response_class": Default(JSONResponse),
        "name": None,
        "callbacks": None,
        "openapi_extra": None,
        "generate_unique_id_function": Default(generate_unique_id),
    }

    @staticmethod
    def route_params(
        *,
        response_model: Any = Default(None),
        status_code: Optional[int] = None,
        tags: Optional[List[Union[str, Enum]]] = None,
        dependencies: Optional[Sequence[params.Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[IncEx] = None,
        response_model_exclude: Optional[IncEx] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: Type[Response] = Default(JSONResponse),
        name: Optional[str] = None,
        callbacks: Optional[List[BaseRoute]] = None,
        openapi_extra: Optional[Dict[str, Any]] = None,
        generate_unique_id_function: Callable[[APIRoute], str] = Default(
            generate_unique_id
        ),
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        return route_params(
            response_model=response_model,
            status_code=status_code,
            tags=tags,
            dependencies=dependencies,
            summary=summary,
            description=description,
            response_description=response_description,
            responses=responses,
            deprecated=deprecated,
            operation_id=operation_id,
            response_model_include=response_model_include,
            response_model_exclude=response_model_exclude,
            response_model_by_alias=response_model_by_alias,
            response_model_exclude_unset=response_model_exclude_unset,
            response_model_exclude_defaults=response_model_exclude_defaults,
            response_model_exclude_none=response_model_exclude_none,
            include_in_schema=include_in_schema,
            response_class=response_class,
            name=name,
            callbacks=callbacks,
            openapi_extra=openapi_extra,
            generate_unique_id_function=generate_unique_id_function,
        )

    async def get(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError()

    async def put(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError()

    async def post(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError()

    async def delete(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError()

    async def options(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError()

    async def head(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError()

    async def patch(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError()

    async def trace(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError()

    def register_routes(self, router: APIRouter, *, route_uri: str):
        HTTP_METHODS: list[str] = [
            "GET",
            "POST",
            "PUT",
            "PATCH",
            "DELETE",
            "OPTIONS",
            "HEAD",
            "TRACE",
        ]

        for method in HTTP_METHODS:
            method = method.lower()
            _func = getattr(type(self), method, None)

            if _func and _func is not getattr(ClassRoute, method):
                _selfed_func = getattr(self, method)
                _param_meta: dict[str, Any] | None = getattr(
                    _selfed_func, "__classroute_param_meta__", None
                )

                if not _param_meta:
                    _param_meta = self.__DEFAULT_PARAM_META__

                _param_meta["methods"] = [method.upper()]

                router.add_api_route(route_uri, _selfed_func, **_param_meta)
