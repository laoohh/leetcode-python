# Determine whether an integer is a palindrome. 
# An integer is a palindrome when it reads the same backward as forward.
#
# Example 1:
#
# Input: 121
# Output: true
# Example 2:
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-.
#  Therefore it is not a palindrome.
# Example 3:
#
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:
#
# Coud you solve it without converting the integer to a string?
#

def isPalindrome( x: int) -> bool:
    if x==0 :
        return True
    elif x<0 or x%10==0 :
        return False

    push = 0
    oragin = x

    while x>0 :
        push = push*10 + x%10
        x=int(x/10)

    print(oragin,x,push)
    if push==oragin :
        return True
    else:
        return False


inputnum=input("input number:")

def isPalindrome2( x: int) -> bool:
    s=str(x)
    return s==s[::-1]

print(isPalindrome2(int(inputnum)))
