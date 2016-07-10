#Find distance between two nodes in a regular binary Tree

#This should be good in a BT
def search_height(root, target, distance):
  if root is None:
    return 0
  if (root == target):
    return distance
  search(root.left, target, distance + 1)
  search(root.left, target, distance + 1)

#At every root in the Tree, run the search for both, and return the min distance where both are found
def find_dist(root, keyOne, keyTwo, distance):
  if root is None:
    return
  else:
    searchOne = search_height(root, keyOne, distance)
    searchTwo = search_height(root, keyTwo, distance)
    if (searchOne > 0 or searchTwo > 0):
      if (searchOne + searchTwo < distance)
        distance = searchOne + searchTwo
    find_dist(root.left, keyOne, keyTwo, distance)
    find_dist(root.right, keyOne, keyTwo, distance)

def solution(root, keyOne, keyTwo):
  distance = 100000
  find_dist(root, keyOne, keyTwo, distance)
  return distance


