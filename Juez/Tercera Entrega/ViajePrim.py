class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)
        if rootX != rootY:
            if self.rank[rootX] > self.rank[rootY]:
                self.parent[rootY] = rootX
            elif self.rank[rootX] < self.rank[rootY]:
                self.parent[rootX] = rootY
            else:
                self.parent[rootY] = rootX
                self.rank[rootX] += 1
            return True
        return False

def kruskal(n, edges):
    uf = UnionFind(n)
    mst_max_edge = 0
    edges.sort(key=lambda x: x[2])

    for h1, h2, d in edges:
        if uf.union(h1, h2):
            mst_max_edge = max(mst_max_edge, d)

    return mst_max_edge

# Entrada
N, M = map(int, input().split())
edges = []

for _ in range(M):
    H1, H2, D = map(int, input().split())
    edges.append((H1, H2, D))

# Salida
print(kruskal(N, edges))
