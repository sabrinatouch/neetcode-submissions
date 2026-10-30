class MinStack:

    def __init__(self):
        '''
            - Initialize stack object
        '''
        self.min = [] # stack
        self.stack = [] # many ways to initialize stack in python???

    def push(self, val: int) -> None:
        '''
            - Push element 'val' onto stack
            input: [2, 2, 3, 1, 4, -1]
            self.min[-1]: -1
            min stack: top (min[0]) 2 2 2 1 1 -1 (min[N]) bottom
            stack: 2 2 3 1 4 -1
        '''
        if not self.min or val < self.min[-1]:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])

        self.stack.append(val)

    def pop(self) -> None:
        '''
            - Remove the element at the top of stack
        '''
        # If the element we're popping is the minimum
            # We want to reassign the self.min to the new minimum of the stack
            # How to keep track of next minimum?
        self.min.pop()
        self.stack.pop() # pop -> [-1] 

    def top(self) -> int:
        '''
            Return top element of the stack
        '''
        return self.stack[-1]

    def getMin(self) -> int:
        '''
            Get the minimum element in the stack
            Return the minimum element
        '''
        return self.min[-1]


'''
- Think of what you would expect these methods to do on an empty stack since that's initially what will happen
''' 
