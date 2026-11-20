def solve(matrix):
    distance = [row[:] for row in matrix]
    for middle in range(len(distance)):
        for left in range(len(distance)):
            for right in range(len(distance)):
                distance[left][right] = min(distance[left][right], distance[left][middle] + distance[middle][right])
    return distance

if __name__ == "__main__":
    print("Exercise: 31_floyd_warshall")
