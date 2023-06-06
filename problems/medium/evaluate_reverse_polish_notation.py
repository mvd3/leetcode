class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = [] # stack
        for n in tokens:
            if n in ["+", "-", "*", "/"]:
                a = s.pop()
                b = s.pop()
                if n == "+":
                    s.append(int(b+a))
                elif n == "-":
                    s.append(int(b-a))
                elif n == "*":
                    s.append(int(b*a))
                elif n == "/":
                    s.append(int(b/a))
            else:
                s.append(int(n))
        return s[0]