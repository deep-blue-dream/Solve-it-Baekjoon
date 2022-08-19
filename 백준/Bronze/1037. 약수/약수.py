import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int,(input().split())))
a = sorted(a)
if len(a) == 1:
    print(a[0]*a[0])
else:
    print(a[0]*a[len(a)-1])
