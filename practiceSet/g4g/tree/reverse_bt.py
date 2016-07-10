#Reverse alternate levels of a bt
#It is a if the row reading was sorted, and flipped
#Level order the tree and reverse the queue, is there another way to do this?
#recursively, swap the left left, with the right right for every other node, tree is full so no null
#I dont think there is a recursive solution


def reverse_queue(queue):
  temp = []
  for item in queue:
    temp.append(item.value)
  lo = 0
  hi = len(temp) - 1
  while (lo < hi):
    temp[lo], temp[hi] = temp[hi], temp[lo]
    lo += 1
    hi -= 1
  return temp

def reverse_alt(root):
  reverse = False
  queueOne = [root]
  queueTwo = []

  while (queueOne):
    item = queueOne.pop()
    if item.left != None:
      queueTwo.insert(0, item.left)
    if item.right != None:
      queueTwo.insert(0, item.right)

  #Just added to queueTwo - swap the entries in the level
  reverse = !reverse
  if (reverse):
    reverse = reverse_queue(queueTwo)
    for i in range(len(queueTwo)):
      queueTwo[i].value = reverse[i]

  while (queueTwo):
    item =  queueTwo.pop()
    if item.left != None:
      queueOne.insert(0, item.left)
    if item.right != None:
      queueTwo.insert(0, item.right)

  #just added to queueOne - swap the entries in the level
  reverse = !reverse
  if (reverse):
    reverse = reverse_queue(queOne)
    for i in range(len(queueOne)):
      queueOne.value = reverse[i]

def solution_driver(tree):
  reverse_alt(tree.root)
  return tree

