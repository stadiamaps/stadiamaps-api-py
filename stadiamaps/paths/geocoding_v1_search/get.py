# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from stadiamaps import api_client, exceptions
from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from stadiamaps import schemas  # noqa: F401

from stadiamaps.model.pelias_response import PeliasResponse
from stadiamaps.model.pelias_layer import PeliasLayer
from stadiamaps.model.pelias_source import PeliasSource

from . import path

# Query params
TextSchema = schemas.StrSchema
FocusPointLatSchema = schemas.Float64Schema
FocusPointLonSchema = schemas.Float64Schema
BoundaryRectMinLatSchema = schemas.Float64Schema
BoundaryRectMaxLatSchema = schemas.Float64Schema
BoundaryRectMinLonSchema = schemas.Float64Schema
BoundaryRectMaxLonSchema = schemas.Float64Schema
BoundaryCircleLatSchema = schemas.Float64Schema
BoundaryCircleLonSchema = schemas.Float64Schema
BoundaryCircleRadiusSchema = schemas.Float64Schema


class BoundaryCountrySchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'BoundaryCountrySchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
BoundaryGidSchema = schemas.StrSchema


class LayersSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['PeliasLayer']:
            return PeliasLayer

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['PeliasLayer'], typing.List['PeliasLayer']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'LayersSchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'PeliasLayer':
        return super().__getitem__(i)


