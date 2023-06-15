class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(words)
        ws = len(words[0]) # word size
        ss = n * ws # substring size
        
        if len(s) < ss:
            return []

        r = []
        pc = {} # permutation content
        cc = {} # correct content
        sp = 0 # start position

        for w in words:
            if w not in cc:
                cc[w] = 1
                pc[w] = 0
                continue
            cc[w] += 1

        while sp + ss <= len(s):
            i = sp
            while i < sp + ss:
                w = s[i:i+ws] # word 
                if w in words: # word detected
                    if pc[w] < cc[w]: # wasn't there before
                        pc[w] += 1 # add to dictionary
                        i += ws # move index
                    else: # already have word
                        sp += 1
                        break
                    continue
                sp += 1 # maybe next character is the begining of a word
                break
            if pc == cc: # correct substring
                r.append(sp) # add result
                sp += 1 # move to next character
            for k in pc.keys():
                pc[k] = 0
        
        return r