from collections import defaultdict

#I make sure words are flush, distribute extra spaces event between words on a line
#I need to assume that this is possible, or else the input will be invalid
def print_justify(inputString, maxWidth):
  #initalize default dict to store the item
  table = defaultdict(list)
  lineLeftOver = {}
  line = 0
  lineCounter = maxWidtth
  #Turn string into an array of words I can work with
  words = inputString.split()
  for i in range(0, len(words)):
    leftOver = lineCounter - len(words[i]) + 1
    if leftOver > 0:
      #We are at our last word
      if leftOver - len(words[i + 1]) < 0:
        #default dict to preinitzlize
        table[line].append(word[i])
        lineLeftOver[line] = leftOver
        line += 1
        lineCounter = maxWidth

  #With processing print all of the lines in order
  for i in range(0, line):
    #default space is 1 - anything ontop of that is extra
    extraSpace = lineLeftOver[i] / len(table[i])
    string = ''
    for j in range(0, len(table[i])):
      string += table[i][j]
      for i in range(0, extraSpace):
        string += ' '
    print string




























