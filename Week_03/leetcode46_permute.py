class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def recPermute(res,lis,rem):
            if len(rem) == 0 :
                res.append(lis)
                return
            for i,val in enumerate(rem):
                recPermute(res, lis + [val] ,rem[:i] + rem[i+1:])

        for i in range(len(nums)):       
            recPermute(res,[nums[i]],nums[:i] + nums[i+1:])   
        return res    