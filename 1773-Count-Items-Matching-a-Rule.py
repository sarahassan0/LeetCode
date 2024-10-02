class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        rules_map = {
            'type': 0,
            'color': 1,
            'name' : 2
        }
        itmes_count = 0

        for item in items:
            if item[rules_map[ruleKey]] == ruleValue:
                itmes_count += 1

        return itmes_count

        