score = []
for i in range(5):
    a = int(input())
    if a >= 40:
        score.append(a)
    elif a < 40:
        score.append(40)

print(int(sum(score)/len(score)))
