# https://leetcode.com/problems/defanging-an-ip-address/

class Solution:
    def defangIPaddr(self, address: str) -> str:
        split = address.split('.')
        join = "[.]".join(split)
        return(join)
