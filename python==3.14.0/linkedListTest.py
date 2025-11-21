class listNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

head = listNode(1)
next1 = listNode(2)
next2 = listNode(3)
next4 = listNode(4)
next5 = listNode(5)
next6 = listNode(3)
#Assigning next values
head.next = next1
next1.next = next2
next2.next = next6
next6.next = next5


def getMiddleVal(root):
    slow = fast = root
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.val

print(getMiddleVal(head))



"""
Implement an algorithm to find the kth to last element of a singly linked list
"""
def kLast(root, k):
    slow = fast = root

    for i in range(k):
        fast = fast.next

    while fast:
        slow = slow.next
        fast = fast.next

    return slow.val

print(kLast(head, 3))

"""
Write code to remove duplicates from an unsorted linked list
"""
def removeDupe(root):
    if not root:
        return
    dummy = root
    slow = root
    fast = root.next
    myDict = {slow.val: True}
    
    while fast:
        if fast.val in myDict:
            slow.next = fast.next
        else:
            myDict[fast.val] =  True

        fast = fast.next
        slow = slow.next

    return dummy
lst = removeDupe(head)
while lst:
    print(lst.val)
    lst = lst.next

def reverseList(root):
    head = root
    prev = None

    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    
    #Return prev because it is the head of the new list
    return prev

reversed = reverseList(head)
print("Reversed list:")
while reversed:
    print(reversed.val)
    reversed = reversed.next