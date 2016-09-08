import unittest

def rotate_matrix( matrix ):
    matrix_two = [list() for i in range(len(matrix))]
    for i in range(len(matrix)):
        matrix.reverse()
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            matrix_two[i].append(matrix[j][i])
    return matrix_two

def rotate_matrix_two( matrix ):
    return zip(*matrix[::-1])

class test_rotate_matrix(unittest.TestCase):

    def setUp(self):
        pass

    def test_rotate_matrix(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        rotated = rotate_matrix( matrix )
        self.assertEqual( rotated[0][0], 7)
        self.assertEqual( rotated[0][2], 1)

if __name__ == '__main__':
    unittest.main()
