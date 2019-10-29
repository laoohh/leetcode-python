#
# Given an array of integers,
# return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#https://www.cnblogs.com/grandyang/p/4606334.html
#https://blog.csdn.net/haolexiao/article/details/53487436
#https://www.jianshu.com/p/452423986672




def twoSum(nums: [], target):
    for x in nums :
        index1=nums.index(x)
        new_nums=nums.copy()
        del new_nums[index1]
        if target-x in new_nums :
            return [ index1, new_nums.index(target-x)+1 ]

inputlist=[3,2,4]
#print(twoSum(inputlist,6))

def twoSum2(nums: [], target):
    i=0
    while i<len(nums) :
        print("nums:",nums)
        y=target-nums[i]
        if y not in nums :
            i+=1
            continue
        del nums[i]
        print("nums:",nums)
        print("nums[i]:",nums[i])
        print("target-nums[i]",target-nums[i])
        return [ i, nums.index(y)+1 ]

inputlist=[3,2,4]
print(twoSum2(inputlist,6))
