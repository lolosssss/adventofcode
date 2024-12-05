with open('./input', 'r') as f:
  data = f.read().strip()

part1, part2 = data.split('\n\n')
rules = [[int(i) for i in item.split('|')] for item in part1.split('\n')]
update_list = [[int(i) for i in item.split(',')] for item in part2.split('\n')]

rule_dict = {}
for rule in rules:
  l, r = rule
  if l in rule_dict:
    rule_dict[l].append(r)
  else:
    rule_dict[l] = [r]

def valid(record):
  for i in range(1, len(record)):
    if record[i] in rule_dict:
      for j in range(i):
        if record[j] in rule_dict[record[i]]:
          return False
  return True

def solve1():
  sum = 0
  for record in update_list:
    if valid(record):
      sum += record[int(len(record) / 2)]
  return sum

print(f'part one: {solve1()}')

def reorder(record):
  new_record = [record[0]]
  for i in range(1, len(record)):
    if new_record[-1] in rule_dict:
      if record[i] in rule_dict[new_record[-1]]:
        new_record.append(record[i])
      elif record[i] in rule_dict:
        j = 0
        while j < len(new_record) and new_record[j] not in rule_dict[record[i]]:
          j += 1
        new_record.insert(j, record[i])
    else:
      if record[i] in rule_dict:
        j = 0
        while j < len(new_record) and new_record[j] not in rule_dict[record[i]]:
          j += 1
        new_record.insert(j, record[i])
  # print(new_record)
  return new_record[int(len(new_record) / 2)]

def solve2():
  sum = 0
  for record in update_list:
    if valid(record) == False:
      sum += reorder(record)
  return sum

print(f'part two: {solve2()}')