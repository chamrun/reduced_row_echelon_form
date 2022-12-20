import numpy as np


def input_matrix() -> np.ndarray:
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = int(input(f"Enter element [{i + 1}][{j + 1}]: "))

    return matrix


def find_reduced_row_echelon_form(matrix: np.ndarray) -> np.ndarray:
    matrix = matrix.astype(float)
    rows, cols = matrix.shape
    lead = 0
    for r in range(rows):
        if lead >= cols:
            return matrix
        i = r
        while matrix[i, lead] == 0:
            i += 1
            if i == rows:
                i = r
                lead += 1
                if cols == lead:
                    return matrix
        matrix[[i, r]] = matrix[[r, i]]
        lv = matrix[r, lead]
        matrix[r] = matrix[r] / lv
        for i in range(rows):
            if i != r:
                lv = matrix[i, lead]
                matrix[i] = matrix[i] - lv * matrix[r]
        lead += 1
    return matrix
