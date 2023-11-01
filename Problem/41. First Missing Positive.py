class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        #Step1
        for index,data in enumerate(nums):
            #print('nums:',nums)
            while( nums[index]>0 and  nums[index]<=len(nums)  and nums[index] !=(nums[nums[index]-1])   ):
                
                temp=nums[nums[index]-1]
                nums[nums[index]-1] = nums[index]
                nums[index]=temp
        
        #print(nums)


        #Step2

        for index,data in enumerate(nums):
            if(nums[index] != index+1):
                return index+1
        return len(nums)+1
