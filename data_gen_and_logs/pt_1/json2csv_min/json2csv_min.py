from csv import writer
from json import load

with open('cases.json', 'r') as r_file:
    cases = sorted(load(r_file), key=lambda x: x['date'], reverse=True)

with open('incidents.csv', 'w') as w_file:
    file_writer = writer(w_file, delimiter=",")
    file_writer.writerow(['creature', 'place', 'danger', 'date'])
    for case in cases:
        file_writer.writerow([case['creature'], case['place'], case['danger'], case['date']])
