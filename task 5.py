# Question: Given the graph below with edge costs, find the minimum-cost path from A to P.

import heapq

graph = {
    'A': [('B', 3), ('C', 2)],
    'B': [('D', 4), ('E', 6)],
    'C': [('F', 5), ('G', 1)],
    'D': [('H', 2)],
    'E': [],
    'F': [],
    'G': [('P', 3)],
    'H': [],
    'P': []
}

start = 'A'
goal = 'P'

pq = [(0, [start])]
best_cost = {}

while pq:
    cost, path = heapq.heappop(pq)
    node = path[-1]

    if node in best_cost and best_cost[node] <= cost:
        continue
    best_cost[node] = cost

    if node == goal:
        print("Optimal path:", " -> ".join(path), "| Cost:", cost)
        break

    for nxt, edge_cost in graph[node]:
        heapq.heappush(pq, (cost + edge_cost, path + [nxt]))
else:
    print("Path not found")

# Time Complexity: O(E log V) due to heap-based exploration of edges.
# Space Complexity: O(V) for storing paths in the priority queue and best_cost map.

