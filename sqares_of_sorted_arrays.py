#solution for the https://leetcode.com/explore/featured/card/fun-with-arrays/521/introduction/3240/

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        
        square_list=[x*x for x in A]
        square_list.sort()
        
        return square_list
