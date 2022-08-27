while True:
    triangle = list(map(int,input().split()))
    if sum(triangle) == 0:
        break
    max_line = max(triangle)
    triangle.remove(max_line)
    if triangle[0]**2 + triangle[1]**2 == max_line**2:
        print("right")
    else:
        print("wrong")