from csv import reader


performance_popularity = {}
with open("ticket_logs.csv", 'r', encoding='utf-8') as r_file:
    file_reader = reader(r_file, delimiter=",")
    for row in file_reader:
        performance_name, phone = row[0], row[1]
        if performance_name not in performance_popularity:
            performance_popularity[performance_name] = set()
        for ch in phone:
            if not ch.isdigit():
                phone = phone.replace(ch, '', 1)
        if len(phone) == 11:
            performance_popularity[performance_name].add(phone)
best_performance_stats = 0
for performance in performance_popularity:
    best_performance_stats = max(best_performance_stats, len(performance_popularity[performance]))
print(best_performance_stats)
