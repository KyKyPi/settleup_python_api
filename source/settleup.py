from dataclasses import asdict

from group import Group, UserGroupView
import pyrebase
import requests
import json
import user_auth_config
from typing import List
from user import Config


class SettleUp:
    """The main class for the python SettleUp API"""

    def __init__(self, config: Config):
        """Initialize the SettleUp instance with necessary auth config
        :param config: instance of Config class containing database auth config
        parameters
        """
        self.config = config
        """instance of Config class containing database auth config
        parameters"""

        firebase = pyrebase.initialize_app(asdict(self.config))

        auth = firebase.auth()
        self.user = auth.sign_in_with_email_and_password(
            user_auth_config.email,
            user_auth_config.password
        )
        """firebase user determined from email/password"""

        # TODO: Implement refresh token. Tokens expire after 1 hour
        self.user = auth.refresh(self.user['refreshToken'])
        # now we have a fresh token
        self.user['idToken']

        self.payload = {'auth': self.user['idToken']}
        """user id token parameter to be passed to database for auth"""
        self.firebase_url = config.databaseURL
        """database url"""

    def request(self, data_request, id) -> dict:
        """method to request data from the database, returns a json dict
        :param data_request: string of request type (ex. userGroups or groups)
        :param id: the required id to perform the request
        (ex. user_id or group_id)
        """
        payload = self.payload
        firebase_url = self.config.databaseURL
        r = requests.get(f'{firebase_url}/{data_request}/{id}.json',
                         params=payload)
        return json.loads(r.text)

    def get_groups(self) -> List[Group]:
        """method to request all groups for a specific user,
        returns a list of Group instances"""
        usergroup_json = self.request('userGroups', self.user['userId'])

        user_groups = []
        for group_id, usergroup_json in usergroup_json.items():
            user_group = UserGroupView.from_dict(group_id, usergroup_json)
            user_groups.append(user_group)

        groups = []
        for user_group in user_groups:
            group_json = self.request('groups', user_group.group_id)

            group = Group.json_to_class(user_group, group_json)
            groups.append(group)
        return groups


config = Config(
    apiKey="AIzaSyCfMEZut1bOgu9d1NHrJiZ7ruRdzfKEHbk",
    authDomain="settle-up-sandbox.firebaseapp.com",
    databaseURL="https://settle-up-sandbox.firebaseio.com",
    storageBucket="settle-up-sandbox.appspot.com"
)

settleup = SettleUp(config)
groups = settleup.get_groups()
for group in groups:
    print(group)
    print(group.group_id)
