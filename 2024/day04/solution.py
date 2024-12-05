with open('./input', 'r') as f:
  data = f.read().strip()

lines = data.split('\n')
matrix = [list(line) for line in lines]

def horizontal(m):
  count = 0
  for row in m:
    idx = 0
    while idx < len(row) - 3:
      while idx < len(row) and row[idx] != 'X':
        idx += 1
      if idx >= len(row):
        break
      if ''.join(row[idx:idx+4]) == 'XMAS':
        count += 1
      idx += 1
  return count

def vertical(m):
  n = [[m[c][r] for c in range(len(m[0]))] for r in range(len(m))]
  return horizontal(n)

def diagonal(m):
  count = 0
  row_cnt = len(m)
  col_cnt = len(m[0])
  for i in range(col_cnt - 3):
    for j in range(row_cnt - 3):
      if m[j][i] != 'X':
        continue
      if ''.join([m[j+x][i+x] for x in range(4)]) == 'XMAS':
        count += 1
  n = m[::-1]
  for i in range(col_cnt - 3):
    for j in range(row_cnt - 3):
      if n[j][i] != 'X':
        continue
      if ''.join([n[j+x][i+x] for x in range(4)]) == 'XMAS':
        count += 1
  return count

def solve1():
  total = 0
  # count horizontal, vertical and diagonal
  total += horizontal(matrix)
  total += vertical(matrix)
  total += diagonal(matrix)

  # diagonally flip the matrix, count reversed.
  reversed_matrix = [row[::-1] for row in matrix[::-1]]
  total += horizontal(reversed_matrix)
  total += vertical(reversed_matrix)
  total += diagonal(reversed_matrix)

  return total

print(f'part one: {solve1()}')

def solve2():
  row_cnt = len(matrix)
  col_cnt = len(matrix[0])
  total = 0
  for r in range(1, row_cnt-1):
    for c in range(1, col_cnt-1):
      if matrix[r][c] != 'A':
        continue
      v1 = matrix[r-1][c-1] + matrix[r][c] + matrix[r+1][c+1]
      v2 = matrix[r-1][c+1] + matrix[r][c] + matrix[r+1][c-1]
      if v1 in ['MAS', 'SAM'] and v2 in ['MAS', 'SAM']:
        total += 1
  return total

print(f'part two: {solve2()}')
