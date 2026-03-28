class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        i=0
        k=float('inf')
        sumofcurr=0
        for j in range(0,len(nums)):
            sumofcurr+=nums[j]
            while sumofcurr>=target:
                k=min(k,j-i+1)
                sumofcurr-=nums[i]
                i+=1
        return k if k!=float('inf') else 0
    
        


            



