def solve(graph, start):
    from collections import deque
    visited = {start}
    queue = deque([start])
    order = []
    while queue:
        node = queue.popleft(); order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor); queue.append(neighbor)
    return order

if __name__ == "__main__":
    print("Exercise: 25_graph_bfs")
