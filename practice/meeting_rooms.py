"""最少教室數：活動區間 [start,end)，同一時刻結束的教室可以立刻再用。"""
import heapq
import sys


def minimum_rooms(intervals):
    if any(start >= end for start, end in intervals):
        raise ValueError('each meeting must have positive duration')
    ends, peak = [], 0
    for start, end in sorted(intervals):
        while ends and ends[0] <= start:
            heapq.heappop(ends)
        heapq.heappush(ends, end)
        peak = max(peak, len(ends))
    return peak


if __name__ == '__main__':
    count = int(input())
    print(minimum_rooms([tuple(map(int, input().split())) for _ in range(count)]))
