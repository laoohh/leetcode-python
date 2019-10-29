# The count-and-say sequence is the sequence of integers
# with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 6.     312211
# 7.     13112221
# 8.
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n where 1 ≤ n ≤ 30,
# generate the nth term of the count-and-say sequence.
#
# Note: Each term of the sequence of integers will be represented
# as a string.
#
# Example 1:
#
# Input: 1
# Output: "1"
#
# Example 2:
#
# Input: 4
# Output: "1211"

def countAndSay(n: int) -> str:
    count_and_say='1'

    while n>=2:
        digit_index=0
        new_count_and_say=""

        while digit_index<len(count_and_say):
            digit_str=count_and_say[digit_index]
            count=1
            while digit_index+1<len(count_and_say) and \
                    digit_str==count_and_say[digit_index+1]:
                count+=1
                digit_index+=1

            new_count_and_say+=str(count)+digit_str
            digit_index+=1
            #print(new_count_and_say,count_and_say)

        count_and_say=new_count_and_say
        n-=1

    return count_and_say

print("1.     1",countAndSay(1))
print("2.     11",countAndSay(2))
print("3.     21",countAndSay(3))
print("4.     1211",countAndSay(4))
print("5.     111221",countAndSay(5))
print("6.     312211",countAndSay(6))
print("7.     13112221",countAndSay(7))
