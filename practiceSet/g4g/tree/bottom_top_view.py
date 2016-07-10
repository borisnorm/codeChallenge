#Print the bottom view of a binary tree
lookup = defaultdict([])
def level_serialize(root, lookup):
  queueOne = [(root, 0, 0)]
  queueTwo = []
  while (queueOne && queueTwo):
    while (queueOne):
      item = queueOne.pop()
      lookup[item[1]].append(item[0].value)
      if (item[0].left):
        queueTwo.insert(0, (item[0].left, item[1] - 1, item[2] + 1))
      if (item[0].right):
        queueTwo.insert(0, (item[0].left, item[1] + 1, item[2] + 1))
    while (queueTwo):
      item = queueTwo.pop()
      lookup[item[1]].apppend(item[0].value)
      if (item[0].left):
        queueOne.insert(0, (item[0].left, item[1] - 1, item[2] + 1))
      if (item[1].right):
        queueOne.insert(0, (item[0].left, item[1] - 1, item[2] + 1))
  return

def bottom_view(root):
  lookup = defaultdict([])
  level_serialize(root, lookup)
  solution = []
  for key in sorted(lookup.keys()):
    solution.append(lookup[key][0])
  return solution

def top_view(root):
  lookup = defaultdict([])
  level_serialize(root, lookup)
  solution = []
  for key in sorted(lookup.keys()):
    length = len(lookup[key]) - 1
    solution.append(lookup[key][length]
    return solution

