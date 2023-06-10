class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        set_word_list = set(wordList)

        if endWord not in set_word_list:
            return 0

        queue = deque()
        queue.append((beginWord,1))

        while queue:
            w, step = queue.popleft()

            for i in range(len(beginWord)):
                for j in range(26):
                    n = w[:i] + chr(97 + j) + w[i+1:]
                    
                    if n == endWord:
                        return step + 1

                    if n in set_word_list:
                        queue.append((n,step+1))
                        set_word_list.remove(n)                  
                    
        return 0
