
class Heap:
    def __init__(self, arr, end):
        self.arr = arr
        self.end = end 
        
    def heapify(self, idx):
        if idx >= self.end:
            return 
        big = idx
        left_child = idx*2 + 1
        right_child = idx*2 + 2
        if left_child < self.end and self.arr[left_child] > self.arr[big]:
            big = left_child

        if right_child < self.end and self.arr[right_child] > self.arr[big]:
            big = right_child
        
        if big != idx:
            self.arr[big], self.arr[idx] = self.arr[idx], self.arr[big]
            self.heapify(big)

    def build_heap(self):
        
        for i in range(self.end/2, -1, -1):
            self.heapify(i)

def heap_sort(arr):
    h = Heap(arr, len(arr))
    h.build_heap()

    for i in range(len(arr)-1, 0, -1):
        h.arr[0], h.arr[i] = h.arr[i], h.arr[0]
        h.end = i - 1 
        h.heapify(0)

    print h.arr

if __name__ == "__main__":
    heap_sort([4, 10, 3, 5, 1])
    #h = Heap([4, 10, 3, 5, 1], 5)
    #h.build_heap()
    #print h.arr
