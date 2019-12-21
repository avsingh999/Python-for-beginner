class Graph:
    def __init__(self):
        # 해당 정점 객체에 매핑되는 키가 포함 된 dictionary
        self.vertices = {}

    def add_vertex(self, key):
        """주어진 키를 가진 꼭지점을 그래프에 추가."""
        vertex = Vertex(key)
        self.vertices[key] = vertex

    def get_vertex(self, key):
        """해당 키로 정점 객체를 반환합니다."""
        return self.vertices[key]

    def __contains__(self, key):
        return key in self.vertices

    def add_edge(self, src_key, dest_key, weight=1):
        """주어진 무게로 src_key에서 dest_key로 가장자리를 추가하십시오."""
        self.vertices[src_key].add_neighbour(self.vertices[dest_key], weight)

    def does_edge_exist(self, src_key, dest_key):
        """src_key에서 dest_key까지의 가장자리가 있으면 True를 반환합니다."""
        return self.vertices[src_key].does_it_point_to(self.vertices[dest_key])

    def display(self):
        print('Vertices: ', end='')
        for v in self:
            print(v.get_key(), end=' ')
        print()

        print('Edges: ')
        for v in self:
            for dest in v.get_neighbours():
                w = v.get_weight(dest)
                print('(src={}, dest={}, weight={}) '.format(v.get_key(),
                                                             dest.get_key(), w))

    def __len__(self):
        return len(self.vertices)

    def __iter__(self):
        return iter(self.vertices.values())


class Vertex:
    def __init__(self, key):
        self.key = key
        self.points_to = {}

    def get_key(self):
        """이 꼭짓점 객체에 해당하는 리턴 키."""
        return self.key

    def add_neighbour(self, dest, weight):
        """이 꼭지점을 지정된 모서리 가중치로 대상으로 지정하십시오."""
        self.points_to[dest] = weight

    def get_neighbours(self):
        """이 정점이 가리키는 모든 정점을 반환합니다. """
        return self.points_to.keys()

    def get_weight(self, dest):
        """이 정점에서 목적지까지의 가장자리 가중치를 얻습니다."""
        return self.points_to[dest]

    def does_it_point_to(self, dest):
        """이 정점이 dest를 가리키면 True를 반환합니다"""
        return dest in self.points_to


def mst_prim(g):
    """연결된 그래프g의 최소 비용 범위 트리를 반환합니다."""
    mst = Graph()  # MST를 보유 할 새로운 Graph 객체 생성

    # 그래프가 비어있는 경우
    if not g:
        return mst

    nearest_neighbour = {}
    smallest_distance = {}
    unvisited = set(g)

    u = next(iter(g))  # g에서 하나의 꼭짓점을 선택하십시오
    mst.add_vertex(u.get_key())  # MST에 사본을 추가하십시오
    unvisited.remove(u)

    for n in u.get_neighbours():
        if n is u:
            continue
        nearest_neighbour[n] = mst.get_vertex(u.get_key())
        smallest_distance[n] = u.get_weight(n)

    while (smallest_distance):
        outside_mst = min(smallest_distance, key=smallest_distance.get)
        # MST 내부에서 가장 가까운 이웃을 얻는다
        inside_mst = nearest_neighbour[outside_mst]
        mst.add_vertex(outside_mst.get_key())
        mst.add_edge(outside_mst.get_key(), inside_mst.get_key(),
                     smallest_distance[outside_mst])
        mst.add_edge(inside_mst.get_key(), outside_mst.get_key(),
                     smallest_distance[outside_mst])
        unvisited.remove(outside_mst)
        del smallest_distance[outside_mst]
        del nearest_neighbour[outside_mst]
        for n in outside_mst.get_neighbours():
            if n in unvisited:
                if n not in smallest_distance:
                    smallest_distance[n] = outside_mst.get_weight(n)
                    nearest_neighbour[n] = mst.get_vertex(outside_mst.get_key())
                else:
                    if smallest_distance[n] > outside_mst.get_weight(n):
                        smallest_distance[n] = outside_mst.get_weight(n)
                        nearest_neighbour[n] = mst.get_vertex(outside_mst.get_key())

    return mst


g = Graph()
print('Undirected Graph')
print('Menu')
print('add vertex <key>')
print('add edge <src> <dest> <weight>')
print('mst')
print('display')
print('quit')

while True:
    do = input('What would you like to do? ').split()

    operation = do[0]
    if operation == 'add':
        suboperation = do[1]
        if suboperation == 'vertex':
            key = int(do[2])
            if key not in g:
                g.add_vertex(key)
            else:
                print('Vertex already exists.')
        elif suboperation == 'edge':
            src = int(do[2])
            dest = int(do[3])
            weight = int(do[4])
            if src not in g:
                print('Vertex {} does not exist.'.format(src))
            elif dest not in g:
                print('Vertex {} does not exist.'.format(dest))
            else:
                if not g.does_edge_exist(src, dest):
                    g.add_edge(src, dest, weight)
                    g.add_edge(dest, src, weight)
                else:
                    print('Edge already exists.')

    elif operation == 'mst':
        mst = mst_prim(g)
        print('Minimum Spanning Tree:')
        mst.display()
        print()

    elif operation == 'display':
        g.display()
        print()

    elif operation == 'quit':
        break
