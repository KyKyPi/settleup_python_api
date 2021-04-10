print("hello world")

import pyrebase

config = {
  "apiKey": "AIzaSyCfMEZut1bOgu9d1NHrJiZ7ruRdzfKEHbk",
  "authDomain": "settle-up-sandbox.firebaseapp.com",
  "databaseURL": "https://settle-up-sandbox.firebaseio.com",
  "storageBucket": "settle-up-sandbox.appspot.com"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
# auth.create_user_with_email_and_password("email@gmail.com", "password")
user = auth.sign_in_with_email_and_password("email@gmail.com", "password")
print(user)
# before the 1 hour expiry:
user = auth.refresh(user['refreshToken'])
# now we have a fresh token
user['idToken']
print(user)

db = firebase.database()
print(db)

# users = db.child("users").get()
# print(users.val()) # {"Morty": {"name": "Mortimer 'Morty' Smith"}, "Rick": {"name": "Rick Sanchez"}}




# auth = firebase.auth()
# #authenticate a user
# user = auth.sign_in_with_email_and_password("krburges@asu.edu", "123456")

# # ----------------------------------------------------------------------------
# # Generate Google OAuth2 access tokens
# # https://firebase.google.com/docs/database/rest/auth#google_oauth2_access_tokens
# # added google-auth with Poetry
#
# # https://google-auth.readthedocs.io/en/latest/user-guide.html
# import google.auth
# # credentials, project = google.auth.default()
#
# from google.oauth2 import service_account
#
# # This line not working
# # attempt poetry add requests
# from google.auth.transport.requests import AuthorizedSession
#
#
#
# # Define the required scopes
# # scopes = [
# #   "https://www.googleapis.com/auth/userinfo.email",
# #   "https://www.googleapis.com/auth/firebase.database"
# # ]
# scopes = [
#   "https://www.googleapis.com/auth/kylee.burgess.14@gmail.com",
#   "https://www.googleapis.com/auth/settle-up-sandbox"
# ]
#
# # Authenticate a credential with the service account
# credentials = service_account.Credentials.from_service_account_file(
#     "path/to/serviceAccountKey.json", scopes=scopes)
#
# # Use the credentials object to authenticate a Requests session.
# authed_session = AuthorizedSession(credentials)
# # response = authed_session.get(
# #     "https://<DATABASE_NAME>.firebaseio.com/users/ada/name.json")
# response = authed_session.get(
#     "https://settle-up-sandbox.firebaseio.com/users/ada/name.json")
#
# # # Or, use the token directly, as described in the "Authenticate with an
# # # access token" section below. (not recommended)
# # request = google.auth.transport.requests.Request()
# # credentials.refresh(request)
# # access_token = credentials.token
# ----------------------------------------------------------------------------