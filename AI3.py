import heapq
def prim(graph):
    n = len(graph)
    visited = set()
    start_vertex = 0
    mst = []
    heap = [(0, start_vertex)]
    while heap:
        (weight, vertex) = heapq.heappop(heap)
        if vertex not in visited:
            visited.add(vertex)
            mst.append((weight, vertex))
            for neighbor, neighbor_weight in graph[vertex]:
                if neighbor not in visited:
                    heapq.heappush(heap, (neighbor_weight, neighbor))
    return mst
graph = [[(1, 5), (2, 1), (3, 4)],
 [(0, 5), (2, 2)],
 [(0, 1), (1, 2), (3, 3)],
 [(0, 4), (2, 3)]
]
mst = prim(graph)
print(mst)
"""
Output:-
PS F:\SAOE\A_SEM6\AI> python .\Prims.py
[(0, 0), (1, 2), (2, 1), (3, 3)]
PS F:\SAOE\A_SEM6\AI>
"""