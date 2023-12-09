import re

# part one
with open('./input', 'r') as f:
  data = f.read().strip()

def sum_of_points(data):
  lines = data.split('\n')
  sum = 0
  for line in lines:
    _, winning_num_str, num_str = re.split(r':|\|', line)
    winning_nums = [int(n) for n in re.split(r' +', winning_num_str.strip())]
    nums = [int(n) for n in re.split(r' +', num_str.strip())]
    intersection = list(set(winning_nums) & set(nums))
    cnt = len(intersection)
    sum += 2 ** (cnt - 1) if cnt > 0 else 0

  return sum

# print(sum_of_points(data))

# part two
def sum_of_copies(data):
  lines = data.split('\n')
  counts = [1] * len(lines)
  for idx, line in enumerate(lines):
    _, winning_num_str, num_str = re.split(r':|\|', line)
    winning_nums = [int(n) for n in re.split(r' +', winning_num_str.strip())]
    nums = [int(n) for n in re.split(r' +', num_str.strip())]
    intersection = list(set(winning_nums) & set(nums))
    cnt = len(intersection)
    for i in range(cnt):
      counts[idx + i + 1] += counts[idx]

  return sum(counts)

print(sum_of_copies(data))
