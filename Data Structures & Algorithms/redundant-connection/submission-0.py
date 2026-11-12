class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = list(range(n+1)) #if n == 3, parent = [0, 1, 2, 3]
        size = [1] * (n+1) # size = [1, 1, 1, 1]

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node]) # path compression
            return parent[node]

        def union(a, b):
            root_a = find(a)
            root_b = find(b)
            if root_a == root_b:
                return False
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a
            parent[root_b] = root_a
            size[root_a] += size[root_b]
            return True

        for a, b in edges:
            if not union(a, b):
                return [a, b]
        return []