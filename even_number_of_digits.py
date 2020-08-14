#solution for the problem https://leetcode.com/explore/featured/card/fun-with-arrays/521/introduction/3237/

class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0

        for i in nums:
            if len(str(i))%2==0:
                count=count+1

        return count
