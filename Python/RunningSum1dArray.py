# https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        List = []
        sum = 0
        for x in nums:
            sum = sum + x
            List.append(sum)
        return(List)
