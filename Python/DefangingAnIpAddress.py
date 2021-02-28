class Solution:
    def defangIPaddr(self, address: str) -> str:
        split = address.split('.')
        join = "[.]".join(split)
        return(join)
