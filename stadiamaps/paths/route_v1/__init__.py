# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from stadiamaps.paths.route_v1 import Api

from stadiamaps.paths import PathValues

path = PathValues.ROUTE_V1