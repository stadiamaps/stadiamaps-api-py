# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.  # noqa: E501

    The version of the OpenAPI document: 5.0.5
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


import re  # noqa: F401
import io
import warnings

from pydantic import validate_arguments, ValidationError
from typing_extensions import Annotated

from pydantic import Field, confloat, conint

from typing import Optional, Union

from stadiamaps.models.height_request import HeightRequest
from stadiamaps.models.height_response import HeightResponse
from stadiamaps.models.tz_response import TzResponse

from stadiamaps.api_client import ApiClient
from stadiamaps.api_response import ApiResponse
from stadiamaps.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class GeospatialApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client

    @validate_arguments
    def elevation(self, height_request : Optional[HeightRequest] = None, **kwargs) -> HeightResponse:  # noqa: E501
        """Get the elevation profile along a polyline or at a point.  # noqa: E501

        The Stadia elevation API allows you to get the elevation of any point on earth. You can pass either a simple set of points or a Google encoded polyline string. This pairs well with our routing APIs, so you can generate an elevation profile for your next bike or run.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.elevation(height_request, async_req=True)
        >>> result = thread.get()

        :param height_request:
        :type height_request: HeightRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: HeightResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the elevation_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.elevation_with_http_info(height_request, **kwargs)  # noqa: E501

    @validate_arguments
    def elevation_with_http_info(self, height_request : Optional[HeightRequest] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get the elevation profile along a polyline or at a point.  # noqa: E501

        The Stadia elevation API allows you to get the elevation of any point on earth. You can pass either a simple set of points or a Google encoded polyline string. This pairs well with our routing APIs, so you can generate an elevation profile for your next bike or run.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.elevation_with_http_info(height_request, async_req=True)
        >>> result = thread.get()

        :param height_request:
        :type height_request: HeightRequest
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(HeightResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'height_request'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method elevation" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        if _params['height_request'] is not None:
            _body_params = _params['height_request']

        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # set the HTTP header `Content-Type`
        _content_types_list = _params.get('_content_type',
            self.api_client.select_header_content_type(
                ['application/json']))
        if _content_types_list:
                _header_params['Content-Type'] = _content_types_list

        # authentication setting
        _auth_settings = ['ApiKeyAuth']  # noqa: E501

        _response_types_map = {
            '200': "HeightResponse",
        }

        return self.api_client.call_api(
            '/elevation/v1', 'POST',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))

    @validate_arguments
    def tz_lookup(self, lat : Annotated[Union[confloat(le=90, ge=-90, strict=True), conint(le=90.0, ge=-90.0, strict=True)], Field(..., description="The latitude of the point you are interested in.")], lng : Annotated[Union[confloat(le=180, ge=-180, strict=True), conint(le=180.0, ge=-180.0, strict=True)], Field(..., description="The longitude of the point you are interested in.")], timestamp : Annotated[Optional[conint(strict=True, le=8200290900000, ge=0)], Field(description="The UNIX timestamp at which the UTC and DST offsets will be calculated. This defaults to the present time. This endpoint is not necessarily guaranteed to be accurate for timestamps that occurred in the past. Time zone geographic boundaries change over time, so if the point you are querying for was previously in a different time zone, historical results will not be accurate. If, however, the point has been in the same geographic time zone for a very long time (ex: `America/New_York`), the historical data may be accurate for 100+ years in the past (depending on how far back the IANA TZDB rules have been specified).")] = None, **kwargs) -> TzResponse:  # noqa: E501
        """Get the current time zone information for any point on earth.  # noqa: E501

        The Stadia TZ API provides time zone information, as well as information about any special offset (such as DST) in effect based on the latest IANA TZDB. Note that this API may not be accurate for timestamps in the past and does not claim to report precise nautical times in the open ocean beyond territorial waters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.tz_lookup(lat, lng, timestamp, async_req=True)
        >>> result = thread.get()

        :param lat: The latitude of the point you are interested in. (required)
        :type lat: float
        :param lng: The longitude of the point you are interested in. (required)
        :type lng: float
        :param timestamp: The UNIX timestamp at which the UTC and DST offsets will be calculated. This defaults to the present time. This endpoint is not necessarily guaranteed to be accurate for timestamps that occurred in the past. Time zone geographic boundaries change over time, so if the point you are querying for was previously in a different time zone, historical results will not be accurate. If, however, the point has been in the same geographic time zone for a very long time (ex: `America/New_York`), the historical data may be accurate for 100+ years in the past (depending on how far back the IANA TZDB rules have been specified).
        :type timestamp: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: TzResponse
        """
        kwargs['_return_http_data_only'] = True
        if '_preload_content' in kwargs:
            raise ValueError("Error! Please call the tz_lookup_with_http_info method with `_preload_content` instead and obtain raw data from ApiResponse.raw_data")
        return self.tz_lookup_with_http_info(lat, lng, timestamp, **kwargs)  # noqa: E501

    @validate_arguments
    def tz_lookup_with_http_info(self, lat : Annotated[Union[confloat(le=90, ge=-90, strict=True), conint(le=90.0, ge=-90.0, strict=True)], Field(..., description="The latitude of the point you are interested in.")], lng : Annotated[Union[confloat(le=180, ge=-180, strict=True), conint(le=180.0, ge=-180.0, strict=True)], Field(..., description="The longitude of the point you are interested in.")], timestamp : Annotated[Optional[conint(strict=True, le=8200290900000, ge=0)], Field(description="The UNIX timestamp at which the UTC and DST offsets will be calculated. This defaults to the present time. This endpoint is not necessarily guaranteed to be accurate for timestamps that occurred in the past. Time zone geographic boundaries change over time, so if the point you are querying for was previously in a different time zone, historical results will not be accurate. If, however, the point has been in the same geographic time zone for a very long time (ex: `America/New_York`), the historical data may be accurate for 100+ years in the past (depending on how far back the IANA TZDB rules have been specified).")] = None, **kwargs) -> ApiResponse:  # noqa: E501
        """Get the current time zone information for any point on earth.  # noqa: E501

        The Stadia TZ API provides time zone information, as well as information about any special offset (such as DST) in effect based on the latest IANA TZDB. Note that this API may not be accurate for timestamps in the past and does not claim to report precise nautical times in the open ocean beyond territorial waters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.tz_lookup_with_http_info(lat, lng, timestamp, async_req=True)
        >>> result = thread.get()

        :param lat: The latitude of the point you are interested in. (required)
        :type lat: float
        :param lng: The longitude of the point you are interested in. (required)
        :type lng: float
        :param timestamp: The UNIX timestamp at which the UTC and DST offsets will be calculated. This defaults to the present time. This endpoint is not necessarily guaranteed to be accurate for timestamps that occurred in the past. Time zone geographic boundaries change over time, so if the point you are querying for was previously in a different time zone, historical results will not be accurate. If, however, the point has been in the same geographic time zone for a very long time (ex: `America/New_York`), the historical data may be accurate for 100+ years in the past (depending on how far back the IANA TZDB rules have been specified).
        :type timestamp: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the ApiResponse.data will
                                 be set to none and raw_data will store the 
                                 HTTP response body without reading/decoding.
                                 Default is True.
        :type _preload_content: bool, optional
        :param _return_http_data_only: response data instead of ApiResponse
                                       object with status code, headers, etc
        :type _return_http_data_only: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(TzResponse, status_code(int), headers(HTTPHeaderDict))
        """

        _params = locals()

        _all_params = [
            'lat',
            'lng',
            'timestamp'
        ]
        _all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout',
                '_request_auth',
                '_content_type',
                '_headers'
            ]
        )

        # validate the arguments
        for _key, _val in _params['kwargs'].items():
            if _key not in _all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method tz_lookup" % _key
                )
            _params[_key] = _val
        del _params['kwargs']

        _collection_formats = {}

        # process the path parameters
        _path_params = {}

        # process the query parameters
        _query_params = []
        if _params.get('lat') is not None:  # noqa: E501
            _query_params.append(('lat', _params['lat']))

        if _params.get('lng') is not None:  # noqa: E501
            _query_params.append(('lng', _params['lng']))

        if _params.get('timestamp') is not None:  # noqa: E501
            _query_params.append(('timestamp', _params['timestamp']))

        # process the header parameters
        _header_params = dict(_params.get('_headers', {}))
        # process the form parameters
        _form_params = []
        _files = {}
        # process the body parameter
        _body_params = None
        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # authentication setting
        _auth_settings = ['ApiKeyAuth']  # noqa: E501

        _response_types_map = {
            '200': "TzResponse",
            '404': None,
        }

        return self.api_client.call_api(
            '/tz/lookup/v1', 'GET',
            _path_params,
            _query_params,
            _header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            response_types_map=_response_types_map,
            auth_settings=_auth_settings,
            async_req=_params.get('async_req'),
            _return_http_data_only=_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=_params.get('_preload_content', True),
            _request_timeout=_params.get('_request_timeout'),
            collection_formats=_collection_formats,
            _request_auth=_params.get('_request_auth'))
