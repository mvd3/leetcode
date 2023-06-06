import json

class Codec:
    def serialize(self, root):
        r = [] # result
        s = [] # stack
        if root:
            r.append(root.val)
            s.append(root)
            while len(s):
                c = s.pop(0) # current
                # add child values to result list
                r += [c.left.val if c.left else None, c.right.val if c.right else None]
                if c.left:
                    s.append(c.left) # add child to stack
                if c.right:
                    s.append(c.right)

        if len(r): # None shouldn't be on the end of the list
            while r[-1] == None:
                del r[-1]

        return json.dumps(r)
        
    def deserialize(self, data):
        return json.loads(data)