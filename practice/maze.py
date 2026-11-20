"""S 到 G 的四方向最短步數，# 是牆；無路可走回傳 -1。"""
from collections import deque
import sys


def shortest_route(rows):
    if not rows or not rows[0] or any(len(row) != len(rows[0]) for row in rows):
        raise ValueError('rectangular non-empty grid required')
    starts, goals = [], []
    for r, row in enumerate(rows):
        for c, cell in enumerate(row):
            if cell not in '.#SG':
                raise ValueError('unknown grid character')
            if cell == 'S': starts.append((r, c))
            if cell == 'G': goals.append((r, c))
    if len(starts) != 1 or len(goals) != 1:
        raise ValueError('exactly one S and one G required')
    queue, seen = deque([(starts[0], 0)]), {starts[0]}
    while queue:
        (r, c), distance = queue.popleft()
        if (r, c) == goals[0]: return distance
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < len(rows) and 0 <= nc < len(rows[0]) and rows[nr][nc] != '#' and (nr, nc) not in seen:
                seen.add((nr, nc)); queue.append(((nr, nc), distance + 1))
    return -1


if __name__ == '__main__':
    height, width = map(int, input().split())
    rows = [input().strip() for _ in range(height)]
    if any(len(row) != width for row in rows): raise ValueError('width mismatch')
    print(shortest_route(rows))
