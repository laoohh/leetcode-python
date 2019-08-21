# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:
#
# What should we return when needle is an empty string?
# This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string.
# This is consistent to C's strstr() and Java's indexOf().


def strStr(haystack: str, needle: str) -> int:
    if needle=="" :
        return 0
    if len(needle)>len(haystack) :
        return -1

    for i in range(len(haystack)) :
        if haystack[i:i+len(needle)]==needle :
            return i
    return -1

haystack = "hello"
needle = "ll"
print(haystack,needle,strStr( haystack, needle ))
haystack = "aaaaa"
needle = "bba"
print(haystack,needle,strStr( haystack, needle ))
haystack = "aaaaa"
needle = ""
print(haystack,needle,strStr( haystack, needle ))
haystack = "aaaaa"
needle = "adfsfsfsdfsfds"
print(haystack,needle,strStr( haystack, needle ))
haystack = "aaaaa"
needle = "aa"
print(haystack,needle,strStr( haystack, needle ))
haystack = "aaaaabbb"
needle = "bbb"
print(haystack,needle,strStr( haystack, needle ))
haystack = "bbaaaaa"
needle = "bb"
print(haystack,needle,strStr( haystack, needle ))
haystack = "aaaaa"
needle = "aaaaa"
print(haystack,needle,strStr( haystack, needle ))
haystack = "aaaaaedfsdfgsdfsfsdfsagfdsdfsdfsdf"
needle = "fgsdfsf"
print(haystack,needle,strStr( haystack, needle ))
