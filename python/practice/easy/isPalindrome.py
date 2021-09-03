# Given an integer x, return true if x is palindrome integer.
#
# An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is
# not.
def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    else:
        return True if x == int(str(x)[::-1]) else False
