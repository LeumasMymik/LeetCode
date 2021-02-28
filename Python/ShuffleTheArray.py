class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        List = []
        count = 0
        for x in range(n):
            List.append(nums[count])
            List.append(nums[count + n])
            count += 1
        return(List)
