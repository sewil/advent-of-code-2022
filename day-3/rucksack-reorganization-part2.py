import functools
# a-z 1-26
# A-Z 27-52
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
points = 0
with open("input.txt") as f:
  lines = f.read().splitlines()
  for i in range(0, len(lines), 3):
    group = lines[i:i+3]
    badge_c = functools.reduce(lambda a,b: set(a) & set(b), group).pop()
    badge = alpha.index(badge_c)+1
    points += badge
    print('group',int(i/3)+1)
    print('\n'.join(group))
    print(badge_c, badge, "\n")

print(points)
