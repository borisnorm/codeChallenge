#Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every directed edge uv, vertex u comes before v in the ordering

def top_sort(graph, source):
  sort_path = []
  size = len(graph.keys())
  visited = set()
  stack = [source]

  while len(visited) < size:
    item = stack.pop(0)
    sort_path.append(item)
    #There will be no cycles in this graph
    for node in getNeighbors(item):
      stack.insert(0, node)

  return sort_path


