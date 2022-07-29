h,m,s = map(int,input().split())
res_t = int(input())

res_h = res_t//3600
res_m = res_t//60
res_s = res_t % 60

def com_time(x,y,z):
    x += (res_h %24)
    y += (res_m % 60)
    z += res_s

    if z >= 60:
        z -= 60
        y += 1

    if y >= 60:
        y -= 60
        x += 1

    if x >= 24:
        x -= 24
    print(x,y,z, sep=" ")

com_time(h,m,s)

