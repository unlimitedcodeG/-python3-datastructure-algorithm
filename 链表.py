from collections import deque


class Test:
    def test(self):
        # Create an Linkedlist
        linkedlist = deque()

        # Add element
        # Time Complexity:O(1)
        linkedlist.append(1)
        linkedlist.append(2)
        linkedlist.append(3)
        # [1,2,3]
        print(linkedlist)

        # Insert element
        # Time Complexity: O(N)
        linkedlist.insert(2, 99)
        # insert(index,value)
        # [1,2,99,3]
        print(linkedlist)

        # Access element
        # Time Complexity:O(N)
        element = linkedlist[2]
        # 99
        print(element)

        # Search element
        # Time Complexity:O(N)
        index = linkedlist.index(99)
        # return index:2
        print(index)

        # Update element
        # Time Complexity:O(N)
        linkedlist[2] = 88
        # [1,2,88,3]
        print(linkedlist)

        # Remove element
        # Time Complexity:O(N)
        # [1,2,3]
        linkedlist.remove(88)
        print(linkedlist)

        # Length
        # Time Complexity:O(1)
        length = len(linkedlist)
        # 3
        print(length)


if __name__ == '__main__':
    test = Test()
    test.test()
