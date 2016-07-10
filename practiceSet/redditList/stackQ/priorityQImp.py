#Priority Queue - this is implemented as an array

class PriorityQueue:

  def __init__(self, size):
    self.array = [None for x in range(size)]
    self.lookup = {}
    self.rightmost = 0
    self.size = 0

  def find_min(self):
    return self.array[1]

  def pop_min(self):
    temp = self.array[1]
    self.array[1] = self.array[rightmost]
    #Swap with your larger child
    pointer = 1
    leftChild = self.array[2 * pointer]
    rightChild = self.array[2 * pointer + 1]
    if leftChild >= rightChild:
      self.array[pointer], self.array[2 * pointer] = self.array[2 * pointer], self.array[pointer]
      pointer = 2 * pointer
    else:
      self.array[pointer], self.array[2 * pointer + 1] = self.array[2 * pointer + 1], self.array[pointer]
      pointer = 2 * pointer + 1
    return temp

  def insert(self, key, value):
    if self.array[1] is None:
      self.array[1] = key
      self.lookup[key] = value
      self.rightmost = 1
    else:
      self.array[rightmost + 1] = key
      self.rightsost += 1
      self.lookup[key] = value
      pointer = rightmost
      while (self.array[pointer] > self.array[pointer/2]):
        self.array[pointer], self.array[pointer/2] = self.array[pointer/2], self.array[pointer]
        pointer = pointer/2
      return

  #Update the weights
  def update(self, key, newValue):















