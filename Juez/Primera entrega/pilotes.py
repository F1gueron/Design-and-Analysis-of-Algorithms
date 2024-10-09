from collections import  deque

def bfsAux(graph, visited, vertex):
    to_visit = deque([vertex])
    visited[vertex] = True

    while to_visit:
        current_vertex = to_visit.popleft()

        for adjacent in graph[current_vertex]:
            if not visited[adjacent]:
                to_visit.append(adjacent)
                visited[adjacent] = True

def bfs(graph):
    num_vertices = len(graph)
    visited = [False] * num_vertices
    num_connected_components = 0

    for vertex in range(num_vertices):
        if not visited[vertex]:
            bfsAux(graph, visited, vertex)
            num_connected_components += 1

    return num_connected_components

if __name__ == '__main__':
    n, m = map(int, input().strip().split())
    graph = [[] for _ in range(n)]

    for _ in range(m):
        a, b = map(int, input().strip().split())
        graph[a].append(b)
        graph[b].append(a)

    num_connected_components = bfs(graph)
    print(num_connected_components)
