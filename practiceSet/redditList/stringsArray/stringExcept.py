#Reverse a string without touching special characters

#Remove, reverse and then put back in there, just straight up ignore them
  #Reinsert them walk through mixed up array,
  #and original array at same time, if you encounter a char in the orignal array
  #keep that there and continue adding things

def special_reverse(string, special_char_set):
  holder = []
  solution = []
  for i in range(len(string)):
    if string[i]) not in special_char_set):
      holder.append(string[i])
  reverse = holder[::-1]

  for i in range(len(string)):
    if string[i] not in special_char_set:
      soluion.append(reverse.pop(0))
    solution.append(string[i])

  return solution


















