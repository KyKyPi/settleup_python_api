from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Group:
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
    group_id: str
    order: int
    color: str
    member_id: str

    @classmethod
    def from_dict(cls, group_id, group_view_dict) -> UserGroupView:
        return cls(
            group_id=group_id,
            order=group_view_dict['order'],
            color=group_view_dict['color'],
            member_id=group_view_dict['member'],
        )
