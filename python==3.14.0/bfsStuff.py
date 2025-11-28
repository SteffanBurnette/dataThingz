from collections import deque

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

root = TreeNode(4)
left1 = TreeNode(9)
left2 = TreeNode(5)
left3 = TreeNode(8)
left4 = TreeNode(10)
right1 = TreeNode(3)
right2 = TreeNode(6)
right3 = TreeNode(7)
right4 = TreeNode(2)

root.left = left1
root.right = right1
left1.left = left2
left1.right = right2
right1.left = left3
right1.right = right3
left2.right = right4
right2.left = left4

def rightMost(node):
    if not node:
        return []
    
    queue = deque([node])
    ans = []

    while queue:
        curr_len = len(queue)
        ans.append(queue[-1].val)
        

        for _ in range(curr_len):
            nodes = queue.popleft()

            if nodes.left:
                queue.append(nodes.left)
            if nodes.right:
                queue.append(nodes.right)

    return ans

print(rightMost(root))


def maxDepthSum(node):
    if not node:
        return 0
    next_level = deque([root,])
    
    while next_level:
        #Prepare to store the next level values
        curr_level = next_level
        next_level = deque()
        
        #Will be used to iterate to the last level and store its node
        for node in curr_level:
            #Add child nodes of the current level in the queue for the next level
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
                
    #Will sum all the values in the last level and return it 
    return sum([node.val for node in curr_level])

print(maxDepthSum(root))

def largestValinEachRow(root):
    if not root:
        return []
    
    ans = []
    queue = deque([root])
    

    while queue:
        cur_len = len(queue)
        cur_max = float("-inf")

        for _ in range(cur_len):
            node = queue.popleft()
            cur_max = max(cur_max, node.val)

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        ans.append(cur_max)

    return ans

print(largestValinEachRow(root))

 #end