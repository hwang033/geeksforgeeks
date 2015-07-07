import pdb
#Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
#Calling next() will return the next smallest number in the BST.
#1. using stack to do this 
#2. changing tree structure, add pointer to its parent node.
# the same question with CCI 4.5
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class TreeIter(object):
    def __init__(self, root):
        self.root = root
        self.cur = root
        while self.cur.left is not None:
            self.cur = self.cur.left

    def has_next(self):
        return self.cur != None

    def next(self):
        #if cur has right subtree 
        rst = self.cur
        if self.cur.right != None:
            self.cur = self.cur.right
            while self.cur.left is not None:
                self.cur = self.cur.left
        else:
            # if cur is root
            if self.cur.parent == None:
                self.cur = self.cur.parent
            # if cur in left sub tree
            elif self.cur.parent.left == self.cur:
                self.cur = self.cur.parent
            # if cur in right sub tree
            else:
                while self.cur.parent != None and \
                    self.cur.parent.right == self.cur:
                    self.cur = self.cur.parent    
                self.cur = self.cur.parent
        return rst

if __name__ == "__main__":
    t1 = TreeNode(1)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t6 = TreeNode(6)
    t7 = TreeNode(7)
    t8 = TreeNode(8)
    t10 = TreeNode(10)
    t13 = TreeNode(13)
    t14 = TreeNode(14)

    t8.left = t3
    t8.right = t10
    t3.parent = t8
    t10.parent = t8
            
    t3.left = t1
    t3.right = t6
    t1.parent = t3
    t6.parent = t3

    t10.right = t14
    t14.parent = t10
    
    t14.left = t13
    t13.parent = t14

    #pdb.set_trace()
    ti = TreeIter(t8)
    while ti.has_next():
        print ti.next().val

