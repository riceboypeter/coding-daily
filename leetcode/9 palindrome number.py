class Solution:
    def isPalindrome(self, x: int) -> bool:
        forward = str(x)
        reverse = forward[::-1]
        return True if reverse == forward else False
    