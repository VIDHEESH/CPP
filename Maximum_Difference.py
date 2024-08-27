import heapq
from typing import List

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        # Create adjacency list
        graph = [[] for _ in range(n)]
        for (a, b), prob in zip(edges, succProb):
            graph[a].append((b, prob))
            graph[b].append((a, prob))
        
        # Initialize probabilities
        probs = [0] * n
        probs[start] = 1
        
        # Max heap for Dijkstra's algorithm
        pq = [(-1, start)]
        
        while pq:
            prob, node = heapq.heappop(pq)
            prob = -prob
            
            if node == end:
                return prob
            
            if prob < probs[node]:
                continue
            
            for neighbor, edge_prob in graph[node]:
                new_prob = prob * edge_prob
                if new_prob > probs[neighbor]:
                    probs[neighbor] = new_prob
                    heapq.heappush(pq, (-new_prob, neighbor))
        
        return 0
