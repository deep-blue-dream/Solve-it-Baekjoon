N = int(input())
solv = []

for i in range(1,N+1):
    if i <100:
        solv.append(i)
    elif i > 100:
        check=list(str(i))
        if (int(check[0])-int(check[1])) == (int(check[1])-int(check[2])):
            solv.append(i) 
        
print(len(solv))