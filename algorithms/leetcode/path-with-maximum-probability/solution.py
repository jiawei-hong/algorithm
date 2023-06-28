class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = defaultdict(dict)

        for [src, dst], prob in zip(edges, succProb):
            graph[src][dst] = graph[dst][src] = prob

        q = [(-1, start)]
        v = set()

        while q:
            prob, node = heapq.heappop(q)

            if node == end:
                return -prob

            if node in v:
                continue

            v.add(node)

            for neighbor in graph[node]:
                neighbor_prob = graph[node][neighbor]
                heapq.heappush(q, (
                    prob * neighbor_prob,
                    neighbor
                ))

        return 0