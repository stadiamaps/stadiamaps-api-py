# coding: utf-8

"""
    Stadia Maps Geospatial APIs

    The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

    The version of the OpenAPI document: 9.0.0
    Contact: support@stadiamaps.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "stadiamaps"
VERSION = "6.0.0"
PYTHON_REQUIRES = ">= 3.8"
REQUIRES = [
    "urllib3 >= 1.25.3, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="Stadia Maps Geospatial APIs",
    author="Stadia Maps Support",
    author_email="support@stadiamaps.com",
    url="https://github.com/stadiamaps/stadiamaps-api-py",
    keywords=["OpenAPI", "OpenAPI-Generator", "Stadia Maps Geospatial APIs"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""
# Stadia Maps Python API Client

The Stadia Maps Geospatial APIs provide you with the data you need to build awesome applications.

For more information about the API, please visit [https://docs.stadiamaps.com](https://docs.stadiamaps.com)

## Installation & Usage
### pip install

```shell
pip install stadiamaps
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```shell
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

### Tests

Execute `pytest` to run the tests. These are run automatically via CI.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
import os
import stadiamaps
from stadiamaps.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.stadiamaps.com
# You can also use our EU endpoint to keep traffic within the EU like so:
# configuration = stadiamaps.Configuration(host="https://api-eu.stadiamaps.com")
# See configuration.py for a list of all supported configuration parameters.
configuration = stadiamaps.Configuration()

# Configure API key authorization. This example assumes it is injected via an environment
# variable.
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Enter a context with an instance of the API client
with stadiamaps.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = stadiamaps.GeocodingApi(api_client)
    text = "Põhja pst 27a" # str | The place name (address, venue name, etc.) to search for.

    try:
        # Search and geocode quickly based on partial input.
        api_response = api_instance.autocomplete(text)
        print("The response of GeocodingApi->autocomplete:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling GeocodingApi->autocomplete: %s\n" % e)
```
    """,  # noqa: E501
    package_data={"stadiamaps": ["py.typed"]},
)
