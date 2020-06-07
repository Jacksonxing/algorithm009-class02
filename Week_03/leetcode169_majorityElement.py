class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic  = {}
        for i in nums:
            dic[i] = dic.get(i,0) + 1  #Count the occurrences
        count_order = sorted(dic.items(), key = lambda k:k[1])    #Sort dictionary by value.
        return count_order[-1][0] 