class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        graph = defaultdict(list)

        @cache
        def dfs(node):
            nx = 0

            for neighbor in graph[node]:
                nx = max(nx, dfs(neighbor))

            return time[node] + nx

        for n1, n2 in relations:
            graph[n1-1].append(n2-1)

        res = 0
        for node in range(n):
            res = max(res, dfs(node))

        return res
