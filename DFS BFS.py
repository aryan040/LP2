# Depth First Search using recursion

graph={
    'A':['B','C'],
    'B':['D','E'],
    'C':['F'],
    'D':[],
    'E':[],
    'F':[]
}

visited=set()

def dfs(node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        
        for neighbour in graph[node]:
            dfs(neighbour)
            
print("DFS Traversal: ")
dfs('A')

# Breadth First Search

from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

visited = []
queue = deque()

def bfs(node):
    visited.append(node)
    queue.append(node)
    
    # The while loop starts here
    while queue:
        s = queue.popleft()
        print(s, end=" ")
        
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

print("\nBFS Traversal: ")
bfs('A')