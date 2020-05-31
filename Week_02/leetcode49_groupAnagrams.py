class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = {}
        for st in strs:
            ss = "".join(sorted(st))
            if ss not in ht:
                ht[ss]=[st]
            else:
                ht[ss].append(st)
        return ht.values()