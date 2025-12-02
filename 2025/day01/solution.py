with open("input", "r") as f:
  data = f.read().strip()

rotations = list(map(lambda r: [-1 if r[0] == 'L' else 1, int(r[1:])], data.split("\n")))


def solve1():
  count = 0
  current = 50
  for rotation in rotations:
    d, clicks = rotation
    current = current + d * clicks
    if current % 100 == 0:
      count += 1

  return count


print(f"prat one: {solve1()}")


def solve2():
  count = 0
  current = 50
  for rotation in rotations:
    d, clicks = rotation
    while clicks > 0:
      current += d
      if current == 0:
        count += 1
      elif current < 0:
        current = 99
      elif current == 100:
        count += 1
        current = 0
      clicks -= 1

  return count


print(f"part two: {solve2()}")
