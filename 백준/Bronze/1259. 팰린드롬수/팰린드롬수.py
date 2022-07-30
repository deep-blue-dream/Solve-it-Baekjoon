while True:
    x = int(input())
    
    if x == 0:
        break
    print("yes") if list(str(x)) == list(reversed(list(str(x)))) else print("no")