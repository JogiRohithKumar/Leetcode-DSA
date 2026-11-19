class Solution:
    def minimizeSum(self, nums: List[int]) -> int:
        if len(nums)<=3:
            return 0
        
        small=sorted(heapq.nsmallest(3,nums))
        large=sorted(heapq.nlargest(3,nums))
        o0=large[0]-small[0]
        o1=large[1]-small[1]
        o2=large[2]-small[2]
        return min(o0,o1,o2)