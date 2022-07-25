numbers = list(range(1,10001))
gener_num = list()

for i in range(1, 10001):
    for j in str(i):
        i += int(j)
    gener_num.append(i)

self_num = [i for i in numbers if i not in gener_num]
for i in self_num:
    print(i)
