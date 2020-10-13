def print_matrix_in_spiral_reverse(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    size = rows * cols
    res = []

    top = 0
    left = 0
    bottom = rows - 1
    right = cols - 1

    while len(res) < size:
        for i in range(right, left - 1, -1):
            if len(res) < size:
                res.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            if len(res) < size:
                res.append(matrix[i][left])
        left += 1

        for i in range(left, right + 1):
            if len(res) < size:
                res.append(matrix[bottom][i])
        bottom -= 1

        for i in range(bottom, top - 1, -1):
            if len(res) < size:
                res.append(matrix[i][right])
        right -= 1
    return res

def main():
  matrix = [
    [1, 2, 3, 13, 23],
    [4, 5, 6, 16, 26],
    [7, 8, 9, 19, 29],
  ]
  for r in matrix:
    print(r)

  spiral = print_matrix_in_spiral_reverse(matrix)
  print(spiral)


if __name__ == '__main__':
  main()
