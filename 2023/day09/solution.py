
with open('./input', 'r') as f:
  data = f.read().strip()

def predict(history, backwards = False):
  all_zero = False
  diffs = [history]
  idx = 0
  while not all_zero:
    prev = diffs[idx]
    diff = [prev[i+1] - prev[i] for i in range(len(prev) - 1)]
    diffs.append(diff)
    idx += 1
    all_zero = all(item == 0 for item in diff)
  if backwards:
    return sum([(item[0] * pow(-1, i)) for i, item in enumerate(diffs) ])
  return sum([item[-1] for item in diffs])


def solve(data):
  histories = [list(map(int, line.split(' '))) for line in data.split('\n')]
  return sum([predict(history) for history in histories])


def solve_2(data):
  histories = [list(map(int, line.split(' '))) for line in data.split('\n')]
  return sum([predict(history, True) for history in histories])


print(solve(data))
print(solve_2(data))
