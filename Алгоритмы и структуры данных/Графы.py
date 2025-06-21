graph = {
    'A': {'C': 4, 'D': 7, 'F': 5},
    'B': {'B': 1, 'C': 5},
    'C': {'E': 3},
    'D': {'G': 1},
    'E': {'C': 3},
    'F': {'D': 3, 'G': 2},
    'G': {},
    'H': {}
}


"""Матрица смежности. Сопоставляем вершины с вершинами, храним веса рёбер."""
  #  A  B  C  D  E  F  G  H
[
    [0, 0, 4, 7, 0, 5, 0, 0], # A
    [0, 1, 5, 0, 0, 0, 0, 0], # B
    [0, 0, 0, 0, 3, 0, 0, 0], # C
    [0, 0, 0, 0, 0, 0, 1, 0], # D
    [0, 0, 3, 0, 0, 0, 0, 0], # E
    [0, 0, 0, 3, 0, 0, 2, 0], # F
    [0, 0, 0, 0, 0, 0, 0, 0], # G
    [0, 0, 0, 0, 0, 0, 0, 0]  # H
]


"""Матрица инцидентности. Сопоставляем вершины с рёбрами. 1 - ребро вышло, -1 - ребро пришло, 2 само в себя"""
# веса ребер
    [4,  7,  5,  1,  5,  3,  1,  3,  3,  2]

  #  e1  e2  e3  e4  e5  e6  e7  e8  e9  e10
[
    [ 1,  1,  1,  0,  0,  0,  0,  0,  0,  0], # A
    [ 0,  0,  0,  2,  1,  0,  0,  0,  0,  0], # B
    [-1,  0,  0,  0, -1,  1,  0, -1,  0,  0], # C
    [ 0, -1,  0,  0,  0,  0,  1,  0, -1,  0], # D
    [ 0,  0,  0,  0,  0, -1,  0,  1,  0,  0], # E
    [ 0,  0, -1,  0,  0,  0,  0,  0,  1,  1], # F
    [ 0,  0,  0,  0,  0,  0, -1,  0,  0, -1], # G
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0], # H
]


from collections import deque
import heapq

"""Обход графа в ширину"""
def breadth_first(graph: dict[str, dict[str, int]], start_vertex: str, search: str) -> dict[str, str]:
    previous: dict[str, str] = {}
    visited: set[str] = set()
    queue: deque[str] = deque()
    queue.append(start_vertex)
    visited.add(start_vertex)
    while len(queue) > 0:
        vertex = queue.popleft()
        if vertex == search:
            break
        outgoing = graph.get(vertex, {})
        for vertex_to in outgoing:
            if vertex_to not in visited:
                visited.add(vertex_to)
                queue.append(vertex_to)
                previous[vertex_to] = vertex

    return previous


if __name__ == '__main__':
    graph = {
        'A': {'C': 4, 'D': 7, 'F': 5},
        'B': {'B': 1, 'C': 5},
        'C': {'E': 3},
        'D': {'G': 1},
        'E': {'C': 3},
        'F': {'D': 3, 'G': 2},
    }

    start = 'A'
    search = 'E'
    links = breadth_first(graph, start, search)
    if search not in links:
        print("Нет пути")
    else:
        path = [search]
        v = search
        while v != start:
            v = links[v]
            path.append(v)
        path.reverse()
    print(path)



"""Алгоритм Дейкстры"""
def dijkstra(graph: dict[str, dict[str, int]], start_vertex: str):
    distance: dict[str, float] = dict((v, float('inf')) for v in graph)
    distance[start_vertex] = 0

    previous: dict[str, str] = dict((v, None) for v in graph)

    visited: set[str] = set()

    priority_queue: list[(int, str)] = []
    heapq.heappush(priority_queue, (0, start_vertex))
    while len(priority_queue) > 0:
        dist, vertex_from = heapq.heappop(priority_queue)
        visited.add(vertex_from)
        outgoing = graph.get(vertex_from, {})
        for (vertex_to, weight) in outgoing.items():
            if vertex_to in visited:
                continue
            cur_dist = dist + weight
            if cur_dist < distance[vertex_to]:
                distance[vertex_to] = cur_dist
                previous[vertex_to] = vertex_from
                heapq.heappush(priority_queue, (distance[vertex_to], vertex_to))
    print(distance)
    print(previous)
