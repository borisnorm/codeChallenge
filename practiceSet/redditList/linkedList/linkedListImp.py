class ListNode:

  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None

class LinkedList:

  def __init__(self, value):
    self.sentinel(value)
    self.size = 0

  def find(self, value):
    pointer = self.sentinel.next
    while (pointer is not None):
      if pointer.value == value:
        return True
      pointer = pointer.next
    return False

  def insert(self, value):
    newNode = ListNode(value)
    newNode.prev = self.sentinel.prev
    newNode.next = self.sentinel
    self.sentinel.prev.next = newNode
    self.sentinel.prev = newNode

  def delete(self, value):
    pointer = self.sentinel.next
    while (pointer.value is not None):
      if (pointer.value = value):
        pointer.prev.next = pointer.next
        pointer.next.prev = pointer.prev
        pointer.next = None
        pointer.prev = None
        return True
      return False


