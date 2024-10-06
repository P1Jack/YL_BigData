from csv import reader
from datetime import *


users = {}
cohorts = {}
weeks = [6, 13, 20, 27]
with open("log.tsv", 'r', encoding='utf-8') as r_file:
    file_reader = reader(r_file, delimiter="\t")
    for row_number, row in enumerate(file_reader):
        if row_number:
            user_id, timestamp = row[0], row[1].split('T')[0]
            ym, d = timestamp[:7], int(timestamp[8:])
            cur_date = datetime.strptime(timestamp, '%Y-%m-%d')
            # print(cur_date, datetime.strptime(ym, '%Y-%m') - cur_date)
            # if user_id not in users:
            #     users[user_id] = cur_date
            # if users[user_id]
            # if ym not in cohorts:
            #     cohorts[ym] = {0: 0, 1: 0, 2: 0, 3: 0}
            # for i in range(3):
            #     if d