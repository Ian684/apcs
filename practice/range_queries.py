"""多筆區間查詢：輸入 n q、n 個整數、q 組 1-based 閉區間。"""
import sys


def solve(text):
    numbers = list(map(int, text.split()))
    if len(numbers) < 2:
        raise ValueError('missing n and q')
    n, q = numbers[:2]
    if n < 0 or q < 0 or len(numbers) != 2 + n + 2 * q:
        raise ValueError('input length does not match n and q')
    prefix = [0]
    for value in numbers[2:2 + n]:
        prefix.append(prefix[-1] + value)
    answers = []
    for i in range(2 + n, len(numbers), 2):
        left, right = numbers[i:i + 2]
        if not 1 <= left <= right <= n:
            raise ValueError('invalid interval')
        answers.append(str(prefix[right] - prefix[left - 1]))
    return '\n'.join(answers)


if __name__ == '__main__':
    print(solve(sys.stdin.read()))
