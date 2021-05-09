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

@dataclass
class UserGroupView:
    group_id: str
    order: int
    color: str
    member_id: str



