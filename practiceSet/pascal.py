#print pascal's

def pascal(root, row):
  counter = 0
  array1 = [root]
  array2 = []

  while counter < row:
    print array1
    array2.append(1)
    for i in range(len(array1) - 1):
      if len(array1) > 1:
        array2.append(array1[i] + array1[i + 1])
    array2.append(1)
    array1 = []
    counter += 1

    print array2
    array1.append(1)
    for i in range(len(array2) - 1):
      if len(array2) > 1:
        array1.append(array2[i] + array2[i + 1])
    array1.append(1)
    array2 = []
    counter += 1

print pascal(1, 5)

