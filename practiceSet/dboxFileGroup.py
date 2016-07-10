#Hash and disjoint set really dont make that much sense
#Hash can make sense under specific conditions

#returns an array of arrays
def fileGrouper(dataArray):
  fileDict = {}
  for i in range(0, len(dataArray)):
    item = dataArray[i]
    if (fileDict[item]):
      fileDict[item].append(item)
    else:
      fileDict[item] = [item]
  #return the nested list
  solution = []
  for keys in fileDict.keys():
    solution.append(fileDict[keys])
  return solution


























