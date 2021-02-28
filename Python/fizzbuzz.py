class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        List = []
        for x in range (n):
            x = x + 1
            if x % 3 == 0 and x % 5 == 0:
                List.append(str("FizzBuzz"))
            elif x % 3 == 0:
                List.append(str("Fizz"))
            elif x % 5 == 0:
                List.append(str("Buzz"))
            else:
                List.append(str(x))
        return(List)
