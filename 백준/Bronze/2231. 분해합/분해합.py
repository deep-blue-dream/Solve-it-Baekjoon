n = int(input())

for i in range(1,n+1):
    total = 0
    solv = []
    for j in str(i):
        solv.append(j)
    a = list(map(int,solv))
    total = i + sum(a)
    
    if total == n:
        print(i)
        break
if total != n:
    print(0)
