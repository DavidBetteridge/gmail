import base64
import google.oauth2.credentials
import googleapiclient.discovery
import json
from email.mime.text import MIMEText
from httplib2 import Credentials

API_SERVICE_NAME = 'gmail'
API_VERSION = 'v1'

def __persist_credentials(credentials: dict):
  with open("persisted_credentials.json", "w") as f:
    f.write(json.dumps(credentials))

def __load_credentials() -> dict:
  with open("persisted_credentials.json", "r") as f:
    creds = f.read()
  return json.loads(creds)

def __credentials_to_dict(credentials: Credentials) -> dict:
  return {'token': credentials.token,
          'refresh_token': credentials.refresh_token,
          'token_uri': credentials.token_uri,
          'client_id': credentials.client_id,
          'client_secret': credentials.client_secret,
          'scopes': credentials.scopes}

def send_test_email():
  # Load credentials from the session.
  stored_creds = __load_credentials()
  credentials = google.oauth2.credentials.Credentials(**stored_creds)

  message = MIMEText("this is the body")
  message['to'] = "david+gmail@hivemap.io"
  message['from'] = ""  # This is ignored
  message['subject'] = "this is the subject"
  raw = base64.urlsafe_b64encode(message.as_bytes())
  raw = raw.decode()
  body = {'raw': raw}

  gmail = googleapiclient.discovery.build(
      API_SERVICE_NAME, API_VERSION, credentials=credentials)

  message = (gmail.users().messages().send(userId="me", body=body)
            .execute())  

  # Save credentials back to session in case access token was refreshed.
  __persist_credentials(__credentials_to_dict(credentials))

send_test_email()