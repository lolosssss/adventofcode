import re

with open('./input', 'r') as f:
  data = f.read().strip()

data = data.replace('\n', '')

def solve1():
  sum = 0
  idx = 0
  content = ''

  while idx < len(data):
    while idx < len(data) and data[idx] != 'm':
      idx += 1
    if idx >= len(data):
      break
    while idx < len(data) and data[idx] != ')':
      content += data[idx]
      idx += 1
    content += ')'
    match = re.match(r'm.*ul\((\d+),(\d+)\)', content)
    if match != None:
      n1, n2 = match.group(1), match.group(2)
      sum += int(n1) * int(n2)
    idx += 1
    content = ''

  print(f'part one - sum: {sum}')

def solve2():
  sum = 0
  idx = 0
  content = ''
  enabled = True

  while idx < len(data):
    while idx < len(data) and (data[idx] != 'm' and data[idx] != 'd'):
      idx += 1
    if idx >= len(data):
      break
    if data[idx] == 'd':
      if idx+4 < len(data) and data[idx:idx+4] == "do()":
        enabled = True
        idx += 4
        continue
      if idx+7 < len(data) and data[idx:idx+7] == "don't()":
        enabled = False
        idx += 7
        continue
    if enabled == False:
      idx += 1
      continue
    while idx < len(data) and data[idx] != ')':
      content += data[idx]
      idx += 1
    content += ')'
    match = re.match(r'm.*ul\((\d+),(\d+)\)', content)
    if match != None:
      n1, n2 = match.group(1), match.group(2)
      sum += int(n1) * int(n2)
    idx += 1
    content = ''
  
  print(f'part two - sum: {sum}')
  return

solve1()
solve2()