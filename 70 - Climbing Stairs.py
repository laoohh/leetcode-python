#!!!! Approach 5: Binets Method
#


# You are climbing a stair case. It takes n steps to reach to the top.
#
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?
#
# Note: Given n will be a positive integer.
#
# Example 1:
#
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step


def climbStairs(n: int) -> int:

    def climb(n:int) -> int:
        if n<=0:    return 0
        if n==1:    return 1
        if n==2:    return 2
        if n>=3:
            return climb(n-1)+climb(n-2)

    def climb2(i, n) :
        if i>n :    return 0;   #to the ground
        if i==n:    return 1;   #last step
        return climb2(i + 1, n) + climb2(i + 2, n);

    def climb3(n:int, climb_dict:{}) :
        if n<=0:    return 0

        if n in climb_dict:
            return climb_dict[n]
        else:
            step=climb3(n-1,climb_dict)+climb3(n-2,climb_dict)
            climb_dict[n]=step
            return step

    climb_dict={ 1: 1, 2: 2 }
    return climb3(n,climb_dict)

print("1  ---",climbStairs(1))
print("2  ---",climbStairs(2))
print("3  ---",climbStairs(3))
print("4  ---",climbStairs(4))
print("5  ---",climbStairs(5))
print("6  ---",climbStairs(6))
print("10 ---",climbStairs(10))
print("20 ---",climbStairs(20))
print("30 ---",climbStairs(30))
print("40 ---",climbStairs(40))
print("50 ---",climbStairs(50))
print("100---",climbStairs(100))
#print("1000  ---",climbStairs(1000))
#print("10000  ---",climbStairs(10000))
