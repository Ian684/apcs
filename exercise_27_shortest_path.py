def solve(graph, start):
    from collections import deque
    distance = {start: 0}
    queue = deque([start])
    while queue:
        node = queue.popleft()
        for neighbor, weight in graph.get(node, []):
            candidate = distance[node] + weight
            if neighbor not in distance or candidate < distance[neighbor]:
                distance[neighbor] = candidate; queue.append(neighbor)
    return distance

if __name__ == "__main__":
    print("Exercise: 27_shortest_path")
