from sys import stdin

input = stdin.readline

n = int(input())
num_list = [0]*10001

for i in range(n):
    nums = int(input())
    num_list[nums] += 1

for i in range(len(num_list)):
    if num_list[i] !=0:
        for j in range(num_list[i]):
            print(i)