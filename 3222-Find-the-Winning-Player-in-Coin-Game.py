class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        winner = 0
        while x >= 1 and y >= 4:
            x -= 1
            y -= 4
            winner += 1


        return  'Bob' if winner %  2 == 0 else 'Alice'
        