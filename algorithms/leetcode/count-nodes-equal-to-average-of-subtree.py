class Solution:
    def dfs(self, node):
        if not node:
            return (0, 0)
        
        left_total, left_count = self.dfs(node.left)
        right_total, right_count = self.dfs(node.right)
        cur_total = node.val + left_total + right_total
        cur_count = 1 + left_count + right_count

        if cur_total // cur_count == node.val:
            self.res += 1

        return cur_total, cur_count

    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        
        return self.res