def solution(arr1, arr2):
    answer = []
    
    #두 리스트를 받는다. 리스트의 모양은 같다. 리스트의 덧셈을 구현하라.
    #각 열과 행에 맞춰서 더한다. 길이는 500을 넘지 않는다? 
    for i in range(len(arr1)): #arr1의 길이만큼 반복 0~1
        arr_sum=[]             #덧셈 작업할 리스트 생성
        for j in range(len(arr1[i])):   #arr1과 arr2의 각 인덱스별로 값을 뽑아서 더할 준비
            arr_sum.append(arr1[i][j]+arr2[i][j]) #arr_sum에, 각 값을 더해서 넣는다.
        answer.append(arr_sum) #answer에 넣는다.
            
    return answer