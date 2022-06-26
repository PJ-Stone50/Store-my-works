import collections

#BFS Queue Concept (First-in & First-out)
def bfs(graph, root):
  # global visited
  visited, queue = set(), collections.deque([root])
  visited.add(root)

  # Dequeue a vertext from queue ("S")
  while queue:
    vertex = queue.popleft()
    print(str(vertex) + " ", end="")

    for V in graph[vertex]:
      if V not in visited:
        visited.add(V)
        queue.append(V)



graph = {'S': set(['A','B','C']),
        'A': set(['S','D']),
        'B': set(['S','E']),
        'C': set(['F','S'])}

print("")
bfs(graph,'S')

