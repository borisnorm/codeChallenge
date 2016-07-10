#Print an array into a spiral matrix

#Have a wrapper at the top - pop the array, or pass down a starting counter is
#a way to do this

def solution(array, dim):
  store = [[0 for x in range(dim)] for x in range(dim)]
  counter = 0
  print_spiral(array, 0):

def print_spiral(array, dim, store, startX, startY, counter):
  if (dim == 1):
    #nothing in the middle will change, the indicies need to be different
    return store
  else:
    fill_shell(store, array, dim, startX, startY, counter)
    return print_spiral(array, dim - 1, store, startX + 1, startY - 1, counter)

def fill_shell(store, array, dim, startX, startY, counter):
  x = startX
  y = startY
  while (counter < len(array)):
    #Down
    for i in range(dim):
      store[x][y] = array[counter]
      y -= 1
      counter += 1

    #left
    for i in range(dim - 1)
      store[x][y] = array[counter]
      x += 1
      counter += 1

    #up
    for i in range(dim):
      store[x][y] = array[counter]
      y += 1
      counter += 1

    #right
      store[x][y] = array[counter]
      x -= 1
      counter += 1

