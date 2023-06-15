class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        res, mx, level = 0, -(2 ** 31 + 1), 1
        queue = [root]

        while queue:
            nodes = []
            cur_level_sum = 0

            for node in queue:
                cur_level_sum += node.val
                if node.left:
                    nodes.append(node.left)
                if node.right:
                    nodes.append(node.right)

            if cur_level_sum > mx:
                mx = cur_level_sum
                res = level

            level += 1
            queue = nodes

        return res