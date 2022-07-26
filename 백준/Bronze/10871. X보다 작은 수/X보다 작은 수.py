n, x = map(int,input().split())                  # n은 수열을 이루는 정수의 개수, x는 비교할 정수
A = list(map(int, input().split()))              # 두 번째 입력받은 값을 이용해서 리스트(수열)를 만든다.

for i in range(n):                               #리스트 수 = n번만큼 반복한다
    if A[i] < x:                                 #리스트 A[i]값이 x보다 작다면
        print(A[i], end=" ")                     # 그 값을 출력한다, 쉼표로 구분해서 출력
