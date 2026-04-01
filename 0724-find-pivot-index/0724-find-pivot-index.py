class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left=0
        right=0
       
        total=sum(nums)
        n=len(nums)
        
        for i in range(n):
            right = total - left - nums[i]
            

        
            if right==left:
                return i
            left+=nums[i]

        return -1            