n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 20]

dic = {}
rep = 0

for i in ar:
    if i not in dic:
        dic[i] = 0
    dic[i] += 1

for i in dic.values():
    if i > 1:
        rep += int(i/2)

print(rep)