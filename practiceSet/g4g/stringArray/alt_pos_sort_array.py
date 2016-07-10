#Gen all possible sorted arrays from alternate
#elements of two given sorted arrays
#Must Start with array a, end with b

def pos_sorted(arrayOne, arrayTwo):
  solution = []
  startIndexOne = 0
  while startIndexOne < len(arrayOne):
    indexOne = startIndexOne
    indexTwo = 0
    answer = [arrayOne[indexOne]]
    while indexOne < len(arrayOne) and indexTwo < len(arrayTwo):

      while arrayTwo[indexTwo] < arrayOne[indexOne]:
        indexTwo += 1
      answer.append[indexTwo]
      solution.append(answer)

      while arrayOne[indexOne] < arrayTwo[indexTwo]:
        indexOne += 1
      answer.append[indexOne]
      solution.append(answer)

    startIndexOne += 1
    return solution


