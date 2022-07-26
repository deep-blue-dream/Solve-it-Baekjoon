n, x = map(int,input().split())                  # n은 수열을 이루는 정수의 개수, x는 비교할 정수
print(*(i for i in list(map(int, input().split())) if x > i))