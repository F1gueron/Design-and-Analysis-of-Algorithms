import heapq
from collections import defaultdict, deque

def dijkstra(graph, start, n):
    distances = {i: float('inf') for i in range(n)}
    distances[start] = 0
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

def minimum_distances(n, m, activities, connections):
    graph = defaultdict(list)
    for u, v, w in connections:
        graph[u].append((v, w))
        graph[v].append((u, w))
    
    activity_locations = defaultdict(list)
    for i, activity in enumerate(activities):
        activity_locations[activity].append(i)
    activity_locations = dict(sorted(activity_locations.items()))
    
    result = []
    for activity, locations in activity_locations.items():
        min_distance = float('inf')
        for location in locations:
            distances = dijkstra(graph, location, n)
            for other_location in locations:
                if location != other_location:
                    min_distance = min(min_distance, distances[other_location])
        result.append(min_distance)
    
    return result

if __name__ == "__main__":
    n, m = map(int, input().split())
    activities = list(map(int, input().split()))
    connections = [tuple(map(int, input().split())) for _ in range(m)]
    
    result = minimum_distances(n, m, activities, connections)
    print(" ".join(map(str, result)))