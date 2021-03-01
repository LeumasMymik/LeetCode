# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewel = list(jewels)
        stone = list(stones)
        for x in range(len(jewel)):
            for y in range(len(stone)):
                if jewel[x] == stone[y]:
                    count += 1
        return(count)
