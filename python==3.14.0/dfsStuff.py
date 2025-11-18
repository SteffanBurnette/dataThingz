class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(5)
left1 = TreeNode(1)
right1 = TreeNode(2)
left2 = TreeNode(4)
left3 = TreeNode(3)

root.left = left1
root.right = right1
left1.left = left2
left2.left = left3

def preDFS(node):
    if not node:
        return 0
    
    print(node.val)
    preDFS(node.left)
    preDFS(node.right)

#Expected output: 5 1 4 3 2
print("Preorder DFS:")
preDFS(root)

def maxPath(node):
    if not node:
        return 0
    
    left = maxPath(node.left)
    right = maxPath(node.right)

    return max(left, right) + 1

print("Return longest path to leaf length:")
path = maxPath(root)
print(path)

'''
def minPath(node):
    if not node:
        return 0
    
    left = minPath(node)
    right = minPath(node)

    return min(left, right) + 1
    '''

def pathSum(node, target, cur):
    if not node:
        return False

    if node.left == None and node.right == None:
        return (cur + node.val) == target
    
    cur += node.val
    print(cur) #For Debugging
    
    left = pathSum(node.left, target, cur)
    right = pathSum(node.right, target, cur)

    return left or right

print("Does Path Sum exist at leaf:")
print(pathSum(root, 7, 0))