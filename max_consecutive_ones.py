#solution to the link https://leetcode.com/explore/featured/card/fun-with-arrays/521/introduction/3238/

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        temp_list=list()

        for i in nums:
            if(i==1):
                count=count+1
            else:
                temp_list.append(count)
                count=0

        temp_list.append(count)

        return max(temp_list)
