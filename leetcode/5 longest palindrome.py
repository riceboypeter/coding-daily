s = "asdsc"

def longestPalindrome(s: str) -> str:
    def check(left:int, right:int):
        right = right-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    for length in range(len(s),0,-1):
        for start in range(len(s) - length + 1):
            if check(start, start + length):
                return s[start: start + length]
    
print(longestPalindrome(s))