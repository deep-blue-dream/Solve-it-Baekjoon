N = int(input())

for i in range(N):
    std, *score = map(int,input().split())
    adv_score = sum(score)/len(score)
    std_list=[]
    for j in score:
        if j > adv_score:
            std_list.append(j)
    per = round(len(std_list)/len(score)*100,3)
    print("{:.3f}%".format(per))