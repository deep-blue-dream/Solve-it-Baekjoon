# 수를 뒤집는 방식을 구현하라? 

N,M = map(int, input().split())

def rev(x):
    final = ""
    res = str(x)
    res = list(res)
    res = list(reversed(res))
    for i in res:
        final += i
    x = final
    return int(x)

if rev(N) > rev(M):
    print(rev(N))
else:
    print(rev(M))