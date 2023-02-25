from collections import deque

# define the graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs_shortest_path(graph, start, end):
    # initialize the queue with the start node
    queue = deque([(start, [start])])
  
    # continue until the queue is empty
    while queue:
        # get the next node and path
        node, path = queue.popleft()

        # if we have found the end node, return the path
        if node == end:
            return path

        # add all adjacent nodes to the queue
        for adjacent in graph.get(node, []):
            # only add nodes that haven't been visited yet
            if adjacent not in path:
                queue.append((adjacent, path + [adjacent]))

    # if no path exists, return None
    return None

# example usage
path = bfs_shortest_path(graph, 'A', 'F')
print(path)  # output: ['A', 'C', 'F']
