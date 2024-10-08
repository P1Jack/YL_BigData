from simplemr import SimpleMapReduce
from dataclasses import dataclass
from datetime import *
from typing import Iterable


@dataclass
class UserEvent:
    userid: str
    time: datetime
    action: str
    value: float


@dataclass
class UserDateCheckout:
    userid: str
    date: str
    checkout: float


@dataclass
class MonthCheckouts:
    month: str
    value: int


def parse_user_event(line):
    row = line.strip().split('\t')
    if row[0] == 'userid' or row[2] != 'checkout':
        yield from ()
    else:
        yield UserDateCheckout(
            userid=row[0],
            date=datetime.fromisoformat(row[1]).strftime('%Y-%m'),
            checkout=float(row[3])
        )


def group_users_by_date(inp: Iterable[UserDateCheckout]) -> Iterable[MonthCheckouts]:
    value = 0
    for ud in inp:
        date = ud.date
        value += ud.checkout
    yield MonthCheckouts(month=date, value=value)


def process(mrjob: SimpleMapReduce) -> SimpleMapReduce:
    return mrjob.map(parse_user_event). \
            reduce(group_users_by_date, key=['date'])


with open("log.tsv", "r") as input_stream:
    mrjob = process(SimpleMapReduce(input_stream))
    for item in mrjob.output():
        print(item)
