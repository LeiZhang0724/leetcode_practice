# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside
# the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).


def reverse(x: int) -> int:
    INT_MIN, INT_MAX = -2 ** 31, 2 ** 31 - 1

    rev = 0
    while x != 0:
        # INT_MIN 也是一个负数，不能写成 rev < INT_MIN // 10
        if rev < INT_MIN // 10 + 1 or rev > INT_MAX // 10:
            return 0
        digit = x % 10
        # Python3 的取模运算在 x 为负数时也会返回 [0, 9) 以内的结果，因此这里需要进行特殊判断
        if x < 0 < digit:
            digit -= 10

        # 同理，Python3 的整数除法在 x 为负数时会向下（更小的负数）取整，因此不能写成 x //= 10
        x = (x - digit) // 10
        rev = rev * 10 + digit

    return rev


# Slice notation "[a:b:c]" means "count in increments of c starting at a inclusive, up to b exclusive". If c is
# negative you count backwards, if omitted it is 1. If a is omitted then you start as far as possible in the
# direction you're counting from (so that's the start if c is positive and the end if negative). If b is omitted then
# you end as far as possible in the direction you're counting to (so that's the end if c is positive and the start if
# negative). If a or b is negative it's an offset from the end (-1 being the last character) instead of the start.
#
# OK, so string[0::-1] is one character, it says "count backwards from index 0 as far as you can". As far as it can
# is the start of the string.
#
# string[0:len(string):-1] or for that matter string[0:anything:-1] is subtly different. It's empty for the same
# reason that string[1:0] is empty. The designated end of the slice cannot be reached from the start. You can think
# of this as the slice having ended "before" it began (hence is empty), or you can think of the end point being
# automatically adjusted to be equal to the start point (hence the slice is empty).
#
# string[:len(string):-1] means "count backwards from the end up to but not including index len(string)". That index
# can't be reached, so the slice is empty.
#
# You didn't try string[:0:-1], but that means "count backwards from the end up to but not including index 0". So
# that's all except the first character, reversed. [:0:-1] is to [::-1] as [0:len(string)-1] is to [:]. In both cases
# the excluded end of the slice is the index that would have been the included last character of the slice with the
# end omitted. 
#
# You also didn't try string[-1::-1], which is the same as string[::-1] because -1 means the last character of the
# string.
