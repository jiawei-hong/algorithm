class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        level_nodes = []
        
        def dfs(node, level=0):
            if not node:
                return

            if len(level_nodes) == level:
                level_nodes.append([])

            dfs(node.left, level + 1)
            level_nodes[level].append(node.val)
            dfs(node.right, level + 1)

        dfs(root)

        nodes_sum = [sum(x) for x in level_nodes]
        m = max(nodes_sum)

        return 1 + nodes_sum.index(m)