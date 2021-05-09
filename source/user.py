from dataclasses import dataclass


@dataclass
class User:
    id_token: str
    refresh_token: str
    user_id: str
