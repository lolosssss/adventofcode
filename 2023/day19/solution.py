import re

with open('./test', 'r') as f:
  data = f.read().strip()


def parse_workflows(workflows):
  obj = {}
  for workflow in workflows:
    name, rules, _ = re.split(r'[{}]', workflow)
    obj[name] = rules.split(',')
  return obj


def parse_rating(rating):
  obj = {}
  for v in rating[1:-1].split(','): obj[v[0]] = int(v[2:])
  return obj


def sum_rating(rating):
  total = 0
  for k in ['x', 'm', 'a', 's']:
    total += rating[k]
  return total


def compare(k, v, o, rating):
  if o == '>':
    return rating[k] > v
  if o == '<':
    return rating[k] < v


def check(rating, wn, workflows):
  # start from workflow named 'in'
  rules = workflows[wn]

  for rule in rules[:-1]:
    e, n = rule.split(':')
    k, o, v = e[0], e[1], int(e[2:])
    if compare(k, v, o, rating):
        if n == 'A':
          return True
        elif n == 'R':
          return False
        return check(rating, n, workflows)

  last = rules[-1]
  if last == 'A':
    return True
  elif last == 'R':
    return False
  return check(rating, last, workflows)


def solve(workflows, ratings):
  workflows = parse_workflows(workflows)
  ratings = list(map(parse_rating, ratings))
  total = 0

  for rating in ratings:
    if check(rating, 'in', workflows):
      total += sum_rating(rating)

  print(total)


workflows, ratings = [p.split('\n') for p in data.split('\n\n')]
solve(workflows, ratings)