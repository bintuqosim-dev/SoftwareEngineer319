import heapq

def dijkstra(graph, start):
 
    distances = {node: float('infinity') for node in graph}
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

graph = {
    'A': [('B', 4), ('C', 1)],
    'B': [('A', 4), ('D', 2), ('E', 5)],
    'C': [('A', 1), ('E', 3)],
    'D': [('B', 2), ('E', 3)],
    'E': [('B', 5), ('C', 3), ('D', 3)]
}
