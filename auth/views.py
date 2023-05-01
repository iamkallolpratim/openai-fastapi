from fastapi import Request, Response, status
from dotenv import load_dotenv
from google_auth_oauthlib.flow import Flow
from settings import google_auth_credentials
import google.auth


flow = Flow.from_client_config(
    google_auth_credentials,
    scopes=['https://www.googleapis.com/auth/userinfo.profile', 'openid' , 'https://www.googleapis.com/auth/userinfo.email'],
    redirect_uri='http://localhost:8000/api/v1/auth/callback'
)


def login():
    authorization_url = flow.authorization_url(prompt="consent")[0]
    print('Please go to this URL: {}'.format(authorization_url))
    return Response(status_code=status.HTTP_302_FOUND, headers={"Location": authorization_url})


async def callback(request: Request, code: str, state: str = None):
    # Exchange the authorization code for an access token
    flow.fetch_token(code=code)
    credentials = flow.credentials.to_json()
    return {"message": "Authentication successful", "credentials": credentials}

