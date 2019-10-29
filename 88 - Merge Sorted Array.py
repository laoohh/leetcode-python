# Given two sorted integer arrays nums1 and nums2,
# merge nums2 into nums1 as one sorted array.
#
# Note:
#
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space
# (size that is greater or equal to m + n)
# to hold additional elements from nums2.
#
# Example:
#
# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
#
# Output: [1,2,2,3,5,6]
#

def merge_easy(nums1: [int], m: int, nums2: [int], n: int) -> None:
    j=0
    for i in range(m,m+n):

        nums1[i]=nums2[j]
        j+=1
    nums1.sort()

def merge(nums1: [int], m: int, nums2: [int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """

    # 2 pointer to each of the list, compare the pointed value,
    # insert before when first pointed bigger

    pointer1=pointer2=0
    endpointer1=m

    while pointer2<n and pointer1<endpointer1:
        print("pointer1=",pointer1,"   pointer2=",pointer2,
                nums1,nums2)
        if nums1[pointer1]>nums2[pointer2]:
            # put all the following elements right 1 position
            print("range=",range(m+n-1,pointer1,-1))
            for i in range(m+n-1,pointer1,-1) :
                print("i=",i)
                nums1[i]=nums1[i-1]
            # current pointed 1 put the value of pointer2
            nums1[pointer1]=nums2[pointer2]
            pointer1+=1
            pointer2+=1
            endpointer1+=1
        else:
            pointer1+=1
        print("pointer1=",pointer1,"   pointer2=",pointer2,
                nums1,nums2)

    while pointer2<n and pointer1<m+n:
        nums1[pointer1]=nums2[pointer2]
        pointer1+=1
        pointer2+=1

    m=m+n


nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge(nums1,m,nums2,n)
print( nums1, m )

nums1 = [10,0,0,0]
m = 1
nums2 = [2,5,6]
n = 3
merge(nums1,m,nums2,n)
print( nums1, m )


nums1 = [0,0,0]
m = 0
nums2 = [2,5,6]
n = 3
merge(nums1,m,nums2,n)
print( nums1, m )




nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
merge_easy(nums1,m,nums2,n)
print( nums1, m )

nums1 = [10,0,0,0]
m = 1
nums2 = [2,5,6]
n = 3
merge_easy(nums1,m,nums2,n)
print( nums1, m )


nums1 = [0,0,0]
m = 0
nums2 = [2,5,6]
n = 3
merge_easy(nums1,m,nums2,n)
print( nums1, m )
