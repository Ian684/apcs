import itertools
import random
import unittest
from practice.range_queries import solve
from practice.maze import shortest_route
from practice.meeting_rooms import minimum_rooms
from practice.shipping import minimum_capacity


class PracticeTests(unittest.TestCase):
    def test_queries(self):
        self.assertEqual(solve('5 3\n2 -3 5 7 1\n1 5\n2 4\n3 3'), '12\n9\n5')
        self.assertEqual(solve('1 1\n-9\n1 1'), '-9')
        with self.assertRaises(ValueError): solve('1 1 9 0 1')

    def test_maze(self):
        self.assertEqual(shortest_route(['S..', '##.', '..G']), 4)
        self.assertEqual(shortest_route(['S#G']), -1)
        self.assertEqual(shortest_route(['SG']), 1)
        with self.assertRaises(ValueError): shortest_route(['S..'])

    def test_rooms_against_timeline(self):
        rng = random.Random(684)
        for _ in range(60):
            intervals = [(start, start + rng.randrange(1, 5)) for start in rng.choices(range(10), k=12)]
            expected = max(sum(a <= t < b for a, b in intervals) for t in range(15))
            self.assertEqual(minimum_rooms(intervals), expected)
        self.assertEqual(minimum_rooms([(0, 1), (1, 2)]), 1)
        self.assertEqual(minimum_rooms([]), 0)

    def test_shipping_against_all_partitions(self):
        rng = random.Random(684)
        for _ in range(30):
            weights = [rng.randrange(1, 9) for _ in range(6)]
            for days in range(1, 7):
                capacities = []
                for cuts in itertools.combinations(range(1, len(weights)), days - 1):
                    bounds = (0,) + cuts + (len(weights),)
                    capacities.append(max(sum(weights[a:b]) for a, b in zip(bounds, bounds[1:])))
                self.assertEqual(minimum_capacity(weights, days), min(capacities))


if __name__ == '__main__': unittest.main()
