# a-z 1-26
# A-Z 27-52
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def conv(a):
  prs = set()
  for i in a:
    prs.add(alpha.index(i)+1)
  return prs

points = 0
with open("input.txt") as f:
  lines = f.read().splitlines()
  for i in range(0, len(lines), 3):
    e1 = conv(lines[i])
    e2 = conv(lines[i+1])
    e3 = conv(lines[i+2])
    badge = sum(e1 & e2 & e3)
    points += badge
    print('group', (i/3)+1,e1,e2,e3,badge)

print(points)
