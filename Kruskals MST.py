class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n  # Added rank to keep the tree flat
    
    def find(self, x):
        # Path compression: points node directly to the root
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        
        if xroot == yroot:
            return False
        
        # Union by Rank: Attach smaller depth tree under root of higher depth tree
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
            
        return True

def kruskal_mst(edges, n):
    # Sort edges based on weight: O(E log E)
    edges.sort(key=lambda x: x[2])
    
    ds = DisjointSet(n)
    mst = []
    total_weight = 0

    for u, v, weight in edges:
        # If u and v are not in the same set, add edge to MST
        if ds.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight
            
        # Optimization: Stop if we have n-1 edges
        if len(mst) == n - 1:
            break

    return mst, total_weight

# --- Execution ---
edges = [
    (0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11),
    (2, 3, 7), (2, 8, 2), (2, 5, 4), (3, 4, 9),
    (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1),
    (6, 8, 6), (7, 8, 7)
]

n = 9 
mst, total_weight = kruskal_mst(edges, n)

print("### Minimum Spanning Tree Edges ###")
for u, v, weight in mst:
    print(f"Edge ({u}, {v}) \t Weight: {weight}")

print("-" * 30)
print(f"Total MST Weight: {total_weight}")