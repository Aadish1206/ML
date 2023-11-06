class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxLevelSum(root):
    if not root:
        return 0

    max_sum = float('-inf')
    level = 1
    max_level = 1

    queue = [root]

    while queue:
        level_sum = 0
        next_level = []

        for node in queue:
            level_sum += node.val

            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        if level_sum > max_sum:
            max_sum = level_sum
            max_level = level

        queue = next_level
        level += 1

    return max_level


root = TreeNode(1)
root.left = TreeNode(7)
root.right = TreeNode(0)
root.left.left = TreeNode(7)
root.left.right = TreeNode(-8)

print(maxLevelSum(root))
