# 사이클 정렬!

사이클 정렬은 **제자리 정렬** 알고리즘, **불안정 정렬** 알고리즘으로 원래 배열에 대한 쓰기의 총합횟수 측면에서 이론적으로 최적인 비교정렬입니다.

- 정렬 할 배열을 사이클들로 나눌 수 있다는 아이디어를 기반으로합니다.
  사이클들은 그래프로 시각화 할 수 있습니다.
  i 번째 인덱스의 요소가 정렬 된 배열의 j 번째 인덱스에 있어야하는 경우 n 개의 노드와 노드 i에서 노드 j로 향하는 에지가 있습니다.


# 예시

    arr[] = {10, 5,  2,  3}
    index =  0   1   2   3
    cycle_start = 0 
    **item** = 10 = arr[0]
    
item을 넣을 위치를 찾으세요.  
   

     pos = cycle_start
        while (arr[i] < item)  
            pos++;
        
우리는 arr[3]에 10을 넣고 item을 arr[3]의 이전 값으로 바꿀겁니다. 

    arr[] = {10, 5, 2, **_10_**} 
    **item** = 3 
    
 **index '0'** 으로 시작하는 회전 정지 사이클을 반복 
item = 3 을 넣을 위치를 찾기
지금 arr[1]의 요소와 item을 swap한다.

    
    arr[] = {10, **_3_**, 2, **_10_**} 
    **item** = 5

index '0' 과 item = 5로 시작하는 회전 정지 사이클을 반복
arr[2]의 요소와 item을 swap한다.
    
    arr[] = {10, **_3_**, **_5_**, **_10_** } 
    **item** = 2
    
index '0' 과 item = 2로 시작하는 회전 정지 사이클을 반복
    
    arr[] = {**_2_**, **_3_**, ** _5_**, **_10_**}  
    
위는 cycle_stat = 0 에 대한 1회 반복입니다.
cycle_start = 1, 2, ..n-2에 대해 위 단계를 반복하세요.

# 코드


    def cycleSort(array): 
    writes = 0
    	
    
    for cycleStart in range(0, len(array) - 1): 
    	item = array[cycleStart] 
    	
    	# item을 넣을곳을 찾으세요. 
    	pos = cycleStart 
    	for i in range(cycleStart + 1, len(array)): 
    	if array[i] < item: 
    		pos += 1
    	
    	# 만약 item이 이미 그곳에 있다면, 이건 사이클이 아닙니다. 
    	if pos == cycleStart: 
    	continue
    	
    	# 그렇지 않으면, item을 해당 위치나 복제된 항목 바로 뒤에 넣으세요. 
    	while item == array[pos]: 
    	pos += 1
    	array[pos], item = item, array[pos] 
    	writes += 1
    	
    	# 사이클의 나머지 부분 회전 
    	while pos != cycleStart: 
    		
    	# item을 넣을곳을 찾으세요.
    	pos = cycleStart 
    	for i in range(cycleStart + 1, len(array)): 
    		if array[i] < item: 
    		pos += 1
    		
    	# item을 해당 위치나 복제된 항목 바로 뒤에 넣으세요. 
    	while item == array[pos]: 
    		pos += 1
    	array[pos], item = item, array[pos] 
    	writes += 1
    	
    return writes 
    	
    # driver 코드 
    arr = [1, 8, 3, 9, 10, 10, 2, 4 ] 
    n = len(arr) 
    cycleSort(arr) 
    
    print("정렬 후 : ") 
    for i in range(0, n) : 
    	print(arr[i], end = ' ') 

## 참조

 1. https://en.wikipedia.org/wiki/Cycle_sort
 2.  https://www.geeksforgeeks.org/cycle-sort/

