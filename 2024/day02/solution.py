import functools

with open('./input', 'r') as f:
  data = f.read().strip()

lines = data.split('\n')
records = [[int(x) for x in line.split(' ')] for line in lines]

def valid(arr):
  diffs = [arr[idx] - arr[idx - 1] for idx in range(1, len(arr))]
  sign_count = 0
  valid_count = 0
  for diff in diffs:
    if diff > 0:
      sign_count += 1
    elif diff < 0:
      sign_count -= 1
    if 1 <= abs(diff) <= 3:
      valid_count += 1
  return abs(sign_count) == len(diffs) and valid_count == len(diffs)


def solve1():
  count = 0
  for record in records:
    if valid(record):
      count += 1
  print(count)


def solve2():
  count = 0
  for record in records:
    if valid(record):
      count += 1
    else:
      is_valid = False
      for i in range(len(record)):
        new_record = record[:i] + record[i+1:]
        if valid(new_record):
          is_valid = True
      if is_valid == True:
        count += 1
  print(count)
  return


solve1()
solve2()