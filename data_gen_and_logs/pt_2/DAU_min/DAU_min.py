from csv import reader


DAU_dict = {}
with open("log.tsv", 'r', encoding='utf-8') as r_file:
    file_reader = reader(r_file, delimiter="\t")
    for row_number, row in enumerate(file_reader):
        if row_number:
            user_id, timestamp = row[0], row[1].split('T')[0]
            if timestamp not in DAU_dict:
                DAU_dict[timestamp] = set()
            DAU_dict[timestamp].add(user_id)
for key in DAU_dict.keys():
    print(key, len(DAU_dict[key]))
