# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications. All endpoints are versioned individually to allow for granular upgrades. We follow the [Semantic Versioning scheme](https://semver.org/).  # noqa: E501

    The version of the OpenAPI document: 5.0.0
    Contact: support@stadiamaps.com
    Generated by: https://openapi-generator.tech
"""

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


class ValhallaLanguages(
    schemas.EnumBase,
    schemas.StrSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    
    @schemas.classproperty
    def BGBG(cls):
        return cls("bg-BG")
    
    @schemas.classproperty
    def CAES(cls):
        return cls("ca-ES")
    
    @schemas.classproperty
    def CSCZ(cls):
        return cls("cs-CZ")
    
    @schemas.classproperty
    def DADK(cls):
        return cls("da-DK")
    
    @schemas.classproperty
    def DEDE(cls):
        return cls("de-DE")
    
    @schemas.classproperty
    def ELGR(cls):
        return cls("el-GR")
    
    @schemas.classproperty
    def ENGB(cls):
        return cls("en-GB")
    
    @schemas.classproperty
    def ENUSXPIRATE(cls):
        return cls("en-US-x-pirate")
    
    @schemas.classproperty
    def ENUS(cls):
        return cls("en-US")
    
    @schemas.classproperty
    def ESES(cls):
        return cls("es-ES")
    
    @schemas.classproperty
    def ETEE(cls):
        return cls("et-EE")
    
    @schemas.classproperty
    def FIFI(cls):
        return cls("fi-FI")
    
    @schemas.classproperty
    def FRFR(cls):
        return cls("fr-FR")
    
    @schemas.classproperty
    def HIIN(cls):
        return cls("hi-IN")
    
    @schemas.classproperty
    def HUHU(cls):
        return cls("hu-HU")
    
    @schemas.classproperty
    def ITIT(cls):
        return cls("it-IT")
    
    @schemas.classproperty
    def JAJP(cls):
        return cls("ja-JP")
    
    @schemas.classproperty
    def NBNO(cls):
        return cls("nb-NO")
    
    @schemas.classproperty
    def NLNL(cls):
        return cls("nl-NL")
    
    @schemas.classproperty
    def PLPL(cls):
        return cls("pl-PL")
    
    @schemas.classproperty
    def PTBR(cls):
        return cls("pt-BR")
    
    @schemas.classproperty
    def PTPT(cls):
        return cls("pt-PT")
    
    @schemas.classproperty
    def RORO(cls):
        return cls("ro-RO")
    
    @schemas.classproperty
    def RURU(cls):
        return cls("ru-RU")
    
    @schemas.classproperty
    def SKSK(cls):
        return cls("sk-SK")
    
    @schemas.classproperty
    def SLSI(cls):
        return cls("sl-SI")
    
    @schemas.classproperty
    def SVSE(cls):
        return cls("sv-SE")
    
    @schemas.classproperty
    def TRTR(cls):
        return cls("tr-TR")
    
    @schemas.classproperty
    def UKUA(cls):
        return cls("uk-UA")
