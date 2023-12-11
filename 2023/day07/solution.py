from collections import Counter

with open('./input', 'r') as f:
  data = f.read().strip()


def get_type_rank(cards):
  """
  five of a kind  - 7
  four of a kind  - 6
  full house      - 5
  three of a kind - 4
  two pair        - 3
  one pair        - 2
  high card       - 1
  """
  c = Counter(cards)
  counts = [0] if (jokers := c.pop("*", 0)) == 5 else sorted(c.values())
    # The most efficient use of a joker is always as the most common non-joker card
  counts[-1] += jokers
  match counts:
    case *_, 5:
      return 7
    case *_, 4:
      return 6
    case *_, 2, 3:
      return 5
    case *_, 3:
      return 4
    case *_, 2, 2:
      return 3
    case *_, 2:
      return 2
  return 1


def calc(data):
  pairs = [line.split(' ') for line in data.split('\n')]
  pairs = list(map(lambda pair: (pair[0], int(pair[1])), pairs))

  # sort
  new_pairs = [(get_type_rank(hand), *map('*23456789TJQKA'.index, hand), bid) for (hand, bid) in pairs]
  new_pairs.sort()
  sum = 0
  for rank, (*_, bid) in enumerate(new_pairs, 1):
    sum += rank * bid
  return sum

# part one
print(calc(data))

#part tow
print(calc(data.replace('J', '*')))


