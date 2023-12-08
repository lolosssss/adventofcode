import re

with open('./input', 'r') as f:
  data = f.read().strip()


# part one
def sum_of_one_line(p, c, n):
  p = '.' + p + '.'
  c = '.' + c + '.'
  n = '.' + n + '.'
  sum = 0
  idx = 1
  num_str = ''
  start = 1
  end = 1
  while idx < 142:
    if c[idx].isdigit():
      num_str += c[idx]
      end += 1
    else:
      if len(num_str) > 0:
        around_str = p[start:end+2] + c[start:end+2] + n[start:end+2]
        if re.match(r'.*[^\.\d].*', around_str):
          num = int(num_str)
          sum += num
        num_str = ''
      start = idx
      end = start

    idx += 1

  return sum

def sum_of_part_number(data):
  lines = data.split('\n')
  sum = 0
  sum += sum_of_one_line('.' * 140, lines[0], lines[1])
  row = 1
  while row < 139:
    sum += sum_of_one_line(lines[row-1], lines[row], lines[row+1])
    row += 1
  sum += sum_of_one_line(lines[138], lines[139], '.' * 140)
  return sum

print(sum_of_part_number(data))

# part two
arr = [[{'cnt': 0, 'value': 1} for i in range(140)] for j in range(140)]

def process_one_line(p, c, n, line_num):
  p = '.' + p + '.'
  c = '.' + c + '.'
  n = '.' + n + '.'
  idx = 1
  num_str = ''
  start = 1
  end = 1
  while idx < 142:
    if c[idx].isdigit():
      num_str += c[idx]
      end += 1
    else:
      if len(num_str) > 0:
        num = int(num_str)
        for cnt, t in enumerate([p, c, n]):
          ptr = start
          while ptr < end + 2:
            if t[ptr] == '*':
              arr[line_num-1+cnt][ptr]['cnt'] = arr[line_num-1+cnt][ptr]['cnt'] + 1
              arr[line_num-1+cnt][ptr]['value'] = arr[line_num-1+cnt][ptr]['value'] * num
            ptr += 1
        num_str = ''
      start = idx
      end = start

    idx += 1

def sum_of_gear_ratio(data):
  lines = data.split('\n')
  process_one_line('.' * 140, lines[0], lines[1], 0)
  row = 1
  while row < 139:
    process_one_line(lines[row-1], lines[row], lines[row+1], row)
    row += 1
  process_one_line(lines[138], lines[139], '.' * 140, 139)
  sum = 0
  for row in arr:
    for col in row:
      if col['cnt'] == 2:
        sum += col['value']
  return sum

print(sum_of_gear_ratio(data))