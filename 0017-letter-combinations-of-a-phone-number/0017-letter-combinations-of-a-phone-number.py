class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        keyboard = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }

        res = []
        path = []
        
        def dfs(i):
            if len(path) == len(digits):
                res.append("".join(path))
                return
            
            cur_digit = digits[i]
            letters = keyboard[cur_digit]

            for letter in letters:
                path.append(letter)
                dfs(i+1)
                path.pop()
        dfs(0)
        return res
        
        