import collections
import heapq
import itertools
import math

def digit_sum(n):
    """整數各十進位位數的和；O(log |n|)。"""
    return sum((int(c) for c in str(abs(n))))

def digital_root(n):
    """反覆加總到個位數，接受非負整數。"""
    if n < 0:
        raise ValueError('non-negative integer required')
    while n >= 10:
        n = sum(map(int, str(n)))
    return n

def reverse_integer(n):
    """反轉十進位數字，結果不保留前導零。"""
    return (-1 if n < 0 else 1) * int(str(abs(n))[::-1])

def base_digits(n, base):
    """非負整數轉 2..36 進位。"""
    if n < 0 or not 2 <= base <= 36:
        raise ValueError('invalid number or base')
    alphabet = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = []
    while n:
        n, r = divmod(n, base)
        result.append(alphabet[r])
    return ''.join(reversed(result)) or '0'

def leap_year(year):
    """西曆閏年：4 整除，百年需再被 400 整除。"""
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

def add_minutes(hour, minute, delta):
    """合法 24 小時時間加上分鐘，delta 可負。"""
    if not 0 <= hour < 24 or not 0 <= minute < 60:
        raise ValueError('invalid clock')
    return list(divmod((hour * 60 + minute + delta) % 1440, 60))

def clock_angle(hour, minute):
    """回傳兩針較小夾角；0<=minute<60。"""
    if not 0 <= minute < 60:
        raise ValueError('invalid minute')
    difference = abs(hour % 12 * 30 + minute * 0.5 - minute * 6)
    return min(difference, 360 - difference)

