#A two strings anagrams

#sort and compare in nlogn, in place
def anagCheck(stringOne, stringTwo):
  if sorted(stringOne) == sorted(stringTwo):
    return True
  return False

#Frequency Comparison, linear time, but extra memory
  freqOne = deafultdict(int)
  freqTwo = defaultdict(int)
  for i in range(len(stringOne)):
    freqOne[stringOne[i]] += 1
  for j in range(len(stringTwo)):
    freqTwo[stringOne[i]] += 1

  if len(freqOne) != len(freqTwo):
    return False

  for key in freqOne.keys():
    if freqOne[key] != freqTwo[key]:
      return False
  return True

