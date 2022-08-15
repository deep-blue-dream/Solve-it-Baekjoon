mg= list(map(int, input().split()))
ms= list(map(int, input().split()))

if sum(mg) >= sum(ms):
    print(sum(mg))
else:
    print(sum(ms))