a,b = map(int,input().split())

spear = (a * b) / 100

defence = a - spear

if defence < 100:
    print(1)
else :
    print(0)

