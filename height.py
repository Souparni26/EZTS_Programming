'''class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None

def height(root):
    if root==None:
        return 0
    LH=height(root.left)
    RH=height(root.right)
    return max(LH,RH)+1


if __name__=="__main__":
    root=node(1)
    
    root.left=node(2)
    root.right=node(5)
    
    root.left.left=node(3)
    root.left.right=node(4)
    
    root.right.right=node(6)
    root.left.right.left=node(9)
    root.right.right.left=node(7)
    root.right.right.right=node(8)
    root.left.right.left.right=node(10)
    root.right.right.left.right=node(11)
    root.left.right.left.right.left=node(14)
    root.right.right.left.right.left=node(12)
    root.right.right.left.right.left.right=node(13)
height(root)'''
class node:
    def __init__(self,data):
        self.value=data
        self.left=None
        self.right=None
def Height(root):
    if root==None:
        return 0
    LH=Height(root.left)
    RH=Height(root.right)
    return max(LH,RH)+1
    

if __name__=="__main__":
    root=node(1)
    
    root.left=node(2)
    root.right=node(5)
    
    root.left.left=node(3)
    root.left.right=node(4)
    
    root.right.right=node(6)
    root.left.right.left=node(9)
    root.right.right.left=node(7)
    root.right.right.right=node(8)
    root.left.right.left.right=node(10)
    root.right.right.left.right=node(11)
    root.left.right.left.right.left=node(14)
    root.right.right.left.right.left=node(12)
    root.right.right.left.right.left.right=node(13)
    print(Height(root))
   
