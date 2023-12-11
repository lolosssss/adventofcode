import re

with open('./input', 'r') as f:
  data = f.read()


def do_mapping(seed, map_arr):
  for map_item in map_arr:
    if seed in range(map_item[0], map_item[1] + 1):
      return seed - map_item[2]
  return seed

def calc_mapping(lines):
  rules = []
  for line in lines:
    dest, src, length = [int(x) for x in line.split(' ')]
    start = src
    end = src + length - 1
    diff = src - dest
    rules.append([start, end, diff])

  rules.sort(key=lambda x: x[0])
  return rules

def find_lowest_location_number(data):
  lines = data.split('\n')

  # seeds
  seeds = [int(x) for x in lines[0].replace(': ', ' ').split(' ')[1:]]

  # map
  seed_to_soil_map = calc_mapping(lines[3:31])
  soil_to_fertilizer_map = calc_mapping(lines[33:43])
  fertilizer_to_water_map = calc_mapping(lines[45:54])
  water_to_light_map = calc_mapping(lines[56:79])
  light_to_temperature_map = calc_mapping(lines[81:113])
  temperature_to_humidity_map = calc_mapping(lines[115:160])
  humidity_to_location_map = calc_mapping(lines[162:211])

  mappings = [
    seed_to_soil_map,
    soil_to_fertilizer_map,
    fertilizer_to_water_map,
    water_to_light_map,
    light_to_temperature_map,
    temperature_to_humidity_map,
    humidity_to_location_map
  ]

  locations = []
  for seed in seeds:
    res = seed
    for mapping in mappings:
      res = do_mapping(res, mapping)
    locations.append(res)

  return min(locations)

print(find_lowest_location_number(data))

# part two
def find_lowest_location_number_2(data):
  seeds_l, *blocks = data.split('\n\n')

  seeds_list = [int(x) for x in seeds_l.split(':')[1].strip().split(' ')]
  seeds = [(a, a + b) for a, b in list(zip(seeds_list[::2], seeds_list[1::2]))]

  for block in blocks:
    ranges = [list(map(int, line.split(' '))) for line in block.split('\n')[1:]]
    news = []
    while len(seeds) > 0:
      s, e = seeds.pop(0)
      for dest, src, length in ranges:
        os = max(src, s)
        oe = min(src + length , e)
        if os < oe:
          news.append((os - src + dest, oe - src + dest))
          if os > s:
            seeds.append((s, os))
          if oe < e:
            seeds.append((oe, e))
          break
      else:
        news.append((s, e))

    seeds = news
  return min(seeds)[0]

print(find_lowest_location_number_2(data))