class SourcesSchema(
    schemas.ListSchema
):


    class MetaOapg:
        
        @staticmethod
        def items() -> typing.Type['PeliasSource']:
            return PeliasSource

    def __new__(
        cls,
        _arg: typing.Union[typing.Tuple['PeliasSource'], typing.List['PeliasSource']],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'SourcesSchema':
        return super().__new__(
            cls,
            _arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> 'PeliasSource':
        return super().__getitem__(i)
SizeSchema = schemas.IntSchema
LangSchema = schemas.StrSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
        'text': typing.Union[TextSchema, str, ],
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'focus.point.lat': typing.Union[FocusPointLatSchema, decimal.Decimal, int, float, ],
        'focus.point.lon': typing.Union[FocusPointLonSchema, decimal.Decimal, int, float, ],
        'boundary.rect.min_lat': typing.Union[BoundaryRectMinLatSchema, decimal.Decimal, int, float, ],
        'boundary.rect.max_lat': typing.Union[BoundaryRectMaxLatSchema, decimal.Decimal, int, float, ],
        'boundary.rect.min_lon': typing.Union[BoundaryRectMinLonSchema, decimal.Decimal, int, float, ],
        'boundary.rect.max_lon': typing.Union[BoundaryRectMaxLonSchema, decimal.Decimal, int, float, ],
        'boundary.circle.lat': typing.Union[BoundaryCircleLatSchema, decimal.Decimal, int, float, ],
        'boundary.circle.lon': typing.Union[BoundaryCircleLonSchema, decimal.Decimal, int, float, ],
        'boundary.circle.radius': typing.Union[BoundaryCircleRadiusSchema, decimal.Decimal, int, float, ],
        'boundary.country': typing.Union[BoundaryCountrySchema, list, tuple, ],
        'boundary.gid': typing.Union[BoundaryGidSchema, str, ],
        'layers': typing.Union[LayersSchema, list, tuple, ],
        'sources': typing.Union[SourcesSchema, list, tuple, ],
        'size': typing.Union[SizeSchema, decimal.Decimal, int, ],
        'lang': typing.Union[LangSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_text = api_client.QueryParameter(
    name="text",
    style=api_client.ParameterStyle.FORM,
    schema=TextSchema,
    required=True,
    explode=True,
)
request_query_focus_point_lat = api_client.QueryParameter(
    name="focus.point.lat",
    style=api_client.ParameterStyle.FORM,
    schema=FocusPointLatSchema,
    explode=True,
)
request_query_focus_point_lon = api_client.QueryParameter(
    name="focus.point.lon",
    style=api_client.ParameterStyle.FORM,
    schema=FocusPointLonSchema,
    explode=True,
)
request_query_boundary_rect_min_lat = api_client.QueryParameter(
    name="boundary.rect.min_lat",
    style=api_client.ParameterStyle.FORM,
    schema=BoundaryRectMinLatSchema,
    explode=True,
)
request_query_boundary_rect_max_lat = api_client.QueryParameter(
    name="boundary.rect.max_lat",
    style=api_client.ParameterStyle.FORM,
    schema=BoundaryRectMaxLatSchema,
    explode=True,
)
request_query_boundary_rect_min_lon = api_client.QueryParameter(
    name="boundary.rect.min_lon",
    style=api_client.ParameterStyle.FORM,
    schema=BoundaryRectMinLonSchema,
    explode=True,
)
request_query_boundary_rect_max_lon = api_client.QueryParameter(
    name="boundary.rect.max_lon",
    style=api_client.ParameterStyle.FORM,
    schema=BoundaryRectMaxLonSchema,
    explode=True,
)
request_query_boundary_circle_lat = api_client.QueryParameter(
    name="boundary.circle.lat",
    style=api_client.ParameterStyle.FORM,
    schema=BoundaryCircleLatSchema,
    explode=True,
)
request_query_boundary_circle_lon = api_client.QueryParameter(
    name="boundary.circle.lon",
    style=api_client.ParameterStyle.FORM,
    schema=BoundaryCircleLonSchema,
    explode=True,
)
request_query_boundary_circle_radius = api_client.QueryParameter(
    name="boundary.circle.radius",
    style=api_client.ParameterStyle.FORM,
    schema=BoundaryCircleRadiusSchema,
    explode=True,
)
request_query_boundary_country = api_client.QueryParameter(
    name="boundary.country",
    style=api_client.ParameterStyle.FORM,
    schema=BoundaryCountrySchema,
)
request_query_boundary_gid = api_client.QueryParameter(
    name="boundary.gid",
    style=api_client.ParameterStyle.FORM,
    schema=BoundaryGidSchema,
    explode=True,
)
request_query_layers = api_client.QueryParameter(
    name="layers",
    style=api_client.ParameterStyle.FORM,
    schema=LayersSchema,
)
request_query_sources = api_client.QueryParameter(
    name="sources",
    style=api_client.ParameterStyle.FORM,
    schema=SourcesSchema,
)
request_query_size = api_client.QueryParameter(
    name="size",
    style=api_client.ParameterStyle.FORM,
    schema=SizeSchema,
    explode=True,
)
request_query_lang = api_client.QueryParameter(
    name="lang",
    style=api_client.ParameterStyle.FORM,
    schema=LangSchema,
    explode=True,
)
_auth = [
    'ApiKeyAuth',
]
SchemaFor200ResponseBodyApplicationJson = PeliasResponse


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: schemas.Unset = schemas.unset
    headers: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
)
_status_code_to_response = {
    '200': _response_for_200,
    '400': _response_for_400,
}
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _search_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _search_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _search_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _search_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Search for location and other info using a place name or address (forward geocoding).
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value

        prefix_separator_iterator = None
        for parameter in (
            request_query_text,
            request_query_focus_point_lat,
            request_query_focus_point_lon,
            request_query_boundary_rect_min_lat,
            request_query_boundary_rect_max_lat,
            request_query_boundary_rect_min_lon,
            request_query_boundary_rect_max_lon,
            request_query_boundary_circle_lat,
            request_query_boundary_circle_lon,
            request_query_boundary_circle_radius,
            request_query_boundary_country,
            request_query_boundary_gid,
            request_query_layers,
            request_query_sources,
            request_query_size,
            request_query_lang,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(
                status=response.status,
                reason=response.reason,
                api_response=api_response
            )

        return api_response


class Search(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def search(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def search(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def search(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def search(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._search_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._search_oapg(
            query_params=query_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


