print ("한계를 입력하세요.")
rows = int(input())

#위 반절
k = 0
for i in range(1, rows + 1): 
    # 빈 공간들 출력 
    for j in range (1, (rows - i) + 1): 
        print(end = " ") 
	  
        # 별들을 출력해보자.
    while k != (2 * i - 1):
        print("*", end = "")
        k = k + 1
    k = 0
	  
    # 줄바꿈 추가 
    print()  

#아래 반절
k = 2
m = 1
for i in range(1, rows): 
    # 빈 공간들 출력
    for j in range (1, k):
        print(end = " ") 
    k = k + 1
	  
    # 별 출력 
    while m <= (2 * (rows - i) - 1): 
        print("*", end = "") 
        m = m + 1
    m = 1
	
    #줄바꿈 추가
    print() 
