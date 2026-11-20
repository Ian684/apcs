def solve(edges, nodes):
    parent = list(range(nodes))
    def find(value):
        if parent[value] != value: parent[value] = find(parent[value])
        return parent[value]
    total = 0
    for weight, left, right in sorted(edges):
        left_root, right_root = find(left), find(right)
        if left_root != right_root:
            parent[right_root] = left_root; total += weight
    return total

if __name__ == "__main__":
    print("Exercise: 32_minimum_spanning")
