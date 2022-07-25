N = [list(map(int,input().split())) for i in range(3)]
x = []
y = []
solv = []
for i in range(len(N)):
    x.append(N[i][0])
    y.append(N[i][1])

for i in x:
    if x.count(i) == 1:
        solv.append(i)
        
for j in y:
    if y.count(j) == 1:
        solv.append(j)
        
print(solv[0],solv[1])
