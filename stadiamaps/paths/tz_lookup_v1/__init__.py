# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from stadiamaps.paths.tz_lookup_v1 import Api

from stadiamaps.paths import PathValues

path = PathValues.TZ_LOOKUP_V1