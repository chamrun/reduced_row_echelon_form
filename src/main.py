from calculator import find_reduced_row_echelon_form, input_matrix
import pandas as pd


def main():
    import numpy as np
    matrix = np.array([[10, -4, -6, 0], [-6, 9, -2, 0], [-4, -5, 8, 0]])
    # matrix = input_matrix()
    reduced_row_echelon_form = find_reduced_row_echelon_form(matrix)
    df = pd.DataFrame(reduced_row_echelon_form)
    print(df)


if __name__ == '__main__':
    main()
