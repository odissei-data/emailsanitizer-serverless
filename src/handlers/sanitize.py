import json
import re

import azure.functions as func


async def main(req: func.HttpRequest) -> func.HttpResponse:
    req_body = req.get_json()
    email_regex = re.compile("([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")

    if not req_body.get('data'):
        return func.HttpResponse(
            "Data field cannot be empty",
            status_code=400
        )

    replacement = req_body.get("replacement_email") or ""

    response_data = re.sub(email_regex, replacement, req_body['data'])
    return func.HttpResponse(
        body=json.dumps({
            "data": response_data,
            "replacement_email": replacement
        }),
        status_code=200,
        mimetype='application/json'
    )
