def solve(graph, start):
    import heapq
    distance = {start: 0}
    queue = [(0, start)]
    while queue:
        cost, node = heapq.heappop(queue)
        if cost != distance[node]: continue
        for neighbor, weight in graph.get(node, []):
            candidate = cost + weight
            if neighbor not in distance or candidate < distance[neighbor]:
                distance[neighbor] = candidate; heapq.heappush(queue, (candidate, neighbor))
    return distance

if __name__ == "__main__":
    print("Exercise: 30_dijkstra")
