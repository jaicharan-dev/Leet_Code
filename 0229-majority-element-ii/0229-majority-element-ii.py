class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums: return []
        curr1, curr2 = None, None
        cnt1, cnt2 = 0, 0

        for n in nums:
            if n == curr1:
                cnt1 += 1
            elif n == curr2:
                cnt2 += 1
            elif cnt1 == 0:
                curr1 = n
                cnt1 = 1
            elif cnt2 == 0:
                curr2 = n
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1, cnt2 = 0, 0
        for n in nums:
            if curr1 == n:
                cnt1 += 1
            elif curr2 == n:
                cnt2 += 1
        
        res = []
        cnt_needed = len(nums) // 3

        if cnt1 > cnt_needed:
            res.append(curr1)
        if cnt2 > cnt_needed:
            res.append(curr2)
        
        return res