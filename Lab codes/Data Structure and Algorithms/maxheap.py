class MaxHeap:
    def __init__(self):
        self.heap = []

    def heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index] > self.heap[parent_index]:
                # Swap the elements if the child is greater than the parent
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def insert(self, element):
        self.heap.append(element)
        index = len(self.heap) - 1
        self.heapify_up(index)

    def heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        largest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index] > self.heap[largest]:
            largest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index] > self.heap[largest]:
            largest = right_child_index

        if largest != index:
            # Swap the elements if the largest child is greater than the parent
            self.heap[index], self.heap[largest] = self.heap[largest], self.heap[index]
            self.heapify_down(largest)

    def delete_max(self):
        if not self.heap:
            return None

        # Swap the root (max element) with the last element
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        max_element = self.heap.pop()

        # Heapify down from the root to maintain the heap property
        self.heapify_down(0)

        return max_element

    def print_heap(self):
        print(" ".join(map(str, self.heap)))


# Example usage
if __name__ == "__main__":
    # Read the number of elements
    n = int(input())

    # Read the elements to be inserted
    elements = list(map(int, input().split()))

    # Create a max-heap and insert elements
    max_heap = MaxHeap()
    for element in elements:
        max_heap.insert(element)

    # Print the contents of the max-heap
    print("Elements in Max-heap are")
    max_heap.print_heap()

    # Read the element to be deleted
    element_to_delete = int(input())

    # Delete the specified element
    deleted_element = max_heap.delete_max()

    if deleted_element is not None:
        print("Elements in Max-heap after deleting {} are".format(element_to_delete))
        max_heap.print_heap()
    else:
        print("Max-heap is empty after deletion.")
