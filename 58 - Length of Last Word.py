# Given a string s consists of upper/lower-case alphabets
# and empty space characters ' ',
# return the length of last word in the string.
#
# If the last word does not exist, return 0.
#
# Note: A word is defined as a character sequence consists of
# non-space characters only.
#
# Example:
#
# Input: "Hello World"
# Output: 5

def lengthOfLastWord(s: str) -> int:
    if s=="" :
        return 0

    split_list=s.split()
    print(split_list)
    if len(split_list)==0:
        return 0
    last_word=split_list[-1]
    print(last_word)
    return len(last_word)

s=""
print(lengthOfLastWord(s))

s=" "
print(lengthOfLastWord(s))

s="              "
print(lengthOfLastWord(s))


s="World"
print(lengthOfLastWord(s))

s="Hello World"
print(lengthOfLastWord(s))

s="Hello World Hello World Hello World Hello World Hello World!"
print(lengthOfLastWord(s))
