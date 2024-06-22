class node:
    def __init__(self,data):
        self.val=data
        self.left=None
        self.right=None
        self.height=1

def insert(root,super):
    if not root:
        return node(super)
    if super<root.val:
        root.left=insert(root.left,super)
    else:
        root.right=insert(root.right,super)

    root.height=1+max(ght(root.left),ght(root.right))
    bf=getbf(root)

    #RR Rotation
    if bf>1 and super<root.left.val:
        return rightrotate(root)
    #RL Rotation
    if bf>1 and super>root.left.val:
        root.left=leftrotate(root.left)
        return rightrotate(root)
    #LL Rotation
    if bf<-1 and super>root.right.val:
        return leftrotate(root)
    #LR Rotation
    if bf<-1 and super<root.right.val:
        root.right=rightrotate(root.right)
        return leftrotate(root)
    return root


def ght(root):
    if not root:
        return 0
    return root.height

def getbf(root):
    if not root:
        return 0
    return ght(root.left)-ght(root.right)

def leftrotate(A):
    B=A.right
    temp=B.left

    B.left=A
    A.right=temp

    A.height=1+max(ght(A.left),ght(A.right))
    B.height=1+max(ght(B.left),ght(B.right))

    return B

def rightrotate(A):
    B=A.left
    temp=B.right

    B.right=A
    A.left=temp

    A.height=1+max(ght(A.left),ght(A.right))
    B.height=1+max(ght(B.left),ght(B.right))

    return B   

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

if __name__=="__main__":
    root=None
    vl=[19,99,75,7,21,34,38,27,134,100,29,0,12,17,143]
    for i in vl:
        root=insert(root,i)
    inorder(root)
    
