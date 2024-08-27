class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        heap = []
        adj = defaultdict(list)
        for e in range(len(edges)):
            adj[edges[e][0]].append((succProb[e], edges[e][1]))
            adj[edges[e][1]].append((succProb[e], edges[e][0]))

        heapq.heappush(heap, (-1, start_node))
        distance = [0]*n
        distance[start_node] = 1
        while heap:
            d, n = heapq.heappop(heap)
            d*=-1
            if n == end_node:
                return d
            for neb in adj[n]:
                dn, nn = neb
                if dn*d > distance[nn]:
                    distance[nn] = dn*d
                    heapq.heappush(heap, (-distance[nn], nn))
        return 0


        
