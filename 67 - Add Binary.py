# Given two binary strings, return their sum (also a binary string).
#
# The input strings are both non-empty and contains only characters 1 or 0.
#
# Example 1:
#
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
#
# Input: a = "1010", b = "1011"
# Output: "10101"

def addBinary1(a: str, b: str) -> str:
    #add one ch by one ch
    result=""
    inc="0"
    if len(a)>=len(b) :
        maxstr=a
        minstr=b
    elif len(a)<len(b) :
        maxstr=b
        minstr=a
    maxpointer=len(maxstr)-1
    minpointer=len(minstr)-1

    while maxpointer>=0 or minpointer>=0:
        if minpointer>=0 :
            digit=int(maxstr[maxpointer])+int(minstr[minpointer])+int(inc)
        else:
            digit=int(maxstr[maxpointer])+int(inc)

        if digit==0:
            ch="0"
            inc="0"
        elif digit==1:
            ch="1"
            inc="0"
        elif digit==2:
            ch="0"
            inc="1"
        elif digit==3:
            ch="1"
            inc="1"
        result=ch+result
        maxpointer-=1
        minpointer-=1
    if inc=="1":
        result=inc+result
    return result


def addBinary(a: str, b: str) -> str:
    if not a and not b:
        return "0"
    elif not a:
        return b
    elif not b:
        return a
    else:
        return bin(int(a,2) + int(b,2))[2:]


print('a = "11", b = "1": Output: "100"  --->',addBinary("11","1"))
print('a = "1010", b = "1011": Output: "10101"  --->',addBinary("1010","1011"))
print('a = "0", b = "0": Output: "0"  --->',addBinary("0","0"))
print('a = "0", b = "1": Output: "1"  --->',addBinary("0","1"))
print('a = "1", b = "1": Output: "10"  --->',addBinary("1","1"))
print('a = "111111111", b = "1111111111111": Output: "??"  --->',addBinary("111111111","1111111111111"))
