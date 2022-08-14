money = int(input())
count = int(input())
item_list = [list(map(int,input().split())) for _ in range(count)]
cost = 0
for i in item_list:
    cost += (i[0]*i[1])

if cost == money:
    print("Yes")
else:
    print("No")
                      
