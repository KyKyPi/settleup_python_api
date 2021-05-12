from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Group:
    """dataclass for group request data"""
    converted_to_currency: str
    invite_link: str
    invite_link_active: bool
    invite_link_hash: str
    last_changed: int
    minimize_debts: bool
    name: str
    owner_color: str
    group_id: str
    order: int
    color: str
    member_id: str

    @classmethod
    def json_to_class(cls, user_group, group_json) -> Group:
        """classmethod to convert json dict information to a class instance
        :param user_group: dict of group information from a userGroups request
        :param group_json: dict of group json data
        """
        group = cls(
            converted_to_currency=group_json['ownerColor'],
            invite_link=group_json['inviteLink'],
            invite_link_active=group_json['inviteLinkActive'],
            invite_link_hash=group_json['inviteLinkHash'],
            last_changed=group_json['lastChanged'],
            minimize_debts=group_json['minimizeDebts'],
            name=group_json['name'],
            owner_color=group_json['ownerColor'],
            group_id=user_group.group_id,
            order=user_group.order,
            color=user_group.color,
            member_id=user_group.member_id,
        )
        return group


@dataclass
class UserGroupView:
    """dataclass for userGroups request data"""
    group_id: str
    order: int
    color: str
    member_id: str

    @classmethod
    def from_dict(cls, group_id, group_view_dict) -> UserGroupView:
        """classmethod to convert json dict information to a class instance
        :param group_id: group id
        :param group_view_dict: dict of group json data
        """
        return cls(
            group_id=group_id,
            order=group_view_dict['order'],
            color=group_view_dict['color'],
            member_id=group_view_dict['member'],
        )
