#Reverse reverse then add back in
def s_rev(string, alphabet):
  string_builder = ""
  for i in range(len(string)):
    if string[i] in alphabet:
      string_builder += string[i]

  rev = string_builder[::-1]
  rev_counter = 0
  for j in range(len(string)):
    if string[j] in alphabet:
      string[j] = rev[rev_counter]
      rev_counter += 1
  return string

