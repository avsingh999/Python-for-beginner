
# find minimum cut for an undirected graph with duplicate edges but no self loops

import pprint, random, copy, time

def main():
    start = time.time()

    graph = get_graph()
    n = 100
    min_cut = repeatKrager(n, graph)

    print(min_cut)

    print(f"--------------------{time.time()-start}------------")

def get_graph():
	# change the below file location with your actual file location to find the minimum number of cuts
	
	text = open(r"E:\Summer 2019\Algorithms\Krager's min cut\kargerMinCut.txt")
    content = text.read().splitlines()
    graph = {}

    for line in content:
        line = [int(i) for i in line.split()]
        graph[line[0]] = line[1:]
        
    text.close()

    return graph


def krager(graph):
    while len(graph) > 2:
        v1, v2 = get_2_random_vertex(graph)
        mergeVertex(graph, v1, v2)
        removeSelfLoops(graph, v1)

    return len(graph[v1])


# merge vertex v1 and v2 and removes v2
def mergeVertex(graph, v1, v2):
    graph[v1].extend(graph[v2])

    # replacing all mention of v2 with v1
    for item in graph[v2]:
        while True:
            try:
                graph[item].remove(v2)
                graph[item].append(v1)
            except:
                break

    del graph[v2]


def removeSelfLoops(graph, v1):
    while True:
        try:
            graph[v1].remove(v1)
        except:
            break


def get_2_random_vertex(graph):
    vertex1 = random.choice(list(graph.keys()))
    vertex2 = random.choice(graph[vertex1])

    return vertex1, vertex2


def repeatKrager(n, graph):
    i = 0

    # change value of mincut if this returns the initial value of min_cut

    min_cut = 1000000
    while i < n:
        graphCopy = copy.deepcopy(graph)
        cut = krager(graphCopy)
        i += 1

        if cut < min_cut:
            min_cut = cut

    return min_cut

if __name__ == "__main__":

    main()
