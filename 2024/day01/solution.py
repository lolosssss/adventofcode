with open('./input', 'r') as f:
  data = f.read().strip()

lines = data.split('\n')

# split left and right list to seperate list
left_list = []
right_list = []

for line in lines:
  left, right = line.split('   ')
  left_list.append(int(left))
  right_list.append(int(right))

left_list.sort()
right_list.sort()

# part one
def solve1():
  sum = 0
  for i in range(0, 1000):
    dis = abs(left_list[i] - right_list[i])
    sum += dis
  print(sum)


# part two
def solve2():
  sum = 0
  idx = 0
  count = 0
  for i in range(0, 1000):
    while (idx < 1000 and right_list[idx] < left_list[i]):
      idx += 1
    while (idx < 1000 and right_list[idx] == left_list[i]):
      idx += 1
      count += 1
    sum += left_list[i] * count
    if idx > 1000:
      break
    count = 0
  print(sum)

solve1()
solve2()
