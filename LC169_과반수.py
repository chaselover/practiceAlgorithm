class Solution:
    def majorityElement(self, nums) -> int:
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        half = len(nums)//2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])
        return [b,a][nums.count(a)>half]

# self를 붙히는 이유는 매개변수인 nums에 대한 재귀이기 때문에?
