#leet code 1
"""
question:
    You are given two integers n and t. Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.
    
Example 1:
Input: n = 10, t = 2
Output: 10
Explanation:
The digit product of 10 is 0, which is divisible by 2, making it the smallest number greater than or equal to 10 that satisfies the condition.
"""

#working answer:
class Solution:
   def smallestNumber(self, n: int, t: int) -> int:
    def pr(n):
        lt = 1
        while n:
            lt*=n%10
            n//=10
        return lt
    while pr(n)%t!=0:
        n+=1
    return n
