# Azure Functions

Refer to [Serverless docs](https://serverless.com/framework/docs/providers/azure/guide/intro/) for more information.

## Installation

This package was developed using the [Serverless framework](); follow the instructions related to the client of your usage therein. Test (and debug accordingly) with `sls offline`, to run an offline version of the code.

Once you've installed the framework, start hacking.

## Development

Develop as usual. Update requirements.txt (ideally with exact version pinning) as you go along. Test locally with `sls offline`

## Tests

Now has tests included using Unittest framework. Run them locally with `python -m unittest` in the root directory.

## Deployment

Once happy with your work, inspect the `serverless.yml` file to determine deployment options. This one, obviously, is aimed at Azure (there are different templates for different clouds, but the structure is interchangeable). If satisfied, login to Azure via cli (need the `azcli` package for this), then do `sls deploy` to deploy.

The result is a Function App on Azure, with two functions strapped in.

## API endpoints.

Here follows a documentation of the two functions exposed.

### Version

Accepted methods: GET 
Request params/body: null
Successfully returns: string
Otherwise returns: 405, 500, 40x
Purpose: Returns a string to denote the current version of the app. This is hardcoded, so check `src/handlers/version.py` for the string contents.

### Sanitize

Accepted methods: POST 
Request params/body: JSON object, containing two items: `data` (str) and `replacement_email` (str).
Successfully returns: JSON object, containing two items: `data` (str) and `replacement_email` (str).
Otherwise returns: 405, 500, 40x
Purpose: Returns your original `data` (which may contain email addresses), replaced by the string in `replacement_email`.
