angle = [int(input()) for _ in range(3)]

if sum(angle) == 180:
    if len(set(angle)) == 1:
        print("Equilateral")
    elif len(set(angle)) == 2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")
