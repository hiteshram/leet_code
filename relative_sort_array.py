#solution for https://leetcode.com/problems/relative-sort-array/submissions/

from itertools import repeat

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        result=list()
        
        for i in arr2:
            #count the occurance of i in arr1 and append to new list based on the count 
            #remove it from arr1 and at the end sort it and add to the new list
            rep=arr1.count(i)
            result.extend(repeat(i,rep))
            arr1=[x for x in arr1 if x!=i]
        
        
        result.extend(sorted(arr1))
        
        return result
