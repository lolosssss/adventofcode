from math import ceil

with open('./input', 'r') as f:
  data = f.read().strip()

next_directions = {
  '|': {'n': 's', 's': 'n'},
  '-': {'w': 'e', 'e': 'w'},
  'L': {'n': 'e', 'e': 'n'},
  'J': {'n': 'w', 'w': 'n'},
  '7': {'s': 'w', 'w': 's'},
  'F': {'s': 'e', 'e': 's'},
}

moving = {
  'n': [-1, 0],
  'e': [0, 1],
  's': [1, 0],
  'w': [0, -1],
}

start_point = [90, 62]


def get_opposite_dir(dir):
  match dir:
    case 'n':
      return 's'
    case 'e':
      return 'w'
    case 's':
      return 'n'
    case 'w':
      return 'e'


# def check_stack(stack):
#   print(stack)
#   match stack:
#     case ['-']:
#       return 1
#     case 'L', *_, 'F':
#       return 2
#     case 'L', *_, '7':
#       return 3
#     case 'J', *_, 'F':
#       return 3
#     case 'J', *_, '7':
#       return 2
#   print(stack)
#   return 1

def convert(val):
  mapping = {
    'J': 1,
    '7': 1,
    '-': 1,
    '.': 0,
    '|': 0,
    'L': 2,
    'F': 2,
  }
  return mapping[val]
  

def solve(data):
  grids = [list(line) for line in data.split('\n')]
  row, col = start_point
  row = row - 1
  current_tile = grids[row][col]
  current_dir = 'n'
  steps = 1

  flags = [[0] * len(grids[0]) for _ in range(len(grids))]
  flags[start_point[0]][start_point[1]] = 1
  flags[row][col] = 1

  while current_tile != 'S':
    next_dir = next_directions[current_tile][get_opposite_dir(current_dir)]
    movement = moving[next_dir]
    row, col = row + movement[0], col + movement[1]
    flags[row][col] = 1
    current_tile = grids[row][col]
    current_dir = next_dir
    steps += 1
  
  print('part one', ceil(steps / 2))


  # part two
  #
  # 往上检查，如果与包围圈相交边数量为偶数，即在包围圈外，如果为奇数，在包围圈内。
  # 规则：
  #   * 如果沿着边，需要检查边的两头方向是否一致，如果一致，计算为偶数，反向则计算为奇数
  rows = len(grids)
  cols = len(grids[0])
  num = 0

  grids[start_point[0]][start_point[1]] = 'L'

  for j in range(cols):
    stack = []
    for i in range(rows):
      if flags[i][j] == 1:
        stack.append(convert(grids[i][j]))
      if flags[i][j] != 1:
        if sum(stack) % 2 == 1:
          num += 1

  print('part two', num)


solve(data)
