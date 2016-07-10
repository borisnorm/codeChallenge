#Select random number from a linked list
def random_once(llist):
  length = 0
  pointer = llist.head
  while pointer is not None:
    length += 1
    pointer = pointer.next
  rand_index = Math.random(length)
  counter = 0
  pointer = llist.head
  while counter < rand_index:
    pointer = pointer.next
    counter += 1
  return pointer.value


#Repeated usage
def random_again(llist):
  list = []
  pointer = llist.head
  while pointer is not None:
    list.append(pointer)
    pointer = pointer.next
  return list

def random(stored_list):
  random = Math.random(len(stored_list) - 1)
  return store_list[random]


