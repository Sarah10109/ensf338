class MinHeap:
    def __init__(self):
        self.heap = []

    def heapify(self, arr):
        self.heap = arr
        start_index = (len(self.heap) - 2) // 2  # Start from the last non-leaf node
        for i in range(start_index, -1, -1):
            self._sift_down(i)

    def enqueue(self, element):
        self.heap.append(element)
        self._sift_up(len(self.heap) - 1)

    def dequeue(self):
        if len(self.heap) == 0:
            raise IndexError("Heap is empty")
        self._swap(0, len(self.heap) - 1)  # Swap the root with the last element
        min_element = self.heap.pop()  # Remove the last element (previous root)
        self._sift_down(0)  # Restore heap property
        return min_element

    def _sift_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.heap[index] < self.heap[parent_index]:
            self._swap(index, parent_index)
            self._sift_up(parent_index)

    def _sift_down(self, index):
        smallest = index
        left_child = 2 * index + 1
        right_child = 2 * index + 2

        if left_child < len(self.heap) and self.heap[left_child] < self.heap[smallest]:
            smallest = left_child

        if right_child < len(self.heap) and self.heap[right_child] < self.heap[smallest]:
            smallest = right_child

        if smallest != index:
            self._swap(index, smallest)
            self._sift_down(smallest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

def is_min_heap(arr):
    n = len(arr)
    # Start from root and go till the last internal node
    for i in range((n - 2) // 2 + 1):
        left = 2 * i + 1
        right = 2 * i + 2
        # Check if left child exists and is greater than parent
        if left < n and arr[i] > arr[left]:
            return False
        # Check if right child exists and is greater than parent
        if right < n and arr[i] > arr[right]:
            return False
    return True

def test_heap_already_sorted():
    min_heap = MinHeap()
    input_array = [1, 2, 3, 4, 5, 6, 7]
    print("Test 1 - Input (Already a Heap):", input_array)
    min_heap.heapify(input_array)
    print("Test 1 - Output (Heapified Array):", min_heap.heap)
    assert is_min_heap(min_heap.heap), "Test 1 Failed: The heap property is not maintained."

def test_empty_array():
    min_heap = MinHeap()
    input_array = []
    print("Test 2 - Input (Empty Array):", input_array)
    min_heap.heapify(input_array)
    print("Test 2 - Output (Heapified Array):", min_heap.heap)
    assert is_min_heap(min_heap.heap), "Test 2 Failed: The heap property is not maintained for an empty array."

def test_long_random_array():
    import random
    min_heap = MinHeap()
    input_array = list(range(10))
    random.shuffle(input_array)
    print("Test 3 - Input (Randomly Shuffled List):", input_array)
    min_heap.heapify(input_array)
    print("Test 3 - Output (Heapified Array):", min_heap.heap)
    assert is_min_heap(min_heap.heap), "Test 3 Failed: The heap property is not maintained for a long, randomly shuffled list."

# Running the tests
test_heap_already_sorted()
test_empty_array()
test_long_random_array()

print("All tests passed!")