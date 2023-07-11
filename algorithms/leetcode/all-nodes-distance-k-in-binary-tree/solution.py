class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def buildParent(node, parent = None):
            if node:
                node.parent = parent
                buildParent(node.left, node)
                buildParent(node.right, node)

        buildParent(root)
        res = []
        v = set()
        
        def dfs(node, distance):
            if not node or node in v: return

            v.add(node)

            if distance == 0:
                res.append(node.val)
                return 
        
            dfs(node.left, distance - 1)
            dfs(node.right, distance - 1)
            dfs(node.parent, distance - 1)

        dfs(target, k)
        
        return res