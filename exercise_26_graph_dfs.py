def solve(graph, start):
    visited = set()
    order = []
    def visit(node):
        if node in visited: return
        visited.add(node); order.append(node)
        for neighbor in graph.get(node, []): visit(neighbor)
    visit(start)
    return order

if __name__ == "__main__":
    print("Exercise: 26_graph_dfs")
