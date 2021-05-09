import desert
from group import Group, UserGroupView
import pyrebase
import requests
import json
import user_auth_config
from typing import List


class SettleUp:

    def __init__(self):
        config = {
            "apiKey": "AIzaSyCfMEZut1bOgu9d1NHrJiZ7ruRdzfKEHbk",
            "authDomain": "settle-up-sandbox.firebaseapp.com",
            "databaseURL": "https://settle-up-sandbox.firebaseio.com",
            "storageBucket": "settle-up-sandbox.appspot.com"
        }

        firebase = pyrebase.initialize_app(config)

        auth = firebase.auth()
        self.user = auth.sign_in_with_email_and_password(user_auth_config.email, user_auth_config.password)

        # TODO: Implement refresh token. Tokens expire after 1 hour
        self.user = auth.refresh(self.user['refreshToken'])
        # now we have a fresh token
        self.user['idToken']

        self.payload = {'auth': self.user['idToken']}

    def get_groups(self) -> List[Group]:
        # usergroup_json = api.request("userGroups")
        r = requests.get('https://settle-up-sandbox.firebaseio.com/userGroups/' + str(self.user['userId'] + '.json'),
                         params=self.payload)
        usergroup_json = json.loads(r.text)

        # # Create a schema for the Group class.
        # usergroup_schema = desert.schema(UserGroupView)
        # # Load the data.
        # user_groups = usergroup_schema.load(usergroup_json)

        user_groups = []
        for group_id, group in usergroup_json.items():
            user_group_view = UserGroupView(group_id, group['order'], group['color'], group['member'])
            user_groups.append(user_group_view)

        groups = []
        for user_group in user_groups:
            # group_json = api.request("group", group_id=user_group.group_id)

            r = requests.get('https://settle-up-sandbox.firebaseio.com/groups/' + str(user_group.group_id + '.json'),
                             params=self.payload)
            group_json = json.loads(r.text)

            # # Create a schema for the Group class.
            # group_schema = desert.schema(Group)
            # # Load the data.
            # group = group_schema.load(group_json)

            # for group in group_json:
            group = group_json
            group = Group(
                converted_to_currency=group['ownerColor'],
                invite_link=group['inviteLink'],
                invite_link_active=group['inviteLinkActive'],
                invite_link_hash=group['inviteLinkHash'],
                last_changed=group['lastChanged'],
                minimize_debts=group['minimizeDebts'],
                name=group['name'],
                owner_color=group['ownerColor'],
                group_id=user_group.group_id,
                order=user_group.order,
                color=user_group.color,
                member_id=user_group.member_id,
            )
            groups.append(group)
        return groups

settleup = SettleUp()
groups = settleup.get_groups()
for group in groups:
    print(group)
    print(group.group_id)
