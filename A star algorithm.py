graph = {
    'A': [('B', 1),('C', 3)],
    'B': [('D', 3),('E', 1)],
    'C': [('F', 5)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 1,
    'F': 0
}

open_list = ['A']
closed_list = []
g = {'A' : 0}
parent = {'A': 'A'}

while open_list:
    n=None
    
    for v in open_list:
        if n is None or g[v] + heuristic[v] < g[n] + heuristic[n]:
            n = v
            
    if n == 'F':
        path = []

        while parent[n] != n:
            path.append(n)
            n=parent[n]
            
        path.append('A')
        path.reverse()
        
        print("Path Found:",path)
        break
    
    for(m,weight) in graph[n]:
        if m not in open_list and m not in closed_list:
            open_list.append(m)
            parent[m] = n
            g[m] = g[n] + weight
            
    open_list.remove(n)
    closed_list.append(n)