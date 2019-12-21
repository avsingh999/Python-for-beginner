# 이중 linked list의 병합 정렬 프로그램

# 이중 linked list의 노드 
class Node: 
	
	# 새로운 노드를 생성하는 생성자
	def __init__(self, data): 
		self.data = data 
		self.next = None
		self.prev = None

class DoublyLinkedList: 

	# 빈 이중 linked list 생성자
	def __init__(self): 
		self.head = None

	# 2 개의 linked리스트를 병합하는 기능 
	def merge(self, first, second): 
		
		# 첫 번째 linked list가 비어있는 경우
		if first is None: 
			return second 
		
		# 두 번째 linked list가 비어있는 경우
		if second is None: 
			return first 

		# 더 작은 값을 고르세요.
		if first.data < second.data: 
			first.next = self.merge(first.next, second) 
			first.next.prev = first 
			first.prev = None
			return first 
		else: 
			second.next = self.merge(first, second.next) 
			second.next.prev = second 
			second.prev = None
			return second 

	# 병합정렬을 하는 함수
	def mergeSort(self, tempHead): 
		if tempHead is None: 
			return tempHead 
		if tempHead.next is None: 
			return tempHead 
		
		second = self.split(tempHead) 
		
		# 좌우 반복 
		tempHead = self.mergeSort(tempHead) 
		second = self.mergeSort(second) 

		# 정렬 된 반쪽을 병합
		return self.merge(tempHead, second) 

	# 이중 linked list (DLL)을 절반 크기의 두 DLL로 분할
	def split(self, tempHead): 
		fast = slow = tempHead 
		while(True): 
			if fast.next is None: 
				break
			if fast.next.next is None: 
				break
			fast = fast.next.next
			slow = slow.next
			
		temp = slow.next
		slow.next = None
		return temp 
		
			
	# list의 헤드와 정수에 대한 참조가 주어지면,list의 앞에 새로운 노드를 삽입합니다
	def push(self, new_data): 

		# 1. 노드 할당 
		# 2. 데이터를 그 안에 넣기
		new_node = Node(new_data) 

		# 3. 새 노드 다음을 헤드로, 이전 노드를 없음 (이미 None)으로 만듭니다.
		new_node.next = self.head 

		# 4. 헤드 노드의 prev를 new_node로 변경
		if self.head is not None: 
			self.head.prev = new_node 

		# 5. 새 노드를 가리 키도록 헤드를 이동
		self.head = new_node 


	def printList(self, node): 
		temp = node 
		print("다음 포인터를 사용하여 순회 순회")
		while(node is not None): 
			print (node.data, end=" ") 
			temp = node 
			node = node.next
		print ("\n이전 포인터를 사용한 역방향 순회")
		while(temp): 
			print (temp.data, end=" ")
			temp = temp.prev

# 위 기능을 테스트하는 드라이버 프로그램
dll = DoublyLinkedList() 
dll.push(5) 
dll.push(20); 
dll.push(4); 
dll.push(3); 
dll.push(30) 
dll.push(10); 
dll.head = dll.mergeSort(dll.head) 
print ("Linked List after sorting")
dll.printList(dll.head) 
