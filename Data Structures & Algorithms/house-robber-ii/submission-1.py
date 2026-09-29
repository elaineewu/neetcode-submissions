class Solution:
    def rob(self, nums: List[int]) -> int:
        first = [0]*len(nums)
        second = [0]*len(nums)

        for i in range(len(nums)):
            if i == 0:
                first[i] = nums[i]
                second[i] = 0
            elif i == 1:
                first[i] = nums[i]
                second[i] = nums[i]
            elif i == len(nums) - 1:
                second[i] = max(max(second[:i-1]) + nums[i], second[i-1])
                first[i] = first[i-1]
            else:
                second[i] = max(max(second[:i-1]) + nums[i], second[i-1])
                first[i] = max(max(first[:i-1]) + nums[i], first[i-1])
                
        return max(max(first), max(second))