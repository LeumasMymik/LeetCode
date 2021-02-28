# https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth = 0
        for i in accounts:
            count = 0
            for j in i:
                count = count + j
            if wealth <= count:
                wealth = count
        return(wealth)
