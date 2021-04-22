# from source.datatypes import Currency

print("hello world")

import pyrebase
import requests
import json
from pprint import pprint
import desert
from datatypes import Group

import user_auth_config

config = {
  "apiKey": "AIzaSyCfMEZut1bOgu9d1NHrJiZ7ruRdzfKEHbk",
  "authDomain": "settle-up-sandbox.firebaseapp.com",
  "databaseURL": "https://settle-up-sandbox.firebaseio.com",
  "storageBucket": "settle-up-sandbox.appspot.com"
}

firebase = pyrebase.initialize_app(config)

auth = firebase.auth()
# user = auth.create_user_with_email_and_password("email@gmail.com", "password")
user = auth.sign_in_with_email_and_password(user_auth_config.email, user_auth_config.password)


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

# User Groups
# https://<environment>.firebaseio.com/userGroups/<user_id>.json
print("\nUser groups")
payload = {'auth': user['idToken']}
r = requests.get('https://settle-up-sandbox.firebaseio.com/userGroups/' + str(user['userId'] + '.json'), params=payload)
user_groups_json = json.loads(r.text)
group_id_list = []
for key, value in user_groups_json.items():
  print("Group: " + key)
  group_id_list.append(key)
  for key2, value2 in value.items():
    print("\t" + key2 + " : " + str(value2))
print("\n")
print(group_id_list)



# Group details
# https://<environment>.firebaseio.com/groups/<group_id>.json
print("\n Group details")
payload = {'auth': user['idToken']}
r = requests.get('https://settle-up-sandbox.firebaseio.com/groups/' + str(group_id_list[0] + '.json'), params=payload)
group_json = json.loads(r.text)
# for key, value in group_json.items():
#   print(key)
#   print("\t" + str(value))
# print("\n")
pprint(group_json)


# List of Members
# https://<environment>.firebaseio.com/members/<groups_id>.json
print("\n List of Members")
payload = {'auth': user['idToken']}
r = requests.get('https://settle-up-sandbox.firebaseio.com/members/' + str(group_id_list[0] + '.json'), params=payload)
members_json = json.loads(r.text)
# for key, value in members_json.items():
#   print("Member id: " + key)
#   for key2, value2 in value.items():
#     print("\t" + key2 + " : " + str(value2))
# print("\n")
pprint(members_json)

# Transactions
# https://<environment>.firebaseio.com/transactions/<group_id>.json
print("\n List of Transactions")
payload = {'auth': user['idToken']}
r = requests.get('https://settle-up-sandbox.firebaseio.com/transactions/' + str(group_id_list[0] + '.json'), params=payload)
transactions_json = json.loads(r.text)
# for key, value in transactions_json.items():
#   print("Transaction id: " + key)
#   for key2, value2 in value.items():
#     print("\t" + key2 + " : " + str(value2))
# # print(transactions_json)
# print("\n")
pprint(transactions_json)



# # Load some simple data types.
# data = {'passengers': [{'name': 'Alice', 'age': 21}, {'name': 'Bob', 'age': 22}]}


# Create a schema for the Group class.
schema = desert.schema(Group)

# Load the data.
group = schema.load(group_json)
# assert car == Car(passengers=[Person(name='Alice', age=21), Person(name='Bob', age=22)])

print(group)
