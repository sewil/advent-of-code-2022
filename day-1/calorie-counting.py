inventories = []
for inv in open("input.txt").read()[:-1].split('\n\n'):
  inventories.append(sum(map(int, inv.split('\n'))))
inventories.sort(reverse=True)
print(sum(inventories[0:3]))
