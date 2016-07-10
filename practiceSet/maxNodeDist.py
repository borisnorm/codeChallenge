#Res is a heap try to find out how to use a heap, by defauly this is a min, heap
#insert by -1 to turn it into a max heap
#h = []
#heappush(h, )
#heappop(h,  )

#The res parameter seems to be needed to store things that are happening
def max_dist(root, result):
  if root is None:
    return 0
  #Find the max value of any rooted subtree at this point
  left = max_dist(node.left)
  right = max_dist(node.right)
  #Check if root passes through you
  passNode = max(max(l, r) + node.value, node.value)
  #check if this passes throught the value
  max_value = max(passNode, node.value + l + r)
  result.add(max_value):
  #I might just be able to return max - value with a res - maybe not because this is based in the root, just tells you about its subtree?
  return max_value #this might not be needed

def max_solution(root):
  #res = heap()
  max_dist(root, res)
  return res.max


