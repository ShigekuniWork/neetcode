class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
        self.count = n
    
    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
    
    def union(self, n1, n2):
        root1 = self.find(n1)
        root2 = self.find(n2)

        if root1 == root2:
            return False
        
        if self.ranks[root1] > self.ranks[root2]:
            self.parents[root2] = root1
        elif self.ranks[root1] < self.ranks[root2]:
            self.parents[root1] = root2
        else:
            self.parents[root1] = root2
            self.ranks[root2] += 1

        self.count -= 1
        return True

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        union_find = UnionFind(n)

        for u, v in edges:
            if not union_find.union(u, v):
                return False
        
        return True