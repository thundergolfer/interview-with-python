# binary_islands: count the number of connected groups of 1's in a binary matrix
# author: Matt Box

def binary_islands(matrix):
    # plan:
    # 1. find a one.
    # 2. tally up one island.
    # 3. mark this cell in a do not visit list and do the same with
    #    any of our neighbours who are 1.
    #    do this recursively so we mark a whole island at a time.
    # 4. repeat until the matrix is exhausted.

    height = len(matrix)
    width = len(matrix[0])

    # setup do_not_visit[][]
    do_not_visit = [[False] * width for i in range(height)]
    # that was from:
    # https://docs.python.org/3/faq/programming.html#how-do-i-create-a-multidimensional-list 
    # ... python is weird.

    def visit(i, j):
        # don't come back
        do_not_visit[i][j] = True
        # visit neighbours who are 1
        if j < (width-1) and matrix[i][j+1] == 1 and not do_not_visit[i][j+1]:
            visit(i, j+1)
        if j > 0 and matrix[i][j-1] == 1 and not do_not_visit[i][j-1]:
            visit(i, j-1)
        if i < (height-1) and matrix[i+1][j] == 1 and not do_not_visit[i+1][j]:
            visit(i+1, j)
        if i > 0 and matrix[i-1][j] == 1 and not do_not_visit[i-1][j]:
            visit(i-1, j)

    def find_a_one(matrix):
        for i in range(height):
            for j in range(width):
                if matrix[i][j] == 1 and not do_not_visit[i][j]:
                    return i, j
        return -1, -1

    islands = 0
    while True:
        i, j = find_a_one(matrix)
        if i < 0:
            # i.e. we could not find a one
            break
        islands += 1
        visit(i, j)

    return islands

import unittest

class Test(unittest.TestCase):
    def test_sanity(self):
        self.assertEqual(binary_islands([[0,0,0,0,0],
                                         [0,0,0,0,0],
                                         [0,0,0,0,0],
                                         [0,0,0,0,0]]), 0)
        self.assertEqual(binary_islands([[1,1,1,1,1],
                                         [1,1,1,1,1],
                                         [1,1,1,1,1],
                                         [1,1,1,1,1]]), 1)
        self.assertEqual(binary_islands([[1,1,0,0,1],
                                         [1,0,0,1,1],
                                         [0,0,0,0,1],
                                         [1,1,0,0,0]]), 3)

if __name__ == '__main__':
    unittest.main()

