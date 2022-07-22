alpha = str(input())
alpha = alpha.lower()
a_count = {'a':0, 'b':0, 'c':0, 'd':0, 'e':0, 'f':0, 'g':0, 'h':0, 'i':0, 
           'j':0, 'k':0, 'l':0, 'n':0, 'm':0, 'o':0, 'p':0, 'q':0, 'r':0,
          's':0, 't':0, 'u':0, 'v':0, 'w':0, 'x':0, 'y':0, 'z':0}

for i in alpha:
    a_count[i] += 1

res = [k for k,v in a_count.items() if max(a_count.values()) == v]

if len(res) > 1 :
    print('?')
else:
    print(res.pop().upper())