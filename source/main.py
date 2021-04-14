print("hello world")

import pyrebase
import requests
import json

config = {
  "apiKey": "AIzaSyCfMEZut1bOgu9d1NHrJiZ7ruRdzfKEHbk",
  "authDomain": "settle-up-sandbox.firebaseapp.com",
  "databaseURL": "https://settle-up-sandbox.firebaseio.com",
  "storageBucket": "settle-up-sandbox.appspot.com"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
user = auth.create_user_with_email_and_password("email@gmail.com", "password")

print(user)
# before the 1 hour expiry:
user = auth.refresh(user['refreshToken'])
# now we have a fresh token
user['idToken']
print(user)
print('\n')
print(user['idToken'])
print('\n')
print(user['refreshToken'])
print('\n\n')

payload = {'auth': user['idToken']}
r = requests.get('https://settle-up-sandbox.firebaseio.com/userGroups/' + str(user['userId'] + '.json'), params=payload)
print("url: " + r.url)
print('\n')
print("Text: " + r.text)
print(r.json())

d = json.loads(r.text)
print(d)

print(d['-MXu6cnWThBu4GkgnBnA']['color'])



