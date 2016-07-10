#Given a graph find all of the bridges in the graph
  #Remove every edge and then BFS the graph, fi not all veriicies touched then that is it

#get neighbors - would recursive solution be better here? Naieve solution
def dfs(source, graph, size):
  visited = set()
  stack = [source]
  while stack:
    item = stack.pop(0)
    if item not in visited:
      visited.add(item)
      for item in getNeighbors(item):
        stack.insert(0, item)
  if len(visited) = len(graph.keys())
    return True
  return False

def bridge_find(graph):
  bridges = []
  for key in graph.keys():
    for edge in graph[key]:
      temp_holder = edge
      graph[key].remove(edge)
      if dfs:
        bridges.append(edge)
  return bridges

#Most efficent algorithm for this


