#solution to https://leetcode.com/submissions/detail/381998451/


class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=list()
        count=nums[0]
        result.append(count)
        for i in range(1,len(nums)):
            count=count+nums[i]
            result.append(count)

        return result
