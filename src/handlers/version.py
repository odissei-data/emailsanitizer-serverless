import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Version request received')
    return func.HttpResponse(
        str({"version": "serverless 0.1.0"}),
        status_code=200
    )
