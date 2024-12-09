with open("./input", "r") as f:
    data = f.read().strip()


def dfs(nums, d, cur, tv):
    if d == len(nums):
        return cur == tv
    sum = cur + nums[d]
    prod = nums[d] if d == 0 else nums[d] * cur
    return dfs(nums, d + 1, sum, tv) or dfs(nums, d + 1, prod, tv)


def solve1():
    sum = 0
    for line in data.split("\n"):
        tvs, arrs = line.split(":")
        tv = int(tvs)
        nums = [int(n) for n in arrs.strip().split(" ")]

        if dfs(nums, 0, 0, tv):
            sum += tv
    return sum


print(f"part one: {solve1()}")


def dfs2(nums, d, tv, acc):
  if d == len(nums):
      return acc == tv
  sum = acc + nums[d]
  prod = nums[d] if d == 0 else nums[d] * acc
  concat = nums[d] if d == 0 else int(str(acc) + str(nums[d]))
  return dfs2(nums, d+1, tv, sum) or dfs2(nums, d+1, tv, prod) or dfs2(nums, d+1, tv, concat)

def solve2():
    sum = 0
    for line in data.split("\n"):
        tvs, arrs = line.split(":")
        tv = int(tvs)
        nums = [int(n) for n in arrs.strip().split(" ")]
        if dfs2(nums, 0, tv, 0):
            sum += tv
    return sum


print(f"part two: {solve2()}")
