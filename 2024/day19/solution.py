with open('./input', 'r') as f:
  data = f.read().strip()

p1, p2 = data.split('\n\n')
patterns = p1.split(', ')
designs = p2.split('\n')


def dfs(words, target: str, his: dict):
  if target in his:
    return his[target]
  if not target:
    return 1
  count = 0
  for word in words:
    if target.startswith(word):
      count += dfs(words, target[len(word):], his)
  his[target] = count
  return count


def solve():
  his = dict()
  impossible = 0
  total = 0
  count = 0
  for design in designs:
    print(f'\rcurrent: {count}', end='')
    ans = dfs(patterns, design, his)
    if ans > 0:
      impossible += 1
      total += ans
    count += 1
  print()
  return (impossible, total)


print(f'(part 1, part2): {solve()}')
