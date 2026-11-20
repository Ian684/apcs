def solve(pairs, values):
    parent = list(range(values))
    def find(node):
        while parent[node] != node:
            parent[node] = parent[parent[node]]; node = parent[node]
        return node
    for left, right in pairs:
        left_root, right_root = find(left), find(right)
        if left_root != right_root: parent[right_root] = left_root
    return [find(value) for value in range(values)]

if __name__ == "__main__":
    print("Exercise: 28_union_find")
