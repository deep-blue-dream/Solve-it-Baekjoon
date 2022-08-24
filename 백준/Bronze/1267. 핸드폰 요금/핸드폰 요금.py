N = int(input())
call_time = list(map(int,input().split()))
#print(call_time)

def call_cost(x):
    Y_cost = 0
    M_cost = 0
    
    for i in x:
        call_minute = 0
        call_second = 0
        call_minute += i // 60
        call_second += i % 60
        #print(call_minute, call_second)
        if call_second > 30 :
            Y_cost += ((call_minute+1) * 20)
            M_cost += ((call_minute+1) * 15)
            #print(i, Y_cost, M_cost)
        else:
            Y_cost += (((call_minute) * 20) + 10)
            M_cost += ((call_minute+1) * 15)
            #print(i, Y_cost, M_cost)
    if Y_cost == M_cost :
        print("Y", "M", Y_cost, sep=' ')
    elif Y_cost > M_cost :
        print("M", M_cost, sep=' ')
    else:
        print("Y", Y_cost, sep=' ')

call_cost(call_time)
        