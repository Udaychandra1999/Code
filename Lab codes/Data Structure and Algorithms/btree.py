class BTreeNode:
    def __init__(self):
        self.keys = [None, None]
        self.children = [None, None, None]

def create_node(key):
    new_node = BTreeNode()
    new_node.keys[0] = key
    return new_node

def insert_b_tree(root, key):
    if root is None:
        return create_node(key)

    if root.keys[1] is None:
        if key < root.keys[0]:
            root.keys[1] = root.keys[0]
            root.keys[0] = key
        else:
            root.keys[1] = key
    else:
        if key < root.keys[0]:
            root.children[0] = insert_b_tree(root.children[0], key)
        elif key > root.keys[1]:
            root.children[2] = insert_b_tree(root.children[2], key)
        else:
            root.children[1] = insert_b_tree(root.children[1], key)

    return root

def traverse_b_tree(root):
    if root:
        traverse_b_tree(root.children[0])
        if root.keys[0] is not None:
            print(root.keys[0], end=' ')
        traverse_b_tree(root.children[1])
        if root.keys[1] is not None:
            print(root.keys[1], end=' ')
        traverse_b_tree(root.children[2])

def main():
    b_tree_root = None

    # n = int(input(""))
    elements = list(map(int, input("").split()))

    for element in elements:
        b_tree_root = insert_b_tree(b_tree_root, element)

    print("", end='')
    traverse_b_tree(b_tree_root)
    print()

if __name__ == "__main__":
    main()
