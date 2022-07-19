N = list(map(int,input().split()))

def solv(x):
    total = 0
    for i in N:
        total += i**2
    mark = total%10
    print(mark)

solv(N)

