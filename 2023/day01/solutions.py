import re

with open('./input', 'r') as f:
  data = f.read().strip()


def calibration(data):
  lines = data.split('\n')
  nums = [re.findall('\d', line) for line in lines]
  return sum((int(n[0] + n[-1])) for n in nums)

print(calibration(data))

"""
将单词替换成数字
需要保持原单词前后连续，防止因为替换顺序引起的错误，例如：
  twonenineight
如仅将单词替换成数字，会变成：
  tw1nin8
正确情况应该是：
  2nenin8
即 28
"""
data = (
  data
    .replace('one', 'one1one')
    .replace('two', 'two2two')
    .replace('three', 'three3three')
    .replace('four', 'four4four')
    .replace('five', 'five5five')
    .replace('six', 'six6six')
    .replace('seven', 'seven7seven')
    .replace('eight', 'eight8eight')
    .replace('nine', 'nine9nine')
)

print(calibration(data))
