from itertools import combinations

n,m = map(int,input().split())
cards = list(map(int, input().split()))

total=0

for card in combinations(cards,3):
    if sum(card) <= m and sum(card) > total:
        total = sum(card)
print(total)
            