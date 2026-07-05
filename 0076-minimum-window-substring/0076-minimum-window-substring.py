class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target_dict = Counter(t)
        need = len(target_dict)
        curr_dict = {char:0 for char in target_dict.keys()}
        have = 0 
        res_len = float('inf')
        res_start = 0
        
        l = 0
        for r in range(len(s)):
            if s[r] in curr_dict:
                curr_dict[s[r]] += 1
                if curr_dict[s[r]] == target_dict[s[r]]:
                    have += 1

                while have == need:
                    if res_len > r-l+1:
                        res_len = r-l+1
                        res_start = l
                    if s[l] in curr_dict:
                        curr_dict[s[l]] -= 1
                        if curr_dict[s[l]] < target_dict[s[l]]:
                            have -= 1
                    l += 1
        return s[res_start: res_start+res_len] if res_len != float('inf') else ""
                
