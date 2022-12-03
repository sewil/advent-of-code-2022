# Rock = A (opponent), X (you), 1 point
# Paper = B (opponent), Y (you), 2 points
# Scissors = C (opp), Z (you), 3 points

# Win = 6 points
# Draw = 3 points
# Lose = 0 points
def conv(c):
  if c == 'A' or c == 'X': return 0
  elif c == 'B' or c == 'Y': return 1
  elif c == 'C' or c == 'Z': return 2

f = open("input.txt", "r")
points=0
for line in f.readlines():
  cs = line[:-1].split(' ')
  a = conv(cs[0])
  b = conv(cs[1])
  if b == 0: # Lose
    me = (a-1)%3
  elif b == 1: # Tie
    me = a
    points += 3
  else:
    me = (a+1)%3
    points += 6
  points += me+1

print(points)
