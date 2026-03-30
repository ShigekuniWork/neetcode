class UnionFind:
    def __init__(self, n: int):
        self.parents = list(range(n))
        self.rank = [0] * n
        self.count = n

    def find(self, x: int):
        if self.parents[x] != x:
            self.parents[x] = self.find(self.parents[x])
        
        return self.parents[x]
    
    def union(self, u :int, v:int):
        root1 = self.find(u)
        root2 = self.find(v)

        if root1 == root2:
            return
        
        if self.rank[root1] > self.rank[root2]:
            self.parents[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parents[root1] = root2
        else:
            self.parents[root1] = root2
            self.rank[root2] += 1

        self.count -= 1

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_find = UnionFind(n)

        for u, v in edges:
            union_find.union(u, v)

        return union_find.count
        