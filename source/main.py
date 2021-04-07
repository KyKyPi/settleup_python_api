print("hello world")

# ----------------------------------------------------------------------------
# Generate Google OAuth2 access tokens
# https://firebase.google.com/docs/database/rest/auth#google_oauth2_access_tokens
# added google-auth with Poetry

# https://google-auth.readthedocs.io/en/latest/user-guide.html
import google.auth
credentials, project = google.auth.default()

from google.oauth2 import service_account

# This line not working
# attempt poetry add requests
from google.auth.transport.requests import AuthorizedSession



# Define the required scopes
scopes = [
  "https://www.googleapis.com/auth/userinfo.email",
  "https://www.googleapis.com/auth/firebase.database"
]

# Authenticate a credential with the service account
credentials = service_account.Credentials.from_service_account_file(
    "path/to/serviceAccountKey.json", scopes=scopes)

# Use the credentials object to authenticate a Requests session.
authed_session = AuthorizedSession(credentials)
# response = authed_session.get(
#     "https://<DATABASE_NAME>.firebaseio.com/users/ada/name.json")
response = authed_session.get(
    "https://settle-up-sandbox.firebaseio.com/users/ada/name.json")

# # Or, use the token directly, as described in the "Authenticate with an
# # access token" section below. (not recommended)
# request = google.auth.transport.requests.Request()
# credentials.refresh(request)
# access_token = credentials.token
# ----------------------------------------------------------------------------