from pydantic import BaseSettings
from dotenv import load_dotenv
import os

load_dotenv()


class Settings(BaseSettings):
    google_auth_credentials: dict = {
        "web": {
            "client_id": os.environ.get('APP_GOOGLE_CLIENT_ID'),
            "client_secret": os.environ.get('APP_GOOGLE_CLIENT_SECRET'),
            "redirect_uri": "http://localhost:8000/api/v1/auth/callback",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://accounts.google.com/o/oauth2/token",
            "userinfo_uri": "https://www.googleapis.com/oauth2/v1/userinfo",
            "scope": ["email", "profile"],
            "prompt": "consent",
        }
    }

    class Config:
        env_prefix = "APP_"


settings = Settings()
google_auth_credentials = settings.google_auth_credentials
