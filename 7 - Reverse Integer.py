# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−231,  231 − 1].
# For the purpose of this problem,
# assume that your function returns 0 when the reversed integer overflows.
#



import math

def reverse(x: int) -> int:
    if x<0:
        nagetive=-1
    else:
        nagetive=1
    strx=str(abs(x))
    i=0
    stry=""
    print(strx)
    while i<len(strx) :
        stry=strx[i]+stry
        i+=1
    reverse_num=nagetive*int(stry)
    if reverse_num<-pow(2,31) or reverse_num>pow(2,31)+1 :
        reverse_num=0
    return reverse_num

def reverse2(x: int) -> int:
    if x<0:
        nagetive=-1
    else:
        nagetive=1
    strx=str(abs(x))[::-1]

    reverse_num=nagetive*int(strx)

    if reverse_num<-pow(2,31) or reverse_num>pow(2,31)+1 :
        reverse_num=0
    return reverse_num

print(reverse2(1534269))
