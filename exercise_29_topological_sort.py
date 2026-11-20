def solve(nodes, edges):
    indegree = {node: 0 for node in nodes}
    graph = {node: [] for node in nodes}
    for left, right in edges:
        graph[left].append(right); indegree[right] += 1
    from collections import deque
    queue = deque(node for node in nodes if indegree[node] == 0)
    order = []
    while queue:
        node = queue.popleft(); order.append(node)
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0: queue.append(neighbor)
    return order

if __name__ == "__main__":
    print("Exercise: 29_topological_sort")
