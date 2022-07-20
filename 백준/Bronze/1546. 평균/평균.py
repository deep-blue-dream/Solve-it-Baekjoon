N = int(input())
 
score = list(map(int,input().split()))

def fake_score(x):
    print((sum(x)/max(x)*100)/len(x))
    
fake_score(score)