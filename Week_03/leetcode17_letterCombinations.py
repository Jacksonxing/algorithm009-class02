class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return []
        self.mapping = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        res = []
        self.backtracking(res,[],0,digits)
        return res
    def backtracking(self,res,subset, index,digits):
        if len(digits) == index:
            res.append(''.join(subset))
            return 
        for i in self.mapping[digits[index]]:
            subset.append(i)
            self.backtracking(res,subset,index+1,digits)
            subset.pop()