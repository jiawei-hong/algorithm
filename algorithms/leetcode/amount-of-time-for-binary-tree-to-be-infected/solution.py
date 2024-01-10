class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        graph = defaultdict(list)

        def dfs(node, prev):
            if prev:
                graph[prev.val].append(node.val)
                graph[node.val].append(prev.val)
            if node.left:
                dfs(node.left, node)
            if node.right:
                dfs(node.right, node)

        dfs(root, None)

        res = -1
        seen = {start}
        queue = [start]

        while queue:
            t = []
            for q in queue:
                for node in graph[q]:
                    if node not in seen:
                        seen.add(node)
                        t.append(node)
            queue = t
            res += 1

        return res
