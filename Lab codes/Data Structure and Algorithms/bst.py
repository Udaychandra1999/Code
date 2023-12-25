class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root


def in_order_traversal(root):
    result = []
    if root:
        result += in_order_traversal(root.left)
        result.append(root.val)
        result += in_order_traversal(root.right)
    return result


def pre_order_traversal(root):
    result = []
    if root:
        result.append(root.val)
        result += pre_order_traversal(root.left)
        result += pre_order_traversal(root.right)
    return result


def post_order_traversal(root):
    result = []
    if root:
        result += post_order_traversal(root.left)
        result += post_order_traversal(root.right)
        result.append(root.val)
    return result


def delete_node(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.val = min_value_node(root.right).val
        root.right = delete_node(root.right, root.val)
    return root


def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current


def construct_bst(elements):
    root = None
    for element in elements:
        root = insert(root, element)
    return root


def main():
    n = int(input())
    elements = list(map(int, input().split()))

    bst_root = construct_bst(elements)

    # In-order traversal
    result_in_order = in_order_traversal(bst_root)
    print(" ".join(map(str, result_in_order)))

    # Pre-order traversal
    result_pre_order = pre_order_traversal(bst_root)
    print(" ".join(map(str, result_pre_order)))

    # Post-order traversal
    result_post_order = post_order_traversal(bst_root)
    print(" ".join(map(str, result_post_order)))

    # Delete node 6
    bst_root = delete_node(bst_root, 6)
    result_after_delete = in_order_traversal(bst_root)
    print(" ".join(map(str, result_after_delete)))

    # Insert node 8
    bst_root = insert(bst_root, 8)
    result_after_insert = in_order_traversal(bst_root)
    print(" ".join(map(str, result_after_insert)))

    # Delete node 5
    bst_root = delete_node(bst_root, 5)
    result_after_second_delete = in_order_traversal(bst_root)
    print(" ".join(map(str, result_after_second_delete)))


if __name__ == "__main__":
    main()
