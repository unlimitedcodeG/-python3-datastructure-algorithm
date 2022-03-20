import heapq 

class Test:
    def test(self):
        # Create maxheap 
        maxheap = [] 
        heapq.heapify(maxheap*-1)

        # Add element 
        heapq.heappush(maxheap,10*-1);
        heapq.heappush(maxheap,8*-1);
        heapq.heappush(maxheap,9*-1);
        heapq.heappush(maxheap,2*-1);
        heapq.heappush(maxheap,1*-1);
        heapq.heappush(maxheap,11*-1);
        # maxheap=[-11, -8, -10, -2, -1, -9]
        print(f'{maxheap=}')

        #peek
        # 1 
        print(f'{maxheap[0]*-1=}')
        print(f'{len(maxheap)=}')

        # nlargest(2,maxheap) = >maxheap smallest
        print(f'{heapq.nlargest(2,maxheap)=}')
        # nsmallest(1,maxheap) = >maxheap largest
        print(f'{heapq.nsmallest(1,maxheap)=}')


        #Delete
        print(f'{heapq.heappop(maxheap)*-1=}')
        # heapq.heappop(maxheap)

        # Size
        length = len(maxheap)
        print(f'{length=}')

        # Iteration
        while len(maxheap)!=0:
            print(f'{heapq.heappop(maxheap)*-1=}')


if __name__ == '__main__':
    test = Test()
    test.test()