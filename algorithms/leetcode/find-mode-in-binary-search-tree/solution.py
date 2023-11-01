class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        record = defaultdict(int)

        def dfs(node):
            if node is None:
                return

            record[node.val] += 1
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        
        mx = max(record.values())

        return [k for k,v in record.items() if v == mx]
