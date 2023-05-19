import re

class Solution:
    def isNumber(self, s: str) -> bool:
        return re.search("^[+|-]?(([0-9]+)?\.?[0-9]+|[0-9]+\.?([0-9]+)?)([e|E][+|-]?[0-9]+)?$", s) != None