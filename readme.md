# Reduced Row Echelon Form

## Introduction

This code provides a function for finding the reduced row echelon form of a matrix. The reduced row echelon form is a
canonical form for a matrix that is often used in linear algebra and other mathematical applications.

## Requirements

This code requires the `numpy` library.

## Usage

There are two main functions in this code:

- `input_matrix()`: This function prompts the user to input a matrix by specifying the number of rows and columns, and
  then allowing the user to enter each element of the matrix. The function returns the matrix input by the user as
  a `numpy` array.

- `find_reduced_row_echelon_form(matrix)`: This function takes a matrix as a `numpy` array and returns the reduced row
  echelon form of the matrix.

Here is an example of how to use these functions:

```python

matrix = input_matrix()
reduced_matrix = find_reduced_row_echelon_form(matrix)
print(reduced_matrix)
```

## Limitations

This code currently only works for matrices with numerical elements. It does not support matrices with complex or
symbolic elements.

## Further Reading

- [Reduced Row Echelon Form](https://en.wikipedia.org/wiki/Row_echelon_form#Reduced_row_echelon_form) on Wikipedia
- [Row Echelon Form](https://mathworld.wolfram.com/RowEchelonForm.html) on MathWorld

[//]: # (- [Row Echelon Form and Reduced Row Echelon Form]&#40;https://www.math.ubc.ca/~cass/courses/m308-02a/docs/RowEchelonForm.pdf&#41;)

[//]: # (  - Notes from the University of British Columbia)
