#print all the permutations of a string

def perm_string(prefix, string):
  if len(string) == 1:
    print (prefix + string)
    return prefix + string
  else:
    for i in range(len(string)):
      #everything except for the added term?
      #draw it out, you need to include the rest of the stuff<F12>
      #car, c, ar vs a, cr, r, ca - you need to include everything except the slot
      #or else you will drop things
      perm_string(prefix + string[i], string[:i] + string[i+1:])

perm_string("", 'ryan')











