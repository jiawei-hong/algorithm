class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        x1,y1 = coordinates[0]
        x2,y2 = coordinates[1]

        for i in range(2, n):
            x,y = coordinates[i]

            if (x-x1) * (y2-y1) != (y-y1) * (x2-x1):
                return False


        return True
