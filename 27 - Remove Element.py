# Given an array nums and a value val,
# remove all instances of that value in-place and return the new length.
#
# Do not allocate extra space for another array,
# you must do this by modifying the input array in-place with O(1) extra memory.
#
# The order of elements can be changed.
# It doesn't matter what you leave beyond the new length.
#
# Example 1:
#
# Given nums = [3,2,2,3], val = 3,
#
# Your function should return length = 2,
# with the first two elements of nums being 2.
#
# It doesn't matter what you leave beyond the returned length.
# Example 2:
#
# Given nums = [0,1,2,2,3,0,4,2], val = 2,
#
# Your function should return length = 5,
# with the first five elements of nums containing 0, 1, 3, 0, and 4.
#
# Note that the order of those five elements can be arbitrary.
#
# It doesn't matter what values are set beyond the returned length.
# Clarification:
#
# Confused why the returned value is an integer but your answer is an array?
#
# Note that the input array is passed in by reference,
# which means modification to the input array will be known to the caller as well.
#
# Internally you can think of this:
# // nums is passed in by reference. (i.e., without making a copy)
# int len = removeElement(nums, val);
#
# // any modification to nums in your function would be known by the caller.
# // using the length returned by your function, it prints the first len elements.
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }


def removeElement(nums: [int], val: int) -> int:
    if len(nums)==0:
        return 0

    element_index=-1
    lotsbetween=False
    for i in range(len(nums)) :
        #i go though all the items to find the val
        if element_index==-1 :
            if nums[i]==val :
                element_index=i
            #print(nums,element_index,i,len(nums))
            continue

        #print(nums,element_index,i,len(nums))
        if nums[i]!=val :
            nums[element_index]=nums[i]
            if lotsbetween :
                #there are lots of val between
                element_index+=1
            else:
                #there is no val between
                element_index=i
        else:
            lotsbetween=True
    #print(nums)
    if element_index!=-1 :
        return element_index
    else:
        return len(nums)

nums = []
val = 3
print("#####",nums)
print("-----",val, removeElement(nums,val),nums)
nums = [3,3,3,3]
val = 3
print("#####",nums)
print("-----",val, removeElement(nums,val),nums)
nums = [0,1,2,2,2,2,2,2]
val = 2
print("#####",nums)
print("-----",val, removeElement(nums,val),nums)

nums = [2,2,2,2,3,0,4,2]
val = 2
print("#####",nums)
print("-----",val, removeElement(nums,val),nums)

nums = [0,1,2,3,3,3,4,2]
val = 2
print("#####",nums)
print("-----",val, removeElement(nums,val),nums)

nums = [2,1,2,1,2,1,2,1,2]
val = 2
print("#####",nums)
print("-----",val, removeElement(nums,val),nums)

nums = [0,2,2,2,2,2,2,2,0]
val = 2
print("#####",nums)
print("-----",val, removeElement(nums,val),nums)

nums = [2]
val = 3
print("#####",nums)
print("-----",val, removeElement(nums,val),nums)

nums = [2,6]
val = 3
print("#####",nums)
print("-----",val, removeElement(nums,val),nums)

nums = [22,2,2,2,22,33,22,4,5,54,4,4,4,65]
val = 3
print("#####",nums)
print("-----",val, removeElement(nums,val),nums)
