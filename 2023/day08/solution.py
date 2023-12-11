import re
from math import lcm

with open('./input', 'r') as f:
  data = f.read().strip()

lines = data.split('\n')
instructs = lines[0]
nodes = lines[2:]

def build_graph(lines):
  graph = dict({})

  for line in lines:
    n, l, r, *_ = re.split(r'[ =(,)]+', line)
    graph[n] = { 'L': l, 'R': r}

  return graph


graph = build_graph(nodes)

def solve(instructs, graph):
  steps = 0
  current = 'AAA'
  idx = 0
  length = len(instructs)
  while current != 'ZZZ':
    node = graph[current]
    current = node[instructs[idx]]
    steps += 1
    idx = idx + 1 if idx < length - 1 else 0

  return steps

print(solve(instructs, graph))

def solve_part_two(instructs, graph):
  steps = []
  starts = list(filter(lambda n: n.endswith('A'), graph.keys()))
  length = len(instructs)

  for start in starts:
    idx = 1
    current = graph[start][instructs[0]]
    step = 1
    while current[-1] != 'Z':
      next = graph[current]
      current = next[instructs[idx]]
      step += 1
      idx = idx + 1 if idx < length - 1 else 0
    steps.append(step)

  return lcm(*steps)

print(solve_part_two(instructs, graph))