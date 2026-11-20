"""依原順序分批，至多 days 天送完的最小每日容量。"""
import sys


def minimum_capacity(weights, days):
    if days <= 0 or any(weight <= 0 for weight in weights):
        raise ValueError('days and weights must be positive')
    if not weights: return 0
    low, high = max(weights), sum(weights)
    while low < high:
        capacity = (low + high) // 2
        used, current = 1, 0
        for weight in weights:
            if current + weight > capacity:
                used += 1; current = 0
            current += weight
        if used <= days: high = capacity
        else: low = capacity + 1
    return low


if __name__ == '__main__':
    n, days = map(int, input().split())
    weights = list(map(int, sys.stdin.read().split()))
    if len(weights) != n: raise ValueError('weight count mismatch')
    print(minimum_capacity(weights, days))
