# Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
# determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
#
# Input: "(]"
# Output: false
# Example 4:
#
# Input: "([)]"
# Output: false
# Example 5:
#
# Input: "{[]}"
# Output: true

def isValid(s: str) -> bool:
    #using the push / pop method
    #left parenthese push, right parenthese pop the same type, check failure
    if len(s)==0 :
        return True
    elif len(s)==1 :
        return False

    stack=[]
    left=["(","[","{"]
    right=[")","]","}"]

    for ch in s :
        #print("for:",s,ch)
        if ch in left :
            stack.append(ch)
        elif ch in right :
            if len(stack)==0 :
                return False
            popch=stack.pop()
            for i in range(len(left)) :
                #print(ch,popch)
                if  ch==right[i] and popch!=left[i] :
                    #not match
                    return False
            #match so far
    if len(stack)==0 :
        return True
    else :
        return False

print(isValid("()"))
print(isValid("()[]{}"))
print(isValid("(]"))
print(isValid("([)]"))
print(isValid("{[]}"))
print(isValid("(("))
