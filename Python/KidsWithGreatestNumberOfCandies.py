class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        List = []
        most = candies[0]
        for x in candies:
            if x > most:
                most = x
        for y in candies:
            if y + extraCandies >= most:
                List.append(True)
            else:
                List.append(False)
        return(List)
