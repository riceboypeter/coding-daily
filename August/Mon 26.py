'''
August 26th, 2024
idk this one was a bit weird bc i had several solutions in mind but it's kinda hard to do the one i wanted to do in python
got it done in ~40 min anyways

Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.
For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".
'''

# there's probably a better way to do this...
def find_longest_palindrome(s: str) -> str:
    def is_palindrome(lst1, lst2):
        # recursively compare the lists
        if not lst1 or not lst2:
            return True
        if lst1[0] != lst2[0]:
            return False
        return is_palindrome(lst1[1:], lst2[1:])

    max_palindrome = ""
    s_list = list(s)

    for i in range(len(s_list)):
        for j in range(i, len(s_list)):
            sub_list = s_list[i:j + 1]
            rev_sub_list = sub_list[::-1]
            if is_palindrome(sub_list, rev_sub_list) and len(sub_list) > len(max_palindrome):
                max_palindrome = ''.join(sub_list)

    return max_palindrome

print(find_longest_palindrome("aabcdcb")) 
print(find_longest_palindrome("bananas"))  