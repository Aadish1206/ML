class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root):
    def dfs(node, max_val):
        if not node:
            return 0
        
        good_count = 0
        if node.val >= max_val:
            good_count = 1
        
        max_val = max(max_val, node.val)
        
        left_count = dfs(node.left, max_val) if node.left else 0
        right_count = dfs(node.right, max_val) if node.right else 0
        
        return good_count + left_count + right_count
    
    return dfs(root, float('-inf'))


root1 = TreeNode(3)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root1.left.right = TreeNode(3)
root1.right.left = TreeNode(1)
root1.right.right = TreeNode(5)

print(goodNodes(root1))  


root2 = TreeNode(3)
root2.left = TreeNode(3)
root2.right = None  # Adjusting the node with a value of None
if root2.left:
    root2.left.right = TreeNode(4)
    if root2.left.right:
        root2.left.right.left = TreeNode(2)

print(goodNodes(root2))  


root3 = TreeNode(1)
print(goodNodes(root3))  
