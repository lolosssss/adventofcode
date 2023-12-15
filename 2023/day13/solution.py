with open('./input', 'r') as f:
  data = f.read().strip()

def transform(matrix):
  row = len(matrix)
  col = len(matrix[0])
  new_matrix = [['' for _ in range(row)] for _ in range(col)]
  for i in range(row):
    for j in range(col):
      new_matrix[j][i] = matrix[i][j]
  return new_matrix


def compare_row(a, b):
  l = len(a)
  diff = 0
  for i in range(l):
    if a[i] != b[i]:
      diff += 1
  return diff


def guess(block, diff=0):
  for f in [100, 1]:
    row = len(block)
    for i in range(1, row):
      l, r = i - 1, i
      diffs = 0
      while l >= 0 and r < row:
        diffs += compare_row(block[l], block[r])
        l -= 1
        r += 1
      if diffs == diff:
        return i * f
    block = transform(block)

  return 0

def solve(data):
  blocks = data.split('\n\n')

  # part one
  total = 0
  for block in blocks:
    total += guess([list(row) for row in block.split('\n')], 0)
  print(total)

  # part two
  total = 0
  for block in blocks:
    total += guess([list(row) for row in block.split('\n')], 1)
  print(total)

solve(data)