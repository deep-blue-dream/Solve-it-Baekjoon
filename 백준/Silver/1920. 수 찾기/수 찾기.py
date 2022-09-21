#표준 입출력 사용해볼 예정
import sys

#이곳에서 N,M은 사용할 일이 없다(딕셔너리를 통한 해시구조를 이용할 계획이므로)
n = map(int, sys.stdin.readline())

#대조군 입력
n_list = list(map(int, sys.stdin.readline().split()))

#딕셔너리 생성
n_dict = {}

#딕셔너리에 값 배치(해시 생성)
for i in n_list:
    n_dict[i] = 1
    

m = map(int,sys.stdin.readline())

#실험군 입력
m_list = list(map(int, sys.stdin.readline().split()))

#실험군에서 값을 하나씩 차출하여 비교군과 대조
for m in m_list:
    #값이 딕셔너리에 참, 거짓에 따라 1과 0 출력
    if m in n_dict:
        sys.stdout.write("1\n")
    else:
        sys.stdout.write("0\n")
    
