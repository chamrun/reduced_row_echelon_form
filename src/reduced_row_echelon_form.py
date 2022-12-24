import numpy as np


def input_matrix() -> np.ndarray:
    """
    Input a matrix from the user.

    Returns:
        np.ndarray: The matrix input by the user.
    """

    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    matrix = np.zeros((rows, cols))

    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = int(input(f"Enter element [{i + 1}][{j + 1}]: "))

    return matrix


def find_reduced_row_echelon_form(matrix: np.ndarray) -> np.ndarray:
    """
    Find the reduced row echelon form of a matrix.

    Args:
        matrix (np.ndarray): The matrix to find the reduced row echelon form of.

    Returns:
        np.ndarray: The reduced row echelon form of the matrix.
    """

    matrix = matrix.astype(float)
    rows, cols = matrix.shape
    lead = 0  # lead is the index of the first non-zero element in a row

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

        matrix[[i, r]] = matrix[[r, i]]  # Swap rows i and r to put the pivot on the diagonal.

        pivot_value = matrix[r, lead]
        matrix[r] = matrix[r] / pivot_value  # Divide row r by the pivot value.

        for i in range(rows):
            if i != r:
                row_i_value = matrix[i, lead]
                matrix[i] = matrix[i] - row_i_value * matrix[r]  # Subtract row r from row i.
        lead += 1

    return matrix
