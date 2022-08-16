import sys
input= sys.stdin.readline

for i in range(3):
    a = [int(input()) for n in range(int(input()))]
    if sum(a) > 0:
        print("+")
    elif sum(a) < 0:
        print("-")
    else:
        print(0)