# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 7.0.0
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ValhallaLanguages(str, Enum):
    """
    ValhallaLanguages
    """

    """
    allowed enum values
    """
    BG_MINUS_BG = 'bg-BG'
    CA_MINUS_ES = 'ca-ES'
    CS_MINUS_CZ = 'cs-CZ'
    DA_MINUS_DK = 'da-DK'
    DE_MINUS_DE = 'de-DE'
    EL_MINUS_GR = 'el-GR'
    EN_MINUS_GB = 'en-GB'
    EN_MINUS_US_MINUS_X_MINUS_PIRATE = 'en-US-x-pirate'
    EN_MINUS_US = 'en-US'
    ES_MINUS_ES = 'es-ES'
    ET_MINUS_EE = 'et-EE'
    FI_MINUS_FI = 'fi-FI'
    FR_MINUS_FR = 'fr-FR'
    HI_MINUS_IN = 'hi-IN'
    HU_MINUS_HU = 'hu-HU'
    IT_MINUS_IT = 'it-IT'
    JA_MINUS_JP = 'ja-JP'
    NB_MINUS_NO = 'nb-NO'
    NL_MINUS_NL = 'nl-NL'
    PL_MINUS_PL = 'pl-PL'
    PT_MINUS_BR = 'pt-BR'
    PT_MINUS_PT = 'pt-PT'
    RO_MINUS_RO = 'ro-RO'
    RU_MINUS_RU = 'ru-RU'
    SK_MINUS_SK = 'sk-SK'
    SL_MINUS_SI = 'sl-SI'
    SV_MINUS_SE = 'sv-SE'
    TR_MINUS_TR = 'tr-TR'
    UK_MINUS_UA = 'uk-UA'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ValhallaLanguages from a JSON string"""
        return cls(json.loads(json_str))


