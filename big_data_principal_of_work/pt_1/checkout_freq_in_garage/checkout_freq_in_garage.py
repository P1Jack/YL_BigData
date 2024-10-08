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
class UserCheckouts:
    userid: str
    frequency: int


def parse_user_event(line):
    row = line.strip().split('\t')
    if row[0] == 'userid' or row[2] != 'checkout':
        yield from ()
    else:
        yield UserEvent(
            userid=row[0],
            time=datetime.fromisoformat(row[1]),
            action=row[2]
        )


# def unicalize_users(inp: Iterable[UserEvent]) -> Iterable[UserEvent]:
#     for us in inp:
#         yield us
#         break


def count_users_checkouts(inp: Iterable[UserEvent]) -> Iterable[UserCheckouts]:
    count = 0
    for us in inp:
        userid = us.userid
        count += 1
    yield UserCheckouts(userid=userid, frequency=count)


def process(mrjob: SimpleMapReduce) -> SimpleMapReduce:
    return mrjob.map(parse_user_event). \
            reduce(count_users_checkouts, key=['userid'])


with open("log.tsv", "r") as input_stream:
    mrjob = process(SimpleMapReduce(input_stream))
    for item in mrjob.output():
        print(item.userid, item.frequency)