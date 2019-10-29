# Given a non-empty array of digits representing a non-negative integer,
# plus one to the integer.
#
# The digits are stored such that the most significant digit is
# at the head of the list,
# and each element in the array contain a single digit.
#
# You may assume the integer does not contain any leading zero,
# except the number 0 itself.
#
# Example 1:
#
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:
#
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.


def plusOne(digits: [int]) -> [int]:
    #transfer the list to string, then int, then +1, then transfer back to string,
    #is there a function transfer string back to list ?
    num=int(''.join([str(digit) for digit in digits]))+1
    mylist = [int(d) for d in list(str(num))]
    return mylist

print("[1,2,3]",plusOne([1,2,3]))
print("[4,3,2,1]",plusOne([4,3,2,1]))
print("[0]",plusOne([0]))
print("[8]",plusOne([8]))
print("[1213446650]",plusOne([1213446650]))
print("[1213543252342354324352345446650]",plusOne([1213543252342354324352345446650]))


#
# class Solution {
#     public int[] plusOne(int[] digits) {
#         int i;
#         for (i = digits.length - 1; i >= 0; i--) {
#             digits[i] = (digits[i] + 1) % 10;
#             if (digits[i] != 0) {
#                 return digits;
#             }
#         }
#
#         int[] result = new int[digits.length + 1];
#         System.arraycopy(digits, 0, result, 1, digits.length);
#         result[0] = 1;
#         return result;
#     }
# }
