class DisjoinstSet:

#This does assume its in the set
#We should use a python dictionary to create this
  def __init__(self, size):
    #Make sure these are default dicts to prevent the key error?
    self.lookup = {}
    self.rank = {}
    self.size = 0

  def add(self, item):
    self.lookup[item] = -1

  #Union by rank
  def union(self, itemOne, itemTwo):
    rankOne = find_rank(itemOne)
    rankTwo = find_rank(itemTwo)
    if rankOne >= rankTwo:
      self.lookup[itemOne] = find(itemTwo)
      self.rank[itemTwo] += 1
      return
    self.lookup[itemTwo] = find(itemOne)
    self.lookup[itemOne] = self.lookup[itemTwo]
    return

  #Find Rank
  def find_rank(self, item):
    return self.rank[item]

  #Find the parent set
  def find(self, item):
    pointer = self.lookup[item]
    while (pointer != -1):
      if (self.lookup[pointer] == -1):
        return pointer
      pointer = self.lookup[pointer]
    return pointer


