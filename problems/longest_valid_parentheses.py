class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        for c in s:
            stack.append(c)
            #print("Прије:", stack)
            if len(stack) == 2:
                if stack[0] == "(" and stack[1] == ")":
                    stack[0] = 2
                    del stack[1]
            elif len(stack) > 2:
                if stack[-2] == "(" and stack[-1] == ")":
                    if stack[-3] != "(" and stack[-3] != ")":
                        stack[-3] += 2
                        del stack[-2]
                    else:
                        stack[-2] = 2
                    del stack[-1]
                elif stack[-3] == "(" and stack[-1] == ")":
                    if len(stack) > 3:
                        if stack[-4] != "(" and stack[-4] != ")":
                            stack[-4] += stack[-2] + 2
                            del stack[-3], stack[-2], stack[-1]
                        else:
                            stack[-2] += 2
                            del stack[-3], stack[-1]
                    else:
                        stack[-2] += 2
                        del stack[-3], stack[-1]
            #print("После", stack)
        r = 0
        for n in stack:
            if n != "(" and n != ")":
                if n > r:
                    r = n
        return r