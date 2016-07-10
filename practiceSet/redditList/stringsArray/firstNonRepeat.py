#Find the first non repeated char in a string

def nonRepeat(string):
  lookup = defaultdict(int)
  for i in range(len(string)):
    lookup[string[i]] += 1
  for j in range(len(string)):
    if lookup[string[j]] < 2:
      return lookup[string[j]]
  return ""


