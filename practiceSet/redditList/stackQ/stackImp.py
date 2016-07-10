#Implement a Stack

class Stack:

  def __init__(self):
    self.stack = []
    self.size = 0

  def push(self, value):
    self.stack.insert(0, value):
    self.size += 1

  def pop(self):
    if len(self.stack) == 0:
      return "empty"
    else:
      self.size -= 1
      return self.stack.pop(0)

