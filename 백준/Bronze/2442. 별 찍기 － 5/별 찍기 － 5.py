n = int(input())

for i in range(1,n+1):
    star = "*" * (i*2-1)
    stab = " " * (n-i)
    print(stab+star)