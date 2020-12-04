# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
    def __init__(self, array):
        # Do not edit the line below.
        self.heap = self.build_heap(array)

    def build_heap(self, array):
        first_parent_idx = ((len(array) - 2) // 2)
        for current_idx in reversed(range(first_parent_idx + 1)):
            self.sift_down(current_idx, len(array) - 1, array)
        
        return array
    
    def sift_down(self, current_idx, end_idx, heap):
        child_one_idx = current_idx * 2 + 1
        while child_one_idx <= end_idx:
            child_two_idx = (current_idx * 2 + 2) if (current_idx * 2 + 2) <= end_idx else float("inf")
            
            if child_two_idx != float("inf") and heap[child_two_idx] < heap[child_one_idx]:
                idx_to_swap = child_two_idx
            else:
                idx_to_swap = child_one_idx
								   

            if heap[idx_to_swap] < heap[current_idx]:
                swap(current_idx, idx_to_swap, heap)
                current_idx = idx_to_swap
                child_one_idx = current_idx * 2 + 1
            else:
                return
    
    def sift_up(self, current_idx, heap):
        parent_idx = ((current_idx - 1) // 2)
        while current_idx > 0 and heap[current_idx] < heap[parent_idx]:
            swap(current_idx, parent_idx, heap)
            current_idx = parent_idx
            parent_idx = ((current_idx - 1) // 2)
    
    def peek(self):
        return self.heap[0]
    
    def remove(self): # always remove the last item
        swap(0, len(self.heap) - 1, self.heap)
        value_to_remove = self.heap.pop()
        self.sift_down(0, len(self.heap) - 1, self.heap)
        return value_to_remove
    
    def insert(self, value):
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1, self.heap)

def swap(idx, jdx, heap):
    heap[idx], heap[jdx] = heap[jdx], heap[idx]


if __name__ == "__main__":
    min_heap = MinHeap([48, 12, 24, 7, 8, -5, 24, 391, 24, 56, 2, 6, 8, 41])
    print(min_heap.heap)






        
