import sys
input = sys.stdin.readline

a,b = map(int,input().split())
chick = int(input())

if 2*chick <= a+b :
    print(a+b-(2*chick))
else:
    print(a+b)
