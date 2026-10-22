class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # nums = [1, 2, 3, 3]
        # output: true

        # nums = [1, 2, 3, 4]
        # output: false

        # nums = [1]
        # output: false

        # empty nums
        # nums = []
        # output: false

        # constraints:
        # - assume nums array is unsorted

        # sorted
        # [1, 2, 3, 3]

        # unsorted
        # [3, 1, 2, 3]

        # check if list <= 1 or null:
            # return false
        # start at beginning of array
            # have two indexes
            # index 1: start at beginning of array
            # index 2: ahead of index 1 +1
                # check the values at index1 and index2
                # if the values are equal, we have a duplicate
                    # return true
                # else increment index2
                # once index2 reaches end of list, increment index1 +1            
                # if index1 reaches the end of list, no duplicates have been found.
        # return false

        # if nums is None or len(nums) <= 1:
        #     return False
        
        # for i in range(len(nums)): # time: O(N), space: O(1)
        #     for j in range(i + 1, len(nums)): # time: O(N)
        #         if nums[i] == nums[j]:
        #             return True 
        
        # return False 
        
        # O(n^2)
        
        visited = set()
        for num in nums: # How many times does your code execute
            if num in visited: # O(1)
                return True
            else:
                visited.add(num) # O(1)
            
        return False # O(N)

        # Starting at the beginning of array
        # Look at the value
        # Check if the value exists in the set
            # If it doesn't exist, then we haven't visited it yet
                # Add the value into the set
            # Else if the value does exist in the set, then we visited it before therefore the value is a duplicate
                # Return True
        # If we reach the end of the arrray no duplicate has been found
        # Return false