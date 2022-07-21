N = [int(input()) for i in range(10)]
res = []

for i in N : 
    res.append(i%42)
print(len(set(res)))
