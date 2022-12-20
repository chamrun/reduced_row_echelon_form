import numpy as np


def input_matrix() -> np.ndarray:
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = int(input(f"Enter element [{i + 1}][{j + 1}]: "))

    return matrix

