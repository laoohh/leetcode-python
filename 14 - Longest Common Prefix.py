# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.

def longestCommonPrefix(strs: [str]) -> str:
    #if strs[i][0] all equar, then check strs[i][1], till not
    if strs==[]:
        return ""
    j=0
    prefix=""
    prefix_ch="a"

    while prefix_ch!="" and j<len(strs[0]) :
        prefix_ch=strs[0][j]
        print(j,strs,prefix_ch)
        for word in strs :
            if j>=len(word) or word[j]!=prefix_ch :
                #end of search, fail
                prefix_ch=""
                break;
        #end of for, success
        prefix=prefix+prefix_ch
        j+=1
    return prefix

print('["flower","flow","flight"]: ',longestCommonPrefix(["flower","flow","flight"]))
print('["dog","racecar","car"]: ',longestCommonPrefix(["dog","racecar","car"]))
print('["dog","dogracecar","dogcar"]: ',longestCommonPrefix(["dog","dogracecar","dogcar"]))
print('Null: ',longestCommonPrefix([]))
print('["aa","a"]: ',longestCommonPrefix(["aa","a"]))
