class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
            - ordered
            - return [index1, index2] where index1 < index2

            Can assume:
            - non-null, non-zero input

            Limited:
            - 

            Test:
            ## same number
            input: [1, 1]
            target: 2
            output: [1, 2]

            ## negative inputs
            input: [-1, 1]
            target: 0
            output: [1, 2]

            ## negative target
            input: [-1, -1]
            target: -2
            output: [1, 2]

            ## positive/negative mixed input
            input: [-3, 4]
            target: 1
            output: [1, 2]

            ## many negatives
            input: [-3, -2, -1, 1, 2, 6]
            target: 3
            output:

            target - input = diff
            3 - (-3) = 6

            input - target
            -3 - 3 = -6

            input = -3
            target = -5
            want: -2
                target - input
                    -5 + (-3) = -8
                input - target 
                    (-3) - (-5) = 2 

            numbers[i] : -3
            i: 0
            target: -5
            diff: -5 - (-3) = -2
                numbers[j] : 
                j: 1

            [i + 1, j + 1]

            Pseudo
            - start at the first index
                - looking for the difference between the target - element at the index
                - look for that difference in the rest of the array
                - if we find the difference,
                    - want to return the first index and the index where we found the difference in the array
                        (NOTE: 1-indexed so 0th index -> 1th index)
        '''

        '''
        ## same number
            input: [1, 1]
            target: 2
            output: [1, 2]

            i: 0
            numbers[i]: 1
            target: 2
            diff: 2 - 1 = 1
            j: i + 1 = 1
            numbers[j] = 1

        return [0 + 1, 1 + 1] = [1, 2]

        ## many negatives
            input: [-3, -2, -1, 1, 2, 6]
            target: 3
            output: [1, 6]

            i: 0
            numbers[i]: -3
            target: 3
            diff: 3 - (-3) = 6
            j: i + 1 = 
            numbers[j] = 
        '''

        '''
            ## many negatives
                                j
            input: [-3, -2, -1, 1, 5, 6]
            target: 11
            output: [1, 5]

            calculated sum: -3 + 6 = 3
                3 > 2 (target)
            target: 

            ## pseudo
                when the sum of numbers[i] + numbers[j] is > target
                    we want to decrease j by 1
                when the sum is < target
                    we want to increase i by 1 
        '''
        '''
            target: 5
            input: [-2, 1, 4]
            i: 1
            numbers[i]: 1
            j: 2
            numbers[j] = 4

            sum: 1 + 4 = 5

            target: -1
            [-2, -1, 0, 2]
            output: [2, 3]

            i: 1
            numbers[i]: -1
            j: 2
            numbers[j] = 0

            sum: -1 + 0 = -1
                -1 = -1
        '''
        '''
            numbers=[100,200,300,500]
            target=500
            output: [2, 3]

            i: 1
            numbers[i]: 200
            j: 2
            numbers[j] = 300

            sum: 200 + 300 = 500
                500 = 500
                [2, 3]
        '''
        i = 0
        j = len(numbers) - 1

        while i < j:
            sum = numbers[i] + numbers[j]
            if sum == target:
                return [i + 1, j + 1]
            elif sum > target:
                j -= 1
            elif sum < target:
                i += 1

        return -1
