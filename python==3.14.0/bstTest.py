class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(10)
left1, left2, left3 = TreeNode(9), TreeNode(10.5), TreeNode(8)
right1, right2, right3 = TreeNode(11), TreeNode(9.5), TreeNode(12)

root.left, root.right = left1, right1
left1.left, left1.right = left3, right2
right1.right, right1.left = right3, left2

#Determine if the given binary tree is a BST
def isBST(node, smallest = float("-inf"), largest = float("inf")):
    if not node:
        return True
    
    if not (smallest < node.val < largest):
        return False
    
    left = isBST(node.left, smallest, node.val)
    right = isBST(node.right, node.val, largest)

    return left and right

print(isBST(root))

def rangeSum(node, low, high):
    if not node:
        return 0
    
    ans = 0
    if low <= node.val <= high:
        ans += node.val

    if node.val > low:
        ans += rangeSum(node.left, low, high)
    
    if node.val < high:
        ans += rangeSum(node.right, low, high)

    return ans

print(rangeSum(root,8, 11))


def getMinimumDifference(root):
    
    def dfs(node):
        if not node:
            return 
    #Perform inorder dfs to append the values in sorted order
        left = dfs(node.left)
        values.append(node.val)
        right = dfs(node.right)
        
    values = []
    dfs(root)
    ans = float("inf")
    
#Stores the smallet difference value encountered
    for i in range(1, len(values)):
        ans = min(ans, values[i] - values[i -1])
        
    return ans

print(getMinimumDifference(root))

def getMaximumDifference(root):
    
    def dfs(node):
        if not node:
            return
        #In order traversal
        dfs(node.left)
        values.append(node.val)
        dfs(node.right)

    values = []
    dfs(root)
    ans = float("-inf")
    end = len(values) - 1
    start = 0

    while start < end:
        ans = max(ans, values[end] - values[start])
        start += 1
        end -= 1

    return ans

print(getMaximumDifference(root))


def insertInBST(node, target):
    if not node:
        return TreeNode(target)
    
    if target < node.val:
        node.left = insertInBST(node.left, target)
    else:
        node.right = insertInBST(node.right, target)
    
    return node

#Simple conditional that outputs the trees values if the function executed sucessfully
if insertInBST(root, 35):
    def dfs(node):
        if not node:
            return

        print(node.val)

        if node.left:
            dfs(node.left)
        if node.right:
            dfs(node.right)
    
    dfs(root)

