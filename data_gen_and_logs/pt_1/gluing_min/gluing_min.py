import csv as c

al = []
lt = {}
s = set()
d = {}
n = []


def dfs(j):
    if d[j] == 0:
        d[j] = 1
        n.append(j)
        for jj in lt[j]:
            dfs(jj)


with open("transaction_logs.csv", "r", encoding="utf-8") as file:
    f = c.reader(file, delimiter=",")
    g = list(f)
    for i in g:
        s.add(i[0])
        s.add(i[1])
        if i[0] not in lt:
            lt[i[0]] = [i[1]]
        else:
            lt[i[0]].append(i[1])
        if i[1] not in lt:
            lt[i[1]] = [i[0]]
        else:
            lt[i[1]].append(i[0])
    for i in list(s):
        d[i] = 0

    for i in lt:
        if d[i] == 0:
            dfs(i)
            n.append(0)
            al.append(n)
            n = []
    fgg = {}
    for i in al:
        for j in i:
            fgg[j] = i
    for i in g:
        fgg[i[0]][-1] += 1
    print(max([fgg[i][-1] for i in fgg]))
# for i in g:
    #     for j in al:
    #         if i[0] in j:
    #             j[-1] += 1
    #             break
