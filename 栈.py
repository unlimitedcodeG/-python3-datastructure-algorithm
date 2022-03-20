from inspect import stack


class Stack:
    def test(self):
        # Create a stack
        stack = []

        # Add element 
        # Time Complexity: O(1)
        stack.append(1)
        stack.append(2)
        stack.append(3)
        # [1,2,3]
        print(stack)

        # Get the top of stack 
        # Time complexity:O(1)
        stack[-1]
        # 3 
        print(stack[-1])

        # Get stack length
        # Time complexity: O(1)
        size = len(stack)
        print(size)

        # Stack is empty？
        # Time complexity:O(1)
        len(stack) == 0
        
        # Iterate Stack
        # Time complexity:O(N)
        while len(stack)>0:
            temp = stack.pop()
            print(f'{temp=}')



if __name__ == '__main__':
    test = Stack()
    test.test()