with open('./input', 'r') as f:
  data = f.read().strip()

def transform(matrix):
  row = len(matrix)
  col = len(matrix[0])
  return [[matrix[j][i] for j in range(col)] for i in range(row)]


def find_emptys(spaces):
  empty_list = []
  for idx, row in enumerate(spaces):
    if all(v == '.' for v in row):
      empty_list.append(idx)
  return empty_list


def solve(data, expansion = 1):
  spaces = [list(line) for line in data.split('\n')]
  row = len(spaces)
  col = len(spaces[0])

  coords = [[[i, j] for j in range(col)] for i in range(row)]
  empty_rows = find_emptys(spaces)
  for empty_row in empty_rows:
    for i in range(empty_row, row):
      for j in range(col):
        coords[i][j][0] += expansion
  empty_cols = find_emptys(transform(spaces))
  for empty_col in empty_cols:
    for j in range(empty_col, col):
      for i in range(row):
        coords[i][j][1] += expansion

  galaxy_coords = []
  for i in range(row):
    for j in range(col):
      if spaces[i][j] == '#':
        galaxy_coords.append(coords[i][j])
  total_distance = 0
  for i, coord in enumerate(galaxy_coords):
    for j in range(i + 1, len(galaxy_coords)):
      total_distance += abs(coord[0] - galaxy_coords[j][0]) + abs(coord[1] - galaxy_coords[j][1])

  return total_distance



# part one
print(solve(data, 1))
# part two
print(solve(data, 1000000-1))