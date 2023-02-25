# bfspython
here's an example of the iterative implementation of BFS using a queue in Python:
Here, we start with a start node and create a queue using deque from the collections module. We also create a visited set to keep track of the nodes that have already been visited.

We then start a loop and dequeue a vertex from the queue. We print the vertex and then add all its adjacent vertices to the queue if they haven't already been visited. We keep doing this until the queue is empty.
