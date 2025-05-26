# # https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)
# // Time Complexity :O(Logn)
# // Space Complexity :O(1)
# // Did this code successfully run on Leetcode :Yes
# // Any problem you faced while coding this :no


# // Your code here along with comments explaining your approach in three sentences only
# This is rotated sorted array it will be roattated along one pivot, there will be atleast one half sorted, Min will be in unsorted section


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,h=0,len(nums)-1
        if nums[l]<=nums[h]:return nums[l]
        while(h-l>1):
            m= l + (h-l)//2
            if nums[m-1]>nums[m] and nums[m+1]>nums[m]:return nums[m]
            elif nums[l]>nums[m]: h=m
            else:l=m
        return nums[h]
