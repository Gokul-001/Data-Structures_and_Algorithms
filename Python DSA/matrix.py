from copy import deepcopy


row,col=2,4
zero_matrix = [ [0 for _ in range(col)] for _ in range(row)]
copy_matrix= [row[::]for row in zero_matrix]
def transpose_matrix(matrix):
    # Get the number of rows and columns in the original matrix
    rows = len(matrix)
    columns = len(matrix[0])

    # Create a new matrix with swapped rows and columns
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(columns)]

    # Perform the transpose
    for i in range(rows):
        for j in range(columns):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

# Example usage:
original_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose_matrix(original_matrix))
# transpose =zip(*matrix) -> another way