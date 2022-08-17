import sys
input = sys.stdin.readline

a = []

for i in range(7):
    b = int(input())
    if b % 2 != 0:
        a.append(b)
    

if a:
    print(sum(a))
    print(min(a))
else:
    print(-1)
