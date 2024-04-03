class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, idx=0):
            if idx == len(word):
                return True

            # check if collision the edge
            if (
                i < 0
                or j < 0
                or i >= row
                or j >= col
                or v[i][j]
                or board[i][j] != word[idx]
            ):
                return False
            v[i][j] = True

            # handle four direction (top, left, right, bottom)
            if (
                dfs(i + 1, j, idx + 1)
                or dfs(i - 1, j, idx + 1)
                or dfs(i, j + 1, idx + 1)
                or dfs(i, j - 1, idx + 1)
            ):
                return True
            v[i][j] = False
            return False

        row = len(board)
        col = len(board[0])
        v = [[False] * col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                if dfs(i, j):
                    return True
        return False
