class BinaryTreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self, level=0, prefix="Root: "):
        ret = "\t" * level + prefix + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1, "L--- ")
        if self.right:
            ret += self.right.__str__(level + 1, "R--- ")
        return ret

def insert(root, key):
    if root is None:
        return BinaryTreeNode(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def find_max_value(node):
    if node is None:
        return None  # Якщо дерево порожнє, повертаємо None
    
    current = node
    # Максимальне значення завжди буде в найправішому вузлі
    while current.right:
        current = current.right
    return current.key

if __name__ == '__main__':
    root = None
    keys = [1, 3, 2, 5, 4, 6, 7]

    for key in keys:
        root = insert(root, key)

    print("Binary Tree:")
    print(root)

    max_value = find_max_value(root)
    print("Maximum value in the Binary Search Tree:", max_value)
