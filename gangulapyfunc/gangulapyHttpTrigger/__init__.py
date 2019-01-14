import logging

import azure.functions as func
import os, json
import sendgrid


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    SENDGRID_API_KEY = 'Your sendgrid API key'
    sg = sendgrid.SendGridAPIClient(SENDGRID_API_KEY)
    data = {
        "personalizations": [
            {
            "to": [
                {
                "email": "ramya.gangula@microsoft.com"
                }
            ],
            "subject": "Sending with SendGrid is Fun"
            }
        ],
        "from": {
            "email": "ramya.gangula@microsoft.com"
        },
        "content": [
            {
            "type": "text/plain",
            "value": "and easy to do anywhere, even with Python"
            }
        ]
        }
    response = sg.client.mail.send.post(request_body=data)
    print(response.status_code)
    print(response.body)
    print(response.headers)
    
    
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello {name}!")
    else:
        return func.HttpResponse(
            "Please pass a name on the query string or in the request body",
            status_code=400
        )
