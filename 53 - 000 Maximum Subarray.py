# !!!!!!!!!!!!!
# Given an integer array nums,
# find the contiguous
# subarray (containing at least one number)
# which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:
#
# If you have figured out the O(n) solution,
# try coding another solution using the divide and conquer approach,
# which is more subtle.

#
# def maxSubArray(self, nums: List[int]) -> int:
#
#     max_here = 0
#     max_sofar = -maxsize-1
#
#     for i in range(len(nums)):
#         max_here = max_here + nums[i]
#         if(max_sofar < max_here):
#             max_sofar = max_here
#         if(max_here<0):
#             max_here = 0
#     return max_sofar
#
#
#
#
#             :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return 0
#         currSum= nums[0]
#         maxSum = currSum
#         for x in range(1,len(nums)):
#             if currSum < nums[x] and currSum < 0:
#                 currSum = nums[x]
#             else:
#                 currSum += nums[x]
#             maxSum = max(currSum,maxSum)
#         return maxSum
# 		```
#
#
#
#         from sys import maxsize
#
#
#
# def max_subarray(nums):
#
#     BEST = -maxsize - 1
#     FINAL = -maxsize - 1
#     for i in range(0, len(nums)):
#         CURRENT = nums[i]
#         BEST = max(CURRENT+BEST, CURRENT)
#
#         if BEST > FINAL:
#             FINAL = BEST
#         else:
#             pass
#
#     return FINAL
#
#

def maxSubArray(nums:[int]):
        pre = nums[0]
        max_ = nums[0]
        sub_begin = 0
        sub_end = 0

        for i in range(1, len(nums)):
            if pre+nums[i]<=nums[i] :
                sub_begin=i
            pre = max(pre+nums[i], nums[i])

            if max_<=pre :
                sub_end=i
            max_ = max(max_, pre)
        return max_, nums[sub_begin:sub_end+1]

nums=[-2,1,-3,4,-1,2,1,-5,4]
print(nums,"----------",maxSubArray(nums))

nums=[-2,1,-3,4,-1,2,1,-5,9]
print(nums,"----------",maxSubArray(nums))

nums=[-2,1,-3,4,-1,2,1,-5,9,-3,4,1,-2,1]
print(nums,"----------",maxSubArray(nums))
