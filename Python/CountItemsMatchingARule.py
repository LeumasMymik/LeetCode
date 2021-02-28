# https://leetcode.com/problems/count-items-matching-a-rule/

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        for x in items:
            if ruleKey == "type" and ruleValue == x[0]:
                count += 1
            elif ruleKey == "color" and ruleValue == x[1]:
                count += 1
            elif ruleKey == "name" and ruleValue == x[2]:
                count += 1
        return(count)
