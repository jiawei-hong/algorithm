class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        self.res = []
        self.f(root)

        return self.res

    def f(self, node, height=0):
        if node is None:
            return

        if len(self.res) < height + 1:
            self.res.append(float('-infinity'))

        cur_val = self.res[height]
        if node.val > cur_val:
            self.res[height] = node.val

        self.f(node.left, height+1)
        self.f(node.right, height+1)
