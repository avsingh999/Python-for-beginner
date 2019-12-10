# 주어진 그래프에서 DFS순회를 출력하는 파이썬3 프로그램 
from collections import defaultdict 

# 이 클래스는 인접list 표현을 사용하여 방향 그래프를 나타냅니다.
class Graph: 

	# 생성자
	def __init__(self): 

		# 그래프를 저장하기위한 기본 dictionary 
		self.graph = defaultdict(list) 

	# 그래프에 edge를 추가하기위한 함수function to add an edge to graph 
	def addEdge(self, u, v): 
		self.graph[u].append(v) 

	# DFS에서 사용하는 함수 
	def DFSUtil(self, v, visited): 

		# 현재 노드를 방문한것으로 표시하고 출력하기 위해 표시 
		visited[v] = True
		print(v, end = ' ') 

		# 이 정점에 인접한 모든 정점에 대해 반복
		for i in self.graph[v]: 
			if visited[i] == False: 
				self.DFSUtil(i, visited) 

	# DFS순회를 수행하는 함수. 
	# 재귀 DFSUtil()을 사용합니다. 
	def DFS(self, v): 

		# 모든 정점을 방문하지 않은 것으로 표시
		visited = [False] * (len(self.graph)) 

		# DFS순회를 출력하기 위해 재귀 도우미 함수를 호출하세요. 
		self.DFSUtil(v, visited) 

# Driver 코드

# 위의 다이어그램에서 주어진 그래프를 생성
g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3) 

print("이하는 (정점 2 에서 시작)의 DFS입니다.") 
g.DFS(3) 
