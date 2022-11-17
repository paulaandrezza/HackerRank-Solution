a = [1, 2, 3, 4, 5]
d = 2

b = []

for i in range(len(a)):
    if(i+d >= len(a)):
        print("if ", a[i+d-len(a)])
        b.append(a[i+d-len(a)])
    else:
        print(a[i+d])
        b.append(a[i+d])
print(b)