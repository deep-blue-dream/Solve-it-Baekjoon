N = int(input())
keys = [input() for i in range(N)]

for i in keys:
    if 6 <= len(i) and  len(i) <= 9 :
        print("yes")
    else:
        print("no")
    
