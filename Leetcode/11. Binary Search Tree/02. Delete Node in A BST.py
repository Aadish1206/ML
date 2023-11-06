class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def deleteNode(root, key):
    if not root:
        return None

    if key < root.val:
        root.left = deleteNode(root.left, key)
    elif key > root.val:
        root.right = deleteNode(root.right, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            temp = find_min(root.right)
            root.val = temp.val
            root.right = deleteNode(root.right, temp.val)

    return root

def find_min(node):
    current = node
    while current.left:
        current = current.left
    return current


def inorder_traversal(node):
    if not node:
        return
    inorder_traversal(node.left)
    print(node.val, end=" ")
    inorder_traversal(node.right)

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

print("Original BST (in-order traversal):")
inorder_traversal(root)
print("\n")

key_to_delete = 3
root = deleteNode(root, key_to_delete)

print(f"After deleting node (in-order traversal):")
inorder_traversal(root)
