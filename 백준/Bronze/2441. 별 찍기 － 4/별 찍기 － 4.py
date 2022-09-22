#점차 감소하는 별 찍기

n = int(input())

for i in range(1, n+1):
    space = " " * (i-1) 
    star = "*" * ((n+1)-i) 
    print(space + star)