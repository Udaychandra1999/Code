class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.right_threaded = False  # Indicates whether the right pointer is a thread

def insert(root, key):
    if not root:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def morris_in_order_traversal(root):
    result = []
    current = root

    while current:
        if not current.left:
            result.append(current.val)
            current = current.right if not current.right_threaded else None
        else:
            predecessor = current.left
            while predecessor.right and predecessor.right != current:
                predecessor = predecessor.right

            if not predecessor.right:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                result.append(current.val)
                current = current.right if not current.right_threaded else None

    return result

def construct_threaded_bst(elements):
    root = None
    for element in elements:
        root = insert(root, element)
    return root

def main():
    n = int(input())
    elements = list(map(int, input().split()))

    threaded_bst_root = construct_threaded_bst(elements)

    # Morris in-order traversal
    result_in_order = morris_in_order_traversal(threaded_bst_root)
    print(" ".join(map(str, result_in_order)))

if __name__ == "__main__":
    main()
