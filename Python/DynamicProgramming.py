
# 509. Fibonacci Number
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

class Solution:
    def fib(self, n: int) -> int:
        result = [0, 1]
        if(n < 2):
            return n
        for i in range (2, n+1):
            result.append(result[i-1] + result[i-2])
        return result[n]

class Solution:
    def fib (self, n: int) -> int:
        pre = 0
        cur = 1
        if(n < 2):
            return n
        for i in range(1, n+1):
            tmp = cur
            cur = cur + pre
            pre = tmp
        return tmp


# 70. Climbing Stairs
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1
        for i in range (n-1):
            tmp = one
            one = one + two
            two = tmp
        return one

# 1137. N-th Tribonacci Number
# The Tribonacci sequence Tn is defined as follows: 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.

class Solution:
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1
        if n == 0:
            return 0
        if n < 3:
            return 1
        for i in range (n):
            tmp = t2
            t2 = t2+t1+t0
            t0 = t1
            t1 = tmp
        return t0
        
        
# 746. Min Cost Climbing Stairs

# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

# You can either start from the step with index 0, or the step with index 1.

# Return the minimum cost to reach the top of the floor.

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        LENGTH = len( cost )
        
        if LENGTH == 1:
            return cost[0];
        
        if LENGTH == 2:
            return min(cost[0], cost[1]);
        
        memoPaths = [0 for _ in range(LENGTH)]
        
        memoPaths[0] = cost[0]
        memoPaths[1] = cost[1]
        
        for i in range ( 2, LENGTH ):
            memoPaths[i] = min(memoPaths[i - 1], memoPaths[i - 2]) + cost[i];
            
        return min(memoPaths[-1], memoPaths[-2])
    
    
    

# 198. House Robber

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

class Solution:
    def rob(self, nums: List[int]) -> int:
        LENGTH = len(nums)
        
        if LENGTH == 1:
            return nums[0]
        if(LENGTH == 2):
            return max(nums[1], nums[0])
        if(LENGTH == 3):
            return max(nums[1], nums[0] + nums[2])
        
        memo = [0 for _ in range(LENGTH)]
        memo[0] = nums[0]
        memo[1] = nums[1]
        memo[2] = nums[0] + nums[2]
        
        for i in range (3, LENGTH ):
            tmp = max(memo[i-3], memo[i-2])
            
            memo[i] = tmp + nums[i]
            
            
        return max(memo[i-1], memo[i])


# 213. House Robber II

# You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.
 
# Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.


class Solution:
    def rob(self, nums: List[int]) -> int:
        LENGTH = len(nums)
        
        if(LENGTH == 1):
            return nums[0]
        if(LENGTH == 2):
            return max(nums[0], nums[1])
        if LENGTH == 3 :
            return max(nums[0], nums[1], nums[2])
        
        m1 = [0 for _ in range(LENGTH)]
        m2 = [0 for _ in range(LENGTH)]
        
        m1[0] = m1[1] = nums[0]
        for i in range(2, LENGTH - 1):
            m1[i] = max(m1[i-1], m1[i-2] + nums[i])
            
        m2[1] = nums[1]
        m2[2] = max(nums[1], nums[2])
        for i in range(3, LENGTH) :
            m2[i] = max(m2[i-1], m2[i-2] + nums[i])
            
        return max(m1[LENGTH - 2], m2[LENGTH - 1])



# 740. Delete and Earn

# You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

# Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
# Return the maximum number of points you can earn by applying the above operation some number of times.

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        length = len(nums)
        
        freq = [0 for _ in range (100000)]
        dp = [0 for _ in range (100000)]
        
        for i in range (length):
            freq[nums[i]] += nums[i]
        
        dp[1] = freq[1]
        for i in range(2, 100000):
            dp[i] = max(dp[i-1], dp[i-2] + freq[i])
            
        return max(dp[100000 - 1], dp[100000 - 2])



# 55. Jump Game

# You are given an integer array nums. You are initially positioned at the array's first index, and each element in the array represents your maximum jump length at that position.

# Return true if you can reach the last index, or false otherwise.

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        mark = True
        mj = 0
        
        for i in range(0, n):
            mj = max(mj - 1, nums[i])
            if(mj == 0 and i != n - 1):
                mark = False
                break
        
        return mark
            

# 45. Jump Game II

# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

# Each element in the array represents your maximum jump length at that position.

# Your goal is to reach the last index in the minimum number of jumps.

# You can assume that you can always reach the last index.

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        n = len(nums)
        cur = farthest = jump = 0
        
        for i in range(n - 1): 
            farthest = max(farthest, nums[i] + i)
            
            if(i == cur):
                jump+=1
                cur = farthest
                
                if(farthest >= n-1):
                    return jump
                
        return jump            