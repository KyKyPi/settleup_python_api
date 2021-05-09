from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto
from typing import List, Dict


@dataclass
class Transactions:
    category: str
    currency_code: str
    date_time: datetime
    exchange_rate: Dict[str, str]
    fixed_exchange_rate: bool
    items: List[TransactionItem]
    purpose: str
    receipt_url: str
    type: TransactionType
    who_paid: List[MemberWeight]


class TransactionType(Enum):
    EXPENSE = "expense"
    ...


@dataclass
class TransactionItem:
    amount: float
    for_whom: list


@dataclass
class MemberWeight:
    member_id: str
    weight: float
