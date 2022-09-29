#0과 1을 호출한 횟수 세기 위한 준비
count0 = [1,0]
count1 = [0,1]

#40보다 작은 횟수 

for i in range(2,41):
    count0.append(count0[i-1] + count0[i-2])
    count1.append(count1[i-1] + count1[i-2])
    
#알아보고자 하는 숫자 입력받기
for _ in range(int(input())):
    n = int(input())
    print(count0[n],count1[n])