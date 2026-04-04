class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sum=0
        count=0
        hashmap={0:1}
        for num in nums:
            sum+=num
            r=sum%k
            if r in hashmap:
                count+=hashmap[r]
            hashmap[r]=hashmap.get(r,0)+1
        return count
        