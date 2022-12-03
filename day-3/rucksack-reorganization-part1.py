# a-z 1-26
# A-Z 27-52
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def conv(a):
  prs = set()
  for i in a:
    prs.add(alpha.index(i)+1)
  return prs

points = 0
for line in open("input.txt").read().splitlines():
  c1 = conv(line[0:int(len(line)/2)])
  c2 = conv(line[int(len(line)/2):])
  prs = sum(c1 & c2)
  points+=prs
  print(c1,c2,prs)

print(points)
