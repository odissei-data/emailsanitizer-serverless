import json
import re
import typing
import azure.functions as func


async def main(req: func.HttpRequest) -> func.HttpResponse:
    req_body = req.get_json()

    if not req_body.get('data'):
        return func.HttpResponse(
            "Data field cannot be empty",
            status_code=400
        )

    replacement = req_body.get("replacement_email") or ""
    result = sanitize(req_body['data'], replacement)

    return func.HttpResponse(
        body=json.dumps({
            "data": str(result),
            "replacement_email": replacement
        }),
        status_code=200,
        mimetype='application/json'
    )

def sanitize(data: str, replacement_email: str):
    email_regex = re.compile("([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
    return re.sub(email_regex, replacement_email, data)
