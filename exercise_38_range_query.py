def solve(values):
    size = 1
    while size < len(values): size *= 2
    tree = [0] * (2 * size)
    tree[size:size + len(values)] = values
    for i in range(size - 1, 0, -1): tree[i] = tree[2*i] + tree[2*i+1]
    def query(left, right):
        left += size; right += size
        total = 0
        while left < right:
            if left & 1: total += tree[left]; left += 1
            if right & 1: right -= 1; total += tree[right]
            left //= 2; right //= 2
        return total
    return query

if __name__ == "__main__":
    print("Exercise: 38_range_query")
