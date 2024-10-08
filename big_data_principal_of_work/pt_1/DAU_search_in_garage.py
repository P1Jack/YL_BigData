from simplemr import SimpleMapReduce


def process(mrjob: SimpleMapReduce) -> SimpleMapReduce:
     return mrjob.map(...)


with open("log.tsv", "r") as input_stream:
    mrjob = process(SimpleMapReduce(input_stream))
    for item in mrjob.output():
        print(item.date, item.dau)