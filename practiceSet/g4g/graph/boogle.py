#Given a 2D array, word board find all of the words in the board

#I need a better lookup
def getNeighbors(graph, x, y):
  neighbors = []
  for i in range (x - 1, x + 2):
    for j in range(y - 1, x + 2):
      if i > 0 and j > 0 and i < len(matrix) and j < len(matrix):
        if (i != x) and (j != y):
          neighbors.append(graph[i][j])
  return neighbors

#Must have an is word function
def boogle(board):
  word_bank = []
  for i in range(len(board)):
    for j in range(len(board)):
      #initalize a word search here
      visited = set()
      word_search(board[i][j], visited, path, word_bank)
  return word_bank

#We need to do DFS recursively, path is a string we add every time, find a way to stop the DFS
def word_search(source, visited, path, word_bank):
  #Stop condition
  if is_word(path):
    for char in path:
      visited.append(char)
      return True
  #Stop condition
  if len(visited) >= len(graph):
    return
  #Recursive propogation
  for char in getNeighbors(source):
    if char not in visited:
      word_search(char, visisted.add(item), path += char, word_bank)

