# Development guide

This Python package is 99% automatically generated by [OpenAPI Generator](https://openapi-generator.tech).
Version 7.x is required.
To regenerate the package with an updated API spec OR to increment the version number for any reason, run
the following command (make sure to replace `X.Y.Z` with the new version number!). Assumes that you have installed
openapi-generator via brew. The command invocation will vary for npm, Docker, and other installations, but the
arguments should remain the same.

```shell
openapi-generator generate -i https://api.stadiamaps.com/openapi.yaml -g python --strict-spec=true -o . -p disallowAdditionalPropertiesIfNotPresent=false -p packageName=stadiamaps -p packageUrl=https://github.com/stadiamaps/stadiamaps-api-py -p packageVersion=X.Y.Z
```

## Tests

The OpenAPI generator adds some unit tests, but these appear to be more or less worthless?
We add our own integration tests in `test/integration`.  You can run these via the following command line:

```shell
STADIA_API_KEY="YOUR-API-KEY" pytest
```

## Caveats

When running the generator, a number of files including the GitHub [python.yml](.github/workflows/python.yml)
action and [pyproject.toml](pyproject.toml). will be overwritten. This is generally the
right idea. However, the updated files will clobber several _intentional_ local modifications, so check your
git diff carefully before committing. You _will_ have to stage some chunks and remove others.
Sorry, not sorry; the automatic generator doesn't support enough configuration.

When making schema changes, you may need to temporarily remove [README.md](README.md) from
[.openapi-generator-ignore](.openapi-generator-ignore) and merge in the updated docs.

### Generator bugs

The following info is current as of v7.7.0.

The auto-generated code does not pass flake8, so we have disabled the checks.
