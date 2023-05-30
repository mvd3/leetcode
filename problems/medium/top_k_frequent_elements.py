class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d[n] + 1 if n in d else 1
        r = []
        for i in range(k):
            m = list(d.keys())[0]
            for k in d.keys():
                if d[m] < d[k]:
                    m = k
            r.append(m)
            del d[m]
        return r