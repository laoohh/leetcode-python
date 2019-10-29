# Implement int sqrt(int x).
#
# Compute and return the square root of x,
# where x is guaranteed to be a non-negative integer.
#
# Since the return type is an integer,
# the decimal digits are truncated and only the integer part of the result is returned.
#
# Example 1:
#
# Input: 4
# Output: 2
# Example 2:
#
# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
#              the decimal part is truncated, 2 is returned.
#


def mySqrt(x: int) -> int:
    #use a pointer to find the left middle of s^2 is less than x
    #if x==0: return 0
    left=0
    right=x

    while left<=right :
        middle=int((left+right)/2)
        #print(left,middle,right)
        if middle*middle>x :
            right=middle-1
        elif middle*middle<x :
            left=middle+1
        else:
            return middle
    return right

print(mySqrt(0))
print(mySqrt(1))
print(mySqrt(2))
print(mySqrt(3))
print(mySqrt(4))
print(mySqrt(8))
print(mySqrt(9))
print(mySqrt(10))
print(mySqrt(16))
print(mySqrt(17))
print(mySqrt(200))
print(mySqrt(3000))
