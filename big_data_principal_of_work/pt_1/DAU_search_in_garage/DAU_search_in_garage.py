from simplemr import SimpleMapReduce
from dataclasses import dataclass
from datetime import *
from typing import Iterable


@dataclass
class UserEvent:
    userid: str
    time: datetime
    action: str


@dataclass
class UserDate:
    userid: str
    date: date


@dataclass
class DateDAU:
    date: date
    dau: int


def parse_user_event(line):
    row = line.strip().split('\t')
    if row[0] == 'userid' or row[2] != 'search':
        yield from ()
    else:
        yield UserEvent(
            userid=row[0],
            time=datetime.fromisoformat(row[1]),
            action=row[2]
        )


def user_event_to_user_date(ue: UserEvent) -> Iterable[UserDate]:
    yield UserDate(
        userid=ue.userid,
        date=ue.time.date()
    )


def unicalize_user_date(inp: Iterable[UserDate]) -> Iterable[UserDate]:
    for ud in inp:
        yield ud
        break


def group_users_by_date(inp: Iterable[UserDate]) -> Iterable[DateDAU]:
    count = 0
    for ud in inp:
        date = ud.date
        count += 1
    yield DateDAU(date=date, dau=count)


def process(mrjob: SimpleMapReduce) -> SimpleMapReduce:
    return mrjob.map(parse_user_event). \
        map(user_event_to_user_date). \
        reduce(unicalize_user_date, key=['userid', 'date']). \
        reduce(group_users_by_date, key=['date'])


with open("log.tsv", "r") as input_stream:
    mrjob = process(SimpleMapReduce(input_stream))
    for item in mrjob.output():
        print(item.date, item.dau)