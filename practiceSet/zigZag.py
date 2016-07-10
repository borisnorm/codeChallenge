#zigZag given a hieght/width print the zigzag version of a string

def zigZag(array, height):
  rowSize = len(array) / height
  store = [[0 for x in range(rowSize)] for x in range(height)]
  counter = 0
  xPosition = 0
  yPosition = height - y
  while len(array) > counter:
    #Down
    for i in range(height):
      yPosition -= 1
      store[xPosition][yPosition] = array[counter]
      counter += 1
    #Zig
    for i in range(height - 2):
      yPosition += 1
      xPosition += 1
      store[xPosition][yPosition] = array[counter]
      counter += 1
    #Up
    for i in range(height):
      yPosition += 1
      store[xPosition][yPosition] = array[counter]
      counter += 1

  #Processed them into a store now print the store
  for i in range(len(store)):
    print ''.join(store[i])

  return

