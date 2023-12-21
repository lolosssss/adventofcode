import re
import copy

with open('./input', 'r') as f:
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


def recur(c, wn, workflows):
  rules = workflows[wn]
  total = 0
  for rule in rules[:-1]:
    nc = copy.deepcopy(c)
    e, n = rule.split(':')
    k, o, v = e[0], e[1], int(e[2:])
    if o == '>':
      nc[k][0] = v + 1 if v > nc[k][0] else nc[k][0]
    else:
      nc[k][1] = v - 1 if v < nc[k][1] else nc[k][1]
    if n == 'A':
      t = 1
      for cc in nc:
        t *= (nc[cc][1] - nc[cc][0] + 1)
      total += t
    elif n != 'R':
      total += recur(nc, n, workflows)
    if o == '<':
      c[k][0] = v if v > c[k][0] else c[k][0]
    else:
      c[k][1] = v if v < c[k][1] else c[k][1]

  last = rules[-1]
  nc = copy.deepcopy(c)
  if last == 'A':
    t = 1
    for cc in nc:
      t *= (nc[cc][1] - nc[cc][0] + 1)
    total += t
  elif last != 'R':
    total += recur(nc, last, workflows)
  return total


def solve_2(workflows):
  workflows = parse_workflows(workflows)
  c = {
    'x': [1, 4000],
    'm': [1, 4000],
    'a': [1, 4000],
    's': [1, 4000],
  }

  total = recur(c, 'in', workflows)
  print(total)


workflows, ratings = [p.split('\n') for p in data.split('\n\n')]
solve(workflows, ratings)

solve_2(workflows)