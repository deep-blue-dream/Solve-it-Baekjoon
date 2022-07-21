# from sys import stdin
# 작업 1 - 입력을 받는다
# 작업 2 - 계산을 한다
# 작업 3 - 계산 된 값의 숫자들을 파악한다
# 작업 4 - 출력한다. 

Num_dict = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0}
#print(Num_dict[1])
N_list = []
total = 1

for i in range(3):
    N_list.append(int(input()))

    
for i in N_list:
    total *= i
    
def cnt(x):
    count = len(str(x))
    for i in range(count):
        Num_dict[x % 10] += 1
        x = x//10 
        
cnt(total)
            
            
for j in range(10):
    print(Num_dict[j])    
 