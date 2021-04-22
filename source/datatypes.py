from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, auto
import desert


@dataclass
class Group:
    convertedToCurrency: Currency
    inviteLink: str
    inviteLinkActive: bool
    inviteLinkHash: str
    lastChanged: int
    minimizeDebts: bool
    name: str
    ownerColor: str


class Currency(Enum):
    EUR = auto()
    USD = auto()


Currency.USD

