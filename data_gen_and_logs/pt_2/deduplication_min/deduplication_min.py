from csv import reader, writer

with open('output.tsv', 'w') as w_file:
    file_writer = writer(w_file, delimiter="\t")
    file_writer.writerow(['userid', 'timestamp', 'action', 'value', 'testids'])
    with open("log.dsv", 'r', encoding='utf-8') as r_file:
        file_reader = reader(r_file, delimiter="\t")
        deduplicated_logs = set()
        logs = []
        tmp_dict = {}
        for row in file_reader:
            format_dict = {"userid": "", "timestamp": "", "action": "", "value": "", "testids": ""}
            for value in row:
                item = value.split("=")
                format_dict[item[0]] = item[1]
            deduplicated_logs.add(tuple(format_dict.values()))
            logs.append(tuple(format_dict.values()))
        for row in deduplicated_logs:
            tmp_dict[row] = True
        for row in logs:
            if tmp_dict[row]:
                tmp_dict[row] = False
                file_writer.writerow(row)
