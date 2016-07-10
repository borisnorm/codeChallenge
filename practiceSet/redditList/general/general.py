#Find most frequent integer in an array
from collections import defaultdict
def freq(array):
  max = 0
  #Make sure that this is zero
  freqDict = defaultdict(0)
  for i in range(len(array)):
    freqDict[array[i]] += 1
  for key in freqDict.keys():
    if freqDict[keys] > max:
      max = freqDict[keys]
  return max

#Return list of intergers where sum 10
def sum10(array, target):
  solution = []
  lookup = set()
  for i in range(len(array)):
    lookup.add(array[i])
  for i in range(len(array)):
    if (target - array[i]) in lookup:
      solution.append(target - array[i], array[i])
  return solution

#Fibbonacci
def fibr(n, tracker):




def fibDP(n):
