def grade_histogram(scores):
    """統計 0-9,...,90-99,100 共 11 級。"""
    if any((not 0 <= s <= 100 for s in scores)):
        raise ValueError('score outside 0..100')
    bins = [0] * 11
    for score in scores:
        bins[score // 10] += 1
    return bins

def weighted_fraction(values, weights):
    """相同長度整數列表，權重非負且總重>0，回傳約分分數。"""
    if len(values) != len(weights) or any((w < 0 for w in weights)) or sum(weights) == 0:
        raise ValueError('invalid weights')
    numerator = sum((v * w for v, w in zip(values, weights)))
    denominator = sum(weights)
    divisor = math.gcd(numerator, denominator)
    return [numerator // divisor, denominator // divisor]

def rotate_matrix(matrix):
    """矩形矩陣順時針 90 度；空矩陣回傳 []。"""
    if not matrix:
        return []
    if any((len(row) != len(matrix[0]) for row in matrix)):
        raise ValueError('ragged matrix')
    return [list(row) for row in zip(*matrix[::-1])]

def transpose_matrix(matrix):
    """矩形轉置，輸入不變。"""
    if not matrix:
        return []
    if any((len(row) != len(matrix[0]) for row in matrix)):
        raise ValueError('ragged matrix')
    return [list(row) for row in zip(*matrix)]

def spiral_order(matrix):
    """矩形矩陣由外向內讀取，O(hw)。"""
    if not matrix:
        return []
    if any((len(row) != len(matrix[0]) for row in matrix)):
        raise ValueError('ragged matrix')
    top, left, bottom, right = (0, 0, len(matrix), len(matrix[0]))
    result = []
    while top < bottom and left < right:
        result.extend(matrix[top][left:right])
        top += 1
        result.extend((matrix[r][right - 1] for r in range(top, bottom)))
        right -= 1
        if top < bottom:
            result.extend(reversed(matrix[bottom - 1][left:right]))
            bottom -= 1
        if left < right:
            result.extend((matrix[r][left] for r in range(bottom - 1, top - 1, -1)))
            left += 1
    return result

def mine_counts(rows):
    """等長字串由 . 與 * 組成，回傳提示字串。"""
    h = len(rows)
    w = len(rows[0]) if rows else 0
    if any((len(row) != w for row in rows)):
        raise ValueError('ragged grid')
    return [''.join(('*' if rows[r][c] == '*' else str(sum((0 <= r + dr < h and 0 <= c + dc < w and (rows[r + dr][c + dc] == '*') for dr in (-1, 0, 1) for dc in (-1, 0, 1) if dr or dc))) for c in range(w))) for r in range(h)]

def island_count(rows):
    """0/1 字串地圖，1 是陸地；O(hw)。"""
    if not rows:
        return 0
    h, w = (len(rows), len(rows[0]))
    if any((len(row) != w for row in rows)):
        raise ValueError('ragged grid')
    seen = set()
    islands = 0
    for r in range(h):
        for c in range(w):
            if rows[r][c] != '1' or (r, c) in seen:
                continue
            islands += 1
            stack = [(r, c)]
            seen.add((r, c))
            while stack:
                a, b = stack.pop()
                for x, y in ((a + 1, b), (a - 1, b), (a, b + 1), (a, b - 1)):
                    if 0 <= x < h and 0 <= y < w and (rows[x][y] == '1') and ((x, y) not in seen):
                        seen.add((x, y))
                        stack.append((x, y))
    return islands

def robot_position(height, width, commands):
    """從 (0,0) 出發；UDLR，超出地圖的動作忽略。"""
    if height < 1 or width < 1:
        raise ValueError('positive dimensions required')
    r = c = 0
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    for command in commands:
        dr, dc = directions[command]
        nr, nc = (r + dr, c + dc)
        if 0 <= nr < height and 0 <= nc < width:
            r, c = (nr, nc)
    return [r, c]

def checkout_time(durations, desks):
    """每位顧客選最早空閒收銀台，非負服務時間；O(n log desks)。"""
    if desks < 1 or any((t < 0 for t in durations)):
        raise ValueError('invalid input')
    ends = [0] * desks
    for duration in durations:
        heapq.heapreplace(ends, ends[0] + duration)
    return max(ends)

def josephus(n, step):
    """0-based 人員編號，回傳淘汰順序（包含最後一人）。"""
    if n < 1 or step < 1:
        raise ValueError('positive n and step required')
    people = list(range(n))
    index = 0
    order = []
    while people:
        index = (index + step - 1) % len(people)
        order.append(people.pop(index))
    return order

def stack_commands(commands):
    """每筆為 ['push',值] 或 ['pop']；空 pop 回傳 None。"""
    stack = []
    out = []
    for command in commands:
        if command[0] == 'push':
            stack.append(command[1])
        elif command == ['pop']:
            out.append(stack.pop() if stack else None)
        else:
            raise ValueError('unknown command')
    return out

def postfix_value(tokens):
    """整數 token 與 + - *，格式不完整時拋錯。"""
    stack = []
    for token in tokens:
        if token in ('+', '-', '*'):
            if len(stack) < 2:
                raise ValueError('missing operand')
            b, a = (stack.pop(), stack.pop())
            stack.append(a + b if token == '+' else a - b if token == '-' else a * b)
        else:
            stack.append(int(token))
    if len(stack) != 1:
        raise ValueError('invalid expression')
    return stack[0]

def balanced_brackets(text):
    """檢查 ()[]{}，其餘字元忽略。"""
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for char in text:
        if char in '([{':
            stack.append(char)
        elif char in pairs and (not stack or stack.pop() != pairs[char]):
            return False
    return not stack

def train_reorder(order):
    """車廂 1..n 依序進站，判斷是否能排成指定排列。"""
    n = len(order)
    if sorted(order) != list(range(1, n + 1)):
        raise ValueError('permutation required')
    stack = []
    next_car = 1
    for target in order:
        while next_car <= n and (not stack or stack[-1] != target):
            stack.append(next_car)
            next_car += 1
        if not stack or stack.pop() != target:
            return False
    return True

def run_length(text):
    """回傳 [字元,連續數量] 列表，空字串是 []。"""
    return [[char, len(list(group))] for char, group in itertools.groupby(text)]

def intersection_length(a, b):
    """合法 [start,end) 區間交集長度。"""
    if a[0] > a[1] or b[0] > b[1]:
        raise ValueError('reversed interval')
    return max(0, min(a[1], b[1]) - max(a[0], b[0]))

def covered_length(intervals):
    """半開區間總覆蓋長度，O(n log n)。"""
    total = 0
    end = None
    for left, right in sorted(intervals):
        if left > right:
            raise ValueError('reversed interval')
        if end is None or left > end:
            total += right - left
            end = right
        elif right > end:
            total += right - end
            end = right
    return total

def balanced_cut(values):
    """非空左右兩段和差最小值，至少兩個數。"""
    if len(values) < 2:
        raise ValueError('at least two values required')
    total = sum(values)
    prefix = 0
    best = math.inf
    for value in values[:-1]:
        prefix += value
        best = min(best, abs(total - 2 * prefix))
    return best

def minimum_window(values, target):
    """正整數列表中和>=target 的最短長度；無解為 0。"""
    if target <= 0 or any((v <= 0 for v in values)):
        raise ValueError('positive inputs required')
    left = total = 0
    best = len(values) + 1
    for right, value in enumerate(values):
        total += value
        while total >= target:
            best = min(best, right - left + 1)
            total -= values[left]
            left += 1
    return 0 if best > len(values) else best

def target_pairs(values, target):
    """計算 i<j 且 values[i]+values[j]=target 的對數。"""
    seen = collections.Counter()
    answer = 0
    for value in values:
        answer += seen[target - value]
        seen[value] += 1
    return answer

def triangle_path(rows):
    """每列比上一列多一格，最大由頂到底路徑和。"""
    if any((len(row) != i + 1 for i, row in enumerate(rows))):
        raise ValueError('triangle shape required')
    if not rows:
        return 0
    best = rows[-1][:]
    for row in reversed(rows[:-1]):
        best = [value + max(best[i], best[i + 1]) for i, value in enumerate(row)]
    return best[0]

def coin_combinations(coins, amount):
    """不同正面額，不限張數，計算組合數。"""
    if amount < 0 or any((c <= 0 for c in coins)) or len(set(coins)) != len(coins):
        raise ValueError('invalid coins')
    ways = [1] + [0] * amount
    for coin in coins:
        for total in range(coin, amount + 1):
            ways[total] += ways[total - coin]
    return ways[amount]

def grid_paths(rows):
    """0 可走、1 障礙的矩陣，回傳左上到右下路徑數。"""
    if not rows or not rows[0]:
        return 0
    w = len(rows[0])
    ways = [0] * w
    ways[0] = 1
    if any((len(row) != w for row in rows)):
        raise ValueError('ragged grid')
    for row in rows:
        for c, blocked in enumerate(row):
            if blocked:
                ways[c] = 0
            elif c:
                ways[c] += ways[c - 1]
    return ways[-1]

def lattice_points(a, b):
    """兩整數座標間，含端點的格點數；重合點為 1。"""
    return math.gcd(abs(a[0] - b[0]), abs(a[1] - b[1])) + 1

def rectangle_overlap(a, b):
    """矩形格式 [x1,y1,x2,y2]，端點相碰面積為 0。"""
    if a[0] > a[2] or a[1] > a[3] or b[0] > b[2] or (b[1] > b[3]):
        raise ValueError('invalid rectangle')
    return max(0, min(a[2], b[2]) - max(a[0], b[0])) * max(0, min(a[3], b[3]) - max(a[1], b[1]))

def mountain_peaks(heights):
    """不把兩端當山峰，回傳 0-based 位置。"""
    return [i for i in range(1, len(heights) - 1) if heights[i] > heights[i - 1] and heights[i] > heights[i + 1]]

def visible_buildings(heights):
    """從左側可看見的建築位置，相同高度遮住後方。"""
    highest = -math.inf
    visible = []
    for i, height in enumerate(heights):
        if height > highest:
            visible.append(i)
            highest = height
    return visible

def dense_ranks(scores):
    """高分第 1 名，相同分數同名次，保留原順序。"""
    rank = {score: i + 1 for i, score in enumerate(sorted(set(scores), reverse=True))}
    return [rank[score] for score in scores]

def sorted_intersection(a, b):
    """輸入可未排序，輸出交集中的不同值。"""
    a, b = (sorted(set(a)), sorted(set(b)))
    i = j = 0
    result = []
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            result.append(a[i])
            i += 1
            j += 1
        elif a[i] < b[j]:
            i += 1
        else:
            j += 1
    return result

def matrix_product(a, b):
    """非空矩形矩陣相乘；維度不合拋錯。"""
    if not a or not b or (not a[0]) or (not b[0]) or any((len(r) != len(a[0]) for r in a)) or any((len(r) != len(b[0]) for r in b)) or (len(a[0]) != len(b)):
        raise ValueError('incompatible matrices')
    return [[sum((a[i][k] * b[k][j] for k in range(len(b)))) for j in range(len(b[0]))] for i in range(len(a))]

def polynomial(coefficients, x):
    """係數依最高次到常數項排序，O(n)。"""
    answer = 0
    for coefficient in coefficients:
        answer = answer * x + coefficient
    return answer

def gcd_lcm(a, b):
    """整數輸入，結果非負；有 0 時 lcm=0。"""
    divisor = math.gcd(a, b)
    return [divisor, abs(a // divisor * b) if divisor else 0]

def prime_count(limit):
    """計算 <=limit 的質數數量。"""
    if limit < 2:
        return 0
    prime = [True] * (limit + 1)
    prime[0] = prime[1] = False
    for p in range(2, math.isqrt(limit) + 1):
        if prime[p]:
            for multiple in range(p * p, limit + 1, p):
                prime[multiple] = False
    return sum(prime)

def divisors(n):
    """正整數全部正因數，遞增輸出。"""
    if n < 1:
        raise ValueError('positive number required')
    result = []
    for d in range(1, math.isqrt(n) + 1):
        if n % d == 0:
            result.append(d)
            if d * d != n:
                result.append(n // d)
    return sorted(result)

def closest_pair_gap(values):
    """至少兩個整數，最小絕對差。"""
    if len(values) < 2:
        raise ValueError('two numbers required')
    ordered = sorted(values)
    return min((b - a for a, b in zip(ordered, ordered[1:])))

def max_profit(prices):
    """先買後賣最多一次，不交易的利益為 0。"""
    low = math.inf
    profit = 0
    for price in prices:
        low = min(low, price)
        profit = max(profit, price - low)
    return profit

def frequency_winner(votes):
    """字串票名列表，無票回傳 None。"""
    counts = collections.Counter(votes)
    return min(counts, key=lambda name: (-counts[name], name)) if counts else None

def parentheses_depth(text):
    """只接受 ()，不平衡時拋錯；空字串深度為 0。"""
    depth = best = 0
    for char in text:
        if char not in '()':
            raise ValueError('parentheses only')
        depth += 1 if char == '(' else -1
        if depth < 0:
            raise ValueError('unbalanced')
        best = max(best, depth)
    if depth:
        raise ValueError('unbalanced')
    return best

def minimum_swaps_binary(values):
    """任意兩位置交換，將 0 放前、1 放後的最少次數。"""
    if any((v not in (0, 1) for v in values)):
        raise ValueError('binary list required')
    zeros = values.count(0)
    return sum(values[:zeros])

def main():
    import argparse
    import json
    from pathlib import Path
    parser = argparse.ArgumentParser(description='Numbered practice exercises; arguments are a JSON array')
    parser.add_argument('exercise', nargs='?')
    parser.add_argument('arguments', nargs='?', default='[]')
    parser.add_argument('--list', action='store_true')
    args = parser.parse_args()
    catalog = json.loads((Path(__file__).resolve().parents[1] / 'curriculum.json').read_text(encoding='utf-8'))
    if args.list:
        for item in catalog:
            print(str(item['id']) + ': ' + item['title'] + ' (' + item['function'] + ')')
        return
    item = next((item for item in catalog if str(item['id']) == args.exercise), None)
    if item is None:
        parser.error('Unknown exercise; use --list')
    arguments = json.loads(args.arguments)
    if not isinstance(arguments, list):
        parser.error('Arguments must be a JSON array')
    print(json.dumps(globals()[item['function']](*arguments), ensure_ascii=False))
if __name__ == '__main__':
    main()
