#Implement a stack with push and pop

class Queue:

  def __init__(self):
    self.queue = []
    size = 0

  def push(self, value):
    self.queue.append(value)
    self.size += 1

  def pop(self):
    if len(self.stack) is 0:
      return "Nothing"
    else:
      self.size -= 1
      return self.queue.pop(0)


