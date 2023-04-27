from fastapi import Request, Response, status
from dotenv import load_dotenv
from google_auth_oauthlib.flow import Flow
from settings import google_auth_credentials
import google.auth





flow = Flow.from_client_config(
    google_auth_credentials,
    scopes=["email", "profile"],
)


def login(request: Request):
    authorization_url, _ = flow.authorization_url(prompt="consent")
    return Response(status_code=status.HTTP_302_FOUND, headers={"Location": authorization_url})


def callback(request: Request, code: str, state: str = None):
    # Exchange the authorization code for an access token
    flow.fetch_token(code=code)
    credentials = flow.credentials
    print(credentials)

    return {"message": "Authentication successful"}
