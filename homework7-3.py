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

def sum_of_values(node):
    if node is None:
        return 0  # Якщо вузол порожній, додаємо 0
    
    # Сума всіх значень - це сума значення поточного вузла і сум значень в лівому та правому піддереві
    left_sum = sum_of_values(node.left)
    right_sum = sum_of_values(node.right)
    
    return node.key + left_sum + right_sum

if __name__ == '__main__':
    root = None
    keys = [1, 3, 2, 5, 4, 6, 7]

    for key in keys:
        root = insert(root, key)

    print("Binary Tree:")
    print(root)

    total_sum = sum_of_values(root)
    print("Sum of all values in the Binary Search Tree:", total_sum)
