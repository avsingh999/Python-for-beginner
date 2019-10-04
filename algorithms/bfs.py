from queue import Queue

def bfs(node):
    q = Queue()
    q.put(node)
    visited = [False for i in range(v+1)]

    while not q.empty():
        next_node = q.get() # remove the next and return it
        visited[next_node] = True
        
        for u in adj[next_node]:
            if not visited[u]:
                q.put(u)

v, e, init = map(int, input().split()) # nodes, edges, bfs initial node

adj = [[] for i in range(v+1)] # adjacency list

for i in range(e):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

bfs(init)
