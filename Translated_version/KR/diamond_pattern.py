# 다이아몬드 패턴을 출력하기위한 파이썬 프로그램. 

def Diamond(rows): 
    n = 0
    for i in range(1, rows + 1): 
        # 빈 공간들 출력을 위한 루프
        for j in range (1, (rows - i) + 1): 
            print(end = " ") 
          
        # 별 출력을 위한 루프
        while n != (2 * i - 1): 
            print("*", end = "") 
            n = n + 1
        n = 0
          
        # 줄바꿈
        print()  
  
    k = 1
    n = 1
    for i in range(1, rows): 
        # 빈 공간들 출력을 위한 루프
        for j in range (1, k + 1): 
            print(end = " ") 
        k = k + 1
          
        # 별 출력을 위한 루프
        while n <= (2 * (rows - i) - 1): 
            print("*", end = "") 
            n = n + 1
        n = 1
        print() 
  
# 마지막으로 몇열의 다이아몬드를 지정하고 싶은가요?
rows = 5
Diamond(rows) 
