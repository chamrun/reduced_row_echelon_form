import unittest

import numpy as np

from reduced_row_echelon_form import find_reduced_row_echelon_form


class TestReducedRowEchelonForm(unittest.TestCase):
    def test_case_1(self):
        input_matrix = np.array(
            [
                [10, -4, -6, 0],
                [-6, 9, -2, 0],
                [-4, -5, 8, 0]
            ]
        )

        result = find_reduced_row_echelon_form(input_matrix)

        expected_result = np.array(
            [
                [1, 0, -31 / 33, 0],
                [0, 1, -28 / 33, 0],
                [0, 0, 0, 0]
            ]
        )

        self.assertTrue(np.array_equal(result, expected_result))


if __name__ == '__main__':
    unittest.main()
