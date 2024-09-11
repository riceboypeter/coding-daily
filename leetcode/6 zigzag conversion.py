
class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows >= len(s):
            return s

        index = 0
        rows = [[] for row in range(numRows)]

        down = True

        for letter in s:
            if down:
                rows[index].append(letter)
                index += 1
                if index == numRows -1:
                    down = False
            elif not down:
                rows[index].append(letter)
                index -= 1
                if index == 0:
                    down = True

        for i in range(numRows):
            rows[i] = ''.join(rows[i])

        return "".join(rows)