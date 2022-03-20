import heapq

class Test:
    def test(self):
        # Create minheap
        minheap = []
        heapq.heapify(minheap)

        # Add element
        heapq.heappush(minheap,10);
        heapq.heappush(minheap,8);
        heapq.heappush(minheap,9);
        heapq.heappush(minheap,2);
        heapq.heappush(minheap,1);
        heapq.heappush(minheap,11);
        # minheap=[1, 2, 9, 10, 8, 11]
        print(f'{minheap=}')

        # nlargest(3,minheap)
        print(f'{heapq.nlargest(3,minheap)=}')

        # nsmallest(1,minheap)
        print(f'{heapq.nsmallest(1,minheap)=}')


        #peek
        # 1
        print(f'{minheap[0]=}')
        # length
        print(f'{len(minheap)=}')

        #Delete
        print(f'{heapq.heappop(minheap)=}')
        # heapq.heappop(minheap)

        # Size
        length = len(minheap)
        print(f'{length=}')

        # Iteration
        while len(minheap)!=0:
            print(f'{heapq.heappop(minheap)=}')



if __name__ == '__main__':
    test = Test()
    test.test()