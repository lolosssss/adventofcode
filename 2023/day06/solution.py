import re

with open('./input', 'r') as f:
  data = f.read()

lines = data.split('\n')
pairs = list(zip(
  map(int, re.split(r'[: ]+', lines[0])[1:]),
  map(int, re.split(r'[: ]+', lines[1])[1:]),
))

result = 1

for pair in pairs:
  time, distance = pair
  cnt = 0
  t = 1
  while t < time:
    if t * (time - t) > distance:
      cnt += 1
    t += 1
  result *= cnt

print(result)

# part two
time = int(lines[0].replace(' ', '').split(':')[1])
distance = int(lines[1].replace(' ', '').split(':')[1])

cnt = 0
t = 1
while t < time:
  if t * (time - t) > distance:
    cnt += 1
  t += 1

print(cnt)