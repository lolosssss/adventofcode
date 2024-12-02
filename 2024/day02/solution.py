import functools

with open('./input', 'r') as f:
  data = f.read().strip()

lines = data.split('\n')
records = [[int(x) for x in line.split(' ')] for line in lines]

def solve1():
  count = 0
  for record in records:
    diffs = [record[idx] - record[idx - 1] for idx in range(1, len(record))]
    sign_count = 0
    valid_count = 0
    for diff in diffs:
      if diff > 0:
        sign_count += 1
      elif diff < 0:
        sign_count -= 1
      if abs(diff) <= 3:
        valid_count += 1
    if abs(sign_count) == len(diffs) and valid_count == len(diffs):
      count += 1
  print(count)


def solve2():
  return


solve1()
solve2()