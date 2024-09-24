class Solution:
    def isValid(self, s: str) -> bool:
        reference = {
            "[":"]",
            "{":"}",
            "(":")"
        }
        closer = []
        for parenthesis in s:
            try:
                if parenthesis in reference:
                    closer.append(reference[parenthesis])
                elif closer[-1] == parenthesis:
                    closer.pop()
                else:
                    return False
            except:
                return False
            
        if closer:
            return False

        return True

print(Solution.isValid(True,"[([]])"))