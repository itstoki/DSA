class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left=0
        right=len(nums)-1
        res=[]
        nums=[x*x for x in nums]
        for i in range(len(nums)):
            if right >= left:
                if nums[right]>=nums[left]:
                    res.append(nums[right])
                    right-=1
                else:
                    res.append(nums[left])
                    left+=1             
        return res[::-1]      
