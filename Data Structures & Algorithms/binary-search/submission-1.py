class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        - Could not have solution

        1. Determine half way point
        2. Condition to look left
        3. Condition to look right
        4. Edge cases???
        '''
      
        '''
        nums -2 0 2 4 6 8
        target -1
        start 1
        end 1
        middle 0
        nums[middle] -2
        '''
        start = 0
        end = len(nums) - 1

        while start <= end:
            middle = (start+end) // 2
            if nums[middle] > target:
                # Look left
                end = middle - 1
            elif nums[middle] < target:
                # Look right
                start = middle + 1
            else:
                return middle

        return -1