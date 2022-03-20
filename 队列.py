from collections import deque


class Test:
    def test(self):
        # Create a queue
        queue = deque()

        # Add element
        # Timeout Complexity:O(1)
        queue.append(1)
        queue.append(2)
        queue.append(3)
        # [1,2,3]
        print(queue)

        # Get the head of the queue
        # Time Complexity: O(1)

        temp1 = queue[0]
        # 1
        print(temp1)

        # Remove the head of the queue
        # Time Complexity:O(1)

        temp2 = queue.popleft()
        # return remove value 1
        print(temp2)
        # [2,3]
        print(queue)

        # Queue is empty?
        # Time Complexity: O(1)
        len(queue)

        # Time Complexity: O(N)
        while len(queue) != 0:
            temp = queue.popleft()
            print(temp)


if __name__ == '__main__':
    test = Test()
    test.test()
