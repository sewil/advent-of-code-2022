import re
def get_range(rangestr):
  m = re.search("(\d+)-(\d+)", rangestr)
  return set(range(int(m.group(1)), int(m.group(2))+1))
points=0
with open("input.txt") as f:
  lines = f.read().splitlines()
  for line in lines:
    ranges = line.split(',')
    range1 = get_range(ranges[0])
    range2 = get_range(ranges[1])
    intrs = range1&range2
    c = len(intrs) > 0
    if c: points+=1
    print(ranges, intrs, c)
print(points)
