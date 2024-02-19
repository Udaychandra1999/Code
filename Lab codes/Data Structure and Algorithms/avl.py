class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.height = 1


def height(node):
    if not node:
        return 0
    return node.height


def balance_factor(node):
    if not node:
        return 0
    return height(node.left) - height(node.right)


def update_height(node):
    if not node:
        return 0
    node.height = 1 + max(height(node.left), height(node.right))
    return node.height


def right_rotate(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    update_height(y)
    update_height(x)

    return x


def left_rotate(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    update_height(x)
    update_height(y)

    return y


def insert(root, key):
    if not root:
        return Node(key)

    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    update_height(root)

    balance = balance_factor(root)

    # Left Heavy
    if balance > 1:
        if key < root.left.val:
            return right_rotate(root)
        else:
            root.left = left_rotate(root.left)
            return right_rotate(root)

    # Right Heavy
    if balance < -1:
        if key > root.right.val:
            return left_rotate(root)
        else:
            root.right = right_rotate(root.right)
            return left_rotate(root)

    return root


def pre_order_traversal(root):
    result = []
    if root:
        result.append(root.val)
        result += pre_order_traversal(root.left)
        result += pre_order_traversal(root.right)
    return result


def in_order_traversal(root):
    result = []
    if root:
        result += in_order_traversal(root.left)
        result.append(root.val)
        result += in_order_traversal(root.right)
    return result


def post_order_traversal(root):
    result = []
    if root:
        result += post_order_traversal(root.left)
        result += post_order_traversal(root.right)
        result.append(root.val)
    return result


def construct_avl_tree(elements):
    root = None
    for element in elements:
        root = insert(root, element)
    return root


def main():
    n = int(input())
    elements = list(map(int, input().split()))

    avl_tree_root = construct_avl_tree(elements)

    # Pre-order traversal
    result_pre_order = pre_order_traversal(avl_tree_root)
    print(" ".join(map(str, result_pre_order)))

    # In-order traversal
    result_in_order = in_order_traversal(avl_tree_root)
    print(" ".join(map(str, result_in_order)))

    # Post-order traversal
    result_post_order = post_order_traversal(avl_tree_root)
    print(" ".join(map(str, result_post_order)))


if __name__ == "__main__":
    main()
