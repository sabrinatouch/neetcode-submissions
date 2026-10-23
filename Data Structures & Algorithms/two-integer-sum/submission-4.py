class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## Problem
        # nums
        #   nums[i] + nums[j] = target
        # goal: return the indices i, j
        #   return the smaller index first
        #   return as a list i.e. [smaller index, larger index]

        # notes: 
        #   - i != j
        #   - can assume there will be exactly one solution i and j that will sum up to the target
        #   - is the array sorted? NO
        #   - can the numbers be negative? YES
        #   - can the target be negative? YES
        #   - can nums be null? NO

        ## Tests
        # input: [1, 2, 3]
        # target: [3]
        # output: [0, 1]

        # input: [0, 0]
        # target: [0]
        # output: [0, 1]

        ## Pseudo-solution
        # Starting at the beginning of the array nums using i to start
            # Have j start at the i+1 index
                # If nums[i] + nums[j] is equal to the target
                    # Return i and j in a list with whichever one is smaller first
                # If nums[i] + nums[j] is not equal to the target
                    # Look at the next number in the list
                    # by incrementing j+1
                    # Repeat the conditional check at line30.

            # If we have compared all values of j starting at i+1, therefore meaning we haven't found a solution
            # Increment i by 1
            # and repeat the process at starting at line 29
            
        # input
        #   1 2 3
        # nums[i]
        #   nums[0 + 1] = 2
        # nums[j]
        #   nums[0 + 1 + 1] = 3
        # target
        #   5

        ## Implementation
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # v2
        # Use a dictionary to store the numbers in the nums array beyond the current number being evaluated

        # Set the current number being evaluated to the first number in the list
        # difference = target - nums[i] (b/c this is the number we want to look for in dictionary)
        # if the integer equaling the difference is in the dictionary, 
            # we know we've found the second value that when added to the first number we looked at, the sum of the two values equals the target
            # return the indices -- ensuring that the smaller index is returned first [small index, large index]
        # if we don't find the integer equaling the difference in the dictionary, then
        # we want to see if the sum can be achieved by starting with the next integer

        # dict = {}

        # for index, num in enumerate(nums):
        #     dict[num] = index
        
        # for i in range(len(nums)):
        #     current_num = dict.pop(nums[i])
        #     diff = target - nums[i]

        #     if diff in dict.keys():
        #         return [i, dict.get(diff)]

        ## v3
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in nums[i+1:]:
                return [i, nums.index(diff, i+1)] #.index(value, start, stop)                
            

