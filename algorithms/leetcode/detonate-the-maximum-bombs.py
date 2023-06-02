class Solution:
    def dfs(self, graph, v, i):
        for node in graph[i]:
            if node not in v:
                v.add(node)
                self.dfs(graph, v, node)

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        graph = [[] for _ in range(n)]
        
        for i in range(n):
            x, y, scope = bombs[i]
            for j in range(n):
                if i != j:
                    xx, yy = bombs[j][0], bombs[j][1]
                    xx, yy = (xx-x) ** 2, (yy-y) ** 2

                    between_two_point = (xx + yy)
                    boom_scope = scope ** 2

                    if between_two_point <= boom_scope:
                        graph[i].append(j)

        ans = -(2 ** 31)
        for i in range(n):
            v = set([i])
            self.dfs(graph, v, i)

            ans = max(ans, len(v))

        return ans