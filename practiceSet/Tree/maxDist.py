#Running time will be n2
def height(root, height = 0)
  if root is None:
    return height
  return max(height(root.left, height + 1), height(root.right, height + 1))

def maxDist(root, maxDist):
  if root is None:
    return 0
  else:
    dist = height(root.left, 0) + height(root.right, 0)
    if dist > maxDist:
      maxDist = dist
    maxDist(root.left, maxDist)
    maxDist(root.right, maxDist)

def solution(root):
  maxDist = 0
  maxDist(root, maxDist)
  return maxDist





