n = int(input())
min_num = 1
max_num = 1
start = 1
count = 1

while True:
    if (min_num <= n and n <= max_num):
        break
    if max_num < n:
        count += 1
        min_num += start*(6*(count-2))
        max_num += start*(6*(count-1))
        #print(min_num,max_num)

print(count)


#bfs이용해야하나? 그래프를 그리는데 방향성에 맞춰서 점화식 적용하면 되나?
#알고리즘은 수학을 이용해?
#각 점에 따라서 6씩 증가하는 등차수열.
# 각 점에서 가장 max는 n+6을 넘길 수 없다.
#count = 1    1
#count = 2    2~7 +6
#count = 3    8~19 +12
#count = 4    20~37 +18
#count = 5    38~61 +24

#min_num
#max_num
# 두 점을 지정해서 그 사이값의 사이클을 구한다.
# 재귀함수를 선택한다?
#1,2,8,20,38
#1,7,19,37,61

#min_num : min_num + cir*(6*(count-2)) 누적합
#max_num : max_num + cir*(6*(count-1)) 누적합