# 12 red, 13 green, 14 blue

import re

with open('./input', 'r') as f:
  data = f.read().strip()

# part one
def sum(data):
  games = data.split('\n')
  s = 0
  for game in games:
    game_idx, sets = map(lambda item: item.strip(), game.split(':'))
    idx = int(game_idx.split(' ')[1])
    if (
      re.match(
        r'.*(?:[1][^0-2] red|[1][^0-3] green|[1][^0-4] blue|2\d \w*).*', sets
      )
      is None
    ):
      s += idx
    else:
      print(idx, sets)

  return s

print(sum(data))

# part two
def sum_of_power(data):
  games = data.split('\n')
  s = 0
  for game in games:
    game_idx, sets = map(lambda item: item.strip(), game.split(':'))
    max_c = {
      'red': 0,
      'green': 0,
      'blue': 0
    }
    rounds = map(lambda item: item.strip(), sets.split(';'))
    for round in rounds:
      cubes = round.split(',')
      num_and_colors = [cube.strip().split(' ') for cube in cubes]
      for num, color in num_and_colors:
        num = int(num)
        if num > max_c[color]:
          max_c[color] = num
    s += max_c['red'] * max_c['green'] * max_c['blue']
  return s

print(sum_of_power(data))
