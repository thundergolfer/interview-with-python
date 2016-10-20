import unittest

def triples_adding_to( x, lst ):
    if len(lst) < 3: return None
    results = set()
    for pos, elem  in enumerate(lst):
        i, j = pos+1, len(lst) - 1
        complement = x - elem
        while i < len(lst) and j > -1 and i < j:
            if pos == i:
                i += 1
                continue
            elif pos == j:
                j -= 1
                continue
            pair_result = lst[i] + lst[j]
            if pair_result > complement:
                j -= 1
            elif pair_result < complement:
                i += 1
            elif pair_result == complement:
                results.add(tuple(sorted([elem, lst[i], lst[j]])))
                i += 1 # could also do j -= 1

    return results


class TestTriplesSummingToX(unittest.TestCase):
    def test_triples_adding_to(self):
        test_lst = [-10, -7, -5, -1, 0, 2, 3, 5, 8, 10]
        self.assertEqual(
            triples_adding_to(5, []), None
        )
        self.assertEqual(
            triples_adding_to(5, test_lst),
            {(-7, 2, 10), (0, 2, 3), (-5, 0, 10), (-10, 5, 10), (-5, 2, 8)}
        )

if __name__ == '__main__':
    unittest.main()
