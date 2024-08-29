class Solution:
    def removeStones(self, stones):
        # Union-Find with path compression
        parent = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                parent[rootY] = rootX

        # Initialize Union-Find for each stone
        for x, y in stones:
            if (x, 'r') not in parent:
                parent[(x, 'r')] = (x, 'r')  # 'r' for row
            if (y, 'c') not in parent:
                parent[(y, 'c')] = (y, 'c')  # 'c' for column
            # Union row and column nodes
            union((x, 'r'), (y, 'c'))

        # Count number of unique connected components
        unique_roots = {find(node) for node in parent}

        # Total stones minus number of connected components gives the number of stones we can remove
        return len(stones) - len(unique_roots)
