from collections import defaultdict, deque
from itertools import count
from math import lcm, prod

with open("input") as f:
  ws = [l.split() for l in f.read().strip().replace(",", "").split("\n")]

flips = {w[1:] for w, *_ in ws if w[0] == "%"}

parents = defaultdict(dict)
children = defaultdict(list)

for w, _, *regs in ws:
  for reg in regs:
    parents[reg][w.strip("&%")] = False
    children[w.strip("&%")].append(reg)


def press(states, sent, periods, i):
  q = deque([('broadcaster', 'button', False)])

  def send(sender, signal):
    for c in children[sender]:
      q.append((c, sender, signal))

  while q:
    receiver, sender, signal = q.popleft()
    sent[signal] += 1
    if receiver == 'broadcaster':
      send('broadcaster', signal)
    elif receiver in flips:
      if not signal:
        states[receiver] = not states[receiver]
        send(receiver, states[receiver])
    else:
      if signal and receiver == 'tg' and sender not in periods:
        periods[sender] = i
      parents[receiver][sender] = signal
      send(receiver, not all(parents[receiver].values()))

  return states, sent, periods


# part one
states = defaultdict(bool)
sent = defaultdict(int)
for _ in range(1000):
  states, sent, _ = press(states, sent, {}, 0)
print(prod(sent.values()))

# part two
states = defaultdict(bool)
sent = defaultdict(int)
periods = {}
for i in count(1):
  states, _, periods = press(states, sent, periods, i)
  if len(periods) == 4:
    print(lcm(*periods.values()))
    break