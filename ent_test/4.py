import math


def s(x1, y1, x0, y0):
    if x1 >= x0:
        x = x1 // w * w
    else:
        x = math.ceil(x1 / w) * w
    if y1 >= y0:
        y = y1 // h * h
    else:
        y = math.ceil(y1 / h) * h
    t = min(abs(x1 - x) / u + abs(y1 - y) / v, abs(x1 - x) / v + abs(y1 - y) / u,
            w / v + abs(y1 - y) / v + (w - x1 % w) / u, h / v + abs(x1 - x) / v + (h - y1 % h) / u)
    return t, x, y


w, h = list(map(int, input().split()))
u, v = list(map(int, input().split()))
x0, y0 = list(map(int, input().split()))
N = int(input())


distances = []
for i in range(N):
    x1, y1 = list(map(int, input().split()))
    s1 = s(x1, y1, x0, y0)
    s2 = s(x0, y0, s1[1], s1[2])
    s3 = s(x0, y0, x1, y1)
    s4 = s(x1, y1, s3[1], s3[2])
    l = s1[0] + s2[0] + abs(s1[1] - s2[1]) / v + abs(s1[2] - s2[2]) / v
    l1 = s3[0] + s4[0]
    l1 += abs(s3[1] - s4[1]) / v + abs(s3[2] - s4[2]) / v
    if x0 // w != x1 // w and y0 // h != y1 // h:
        distances.append(min(round(l), round(l1),
                   round(abs(x1 - x0) / v + abs(y1 - y0) / u), round(abs(x1 - x0) / u + abs(y1 - y0) / v)))
    elif x0 // w != x1 // w:
        distances.append(min(round(l), round(l1), round(abs(x1 - x0) / u + abs(y1 - y0) / v)))
    elif y0 // h != y1 // h:
        distances.append(min(round(l), round(l1), round(abs(x1 - x0) / v + abs(y1 - y0) / u)))
    else:
        distances.append(min(round(l), round(l1)))

distances.sort()
mi = 10 ** 9
t1 = 0
t2 = 0
for i in range(len(distances) - 1):
    if distances[i + 1] - distances[i] < mi:
        mi = distances[i + 1] - distances[i]
        t1 = distances[i]
        t2 = distances[i + 1]
print(t1, t2)
