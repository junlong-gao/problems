class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        #print nums
        rst = 0
        for i in range(len(nums)/2):
            #print len(nums) - 2 - 2*i, nums[len(nums) - 2 - 2*i] 
            rst = rst + nums[len(nums) - 2 - 2*i] 
        return rst