N = int(input())
F = int(input())

changeN = (N - (N%100))

while True:
    if changeN % F == 0:
        break
    else :
        changeN += 1
print('{:02d}'.format(changeN%100))