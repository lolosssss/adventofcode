with open("./input", "r") as f:
  data = f.read().strip()

mat = [list(row) for row in data.split("\n")]
freqs = dict()
row = len(mat)
col = len(mat[0])
for r in range(row):
  for c in range(col):
    if mat[r][c] != ".":
      if mat[r][c] in freqs:
        freqs[mat[r][c]].append((r, c))
      else:
        freqs[mat[r][c]] = [(r, c)]


def solve1():
  seen = set()
  for freq, locs in freqs.items():
    s = len(locs)
    for i in range(s - 1):
      p1 = locs[i]
      for j in range(i + 1, s):
        p2 = locs[j]
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        p_l = (p1[0] - dx, p1[1] - dy)
        p_r = (p2[0] + dx, p2[1] + dy)
        if 0 <= p_l[0] < row and 0 <= p_l[1] < col:
            seen.add(p_l)
        if 0 <= p_r[0] < row and 0 <= p_r[1] < col:
            seen.add(p_r)
  return len(seen)


print(f"part one: {solve1()}")


def solve2():
  seen = set()
  for freq, locs in freqs.items():
    s = len(locs)
    for i in range(s - 1):
      p1 = locs[i]
      for j in range(i + 1, s):
        p2 = locs[j]
        seen.add(p1)
        seen.add(p2)
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        t = 1
        p_l = (p1[0] - dx, p1[1] - dy)
        while 0 <= p_l[0] < row and 0 <= p_l[1] < col:
          seen.add(p_l)
          t += 1
          p_l = (p1[0] - t * dx, p1[1] - t * dy)
        t = 1
        p_r = (p2[0] + dx, p2[1] + dy)
        while 0 <= p_r[0] < row and 0 <= p_r[1] < col:
          seen.add(p_r)
          t += 1
          p_r = (p2[0] + t * dx, p2[1] + t * dy)

  return len(seen)


print(f"part two: {solve2()}")