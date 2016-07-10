
def longestPal(stringArg):
  max_len = 1;
  for i in range(0, len(stringArg)):
    for j in range(i, len(stringArg)):
      if (isPalindrome(stringArg[i: j])):
         #I was not returning a descriptive integer something else should be different
         max_len = max(max_len, len(stringArg[i: j]));
      #Bad return statement because this max parenthesis was not closed
  return max_len;

def isPalindrome(string):
  start = 0;
  end = len(string) - 1;
  #Length string - 1
  while (start < end):
    #I should just be !=
    if string[start] != string[end]:
    #booleans should be caps
      return False;
    start = start + 1
    end = end - 1
  return True;


print isPalindrome("tacocat");
print longestPal("abcccddd");




















