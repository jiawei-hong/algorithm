class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        r_queue = []
        d_queue = []

        for i in range(len(senate)):
            if senate[i] == "R":
                r_queue.append(i)
            else:
                d_queue.append(i)

        while r_queue and d_queue:
            r, d = r_queue.pop(0), d_queue.pop(0)

            if r < d:
                r_queue.append(len(senate) + r)
            else:
                d_queue.append(len(senate) + d)

        return "Dire" if d_queue else "Radiant"
