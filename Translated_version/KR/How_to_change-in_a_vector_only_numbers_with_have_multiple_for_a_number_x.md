# 숫자 x에 대해 배수가 여러개인 벡터만 변경하는 방법

#방법
벡터(목록)의 요소 X가 다른 숫자 Y로 나눌 수 있는지 확인하는 함수를 만들어야합니다.
```
def change_multiple(change_to,multiple,vector):
    for i in range(len(vector)): # scroll through the list
        if vector[i]%multiple == 0: #check if the mod of element vector[position] with  multiple  is 0 or not
            vector[i] = change_to # if 0 is multiple, change the number
        
```
 
 *테스트의 한 예*
```
vector = [4,5,6,7,9,10]
multiple = 2
change_to = 999

print(vector) # >> [4,5,6,7,9,10]

change_multiple(change_to,multiple,vector)

print(vector) # >> [999,5,999,7,9,999]
```
