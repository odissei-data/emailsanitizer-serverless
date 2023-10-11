import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Version request received')
    return func.HttpResponse(
        str(return_version()),
            status_code=200
    )

def return_version():
    return {"version": "serverless 0.1.0"}
