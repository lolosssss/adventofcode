with open('./input', 'r') as f:
  data = f.read().strip()

dm = [int(c) for c in list(data)]

def print_blocks(blocks):
  content = ''
  for b in blocks:
    if b == -1:
      content += '.'
    elif b == -2:
      content += '*'
    else:
      content += str(b)
  print(content)

def solve1():
  blocks = []
  f_id = 0
  for idx in range(len(dm)):
    if idx % 2 == 0:
      # file blocks
      c = dm[idx]
      for _ in range(c):
        blocks.append(f_id)
      f_id += 1
    else:
      # free spaces
      c = dm[idx]
      for _ in range(c):
        blocks.append(-1)

  lp = 0
  rp = len(blocks) - 1
  while lp < len(blocks) and rp >= 0 and lp < rp:
    while lp < len(blocks) and blocks[lp] >= 0:
      lp += 1
    while rp >= 0 and blocks[rp] == -1:
      rp -= 1
    if lp >= rp:
      break
    blocks[lp], blocks[rp] = blocks[rp], -2
    lp += 1
    rp -= 1

  total = 0
  for idx, fid in enumerate(blocks):
    if fid >= 0:
      total += idx * fid
  return total

print(f'part one: {solve1()}')