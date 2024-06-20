class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class node:
    def __init__(self, Node, HKey):
        self.node = Node
        self.hkey = HKey

def topview(root):        
    temp = node(root, 0) 
    Q = [temp]
    Q.append(None)
    Key_Dict = {}
    while len(Q)!= 0:
        curr = Q.pop(0)
        
        if curr == None:
            if len(Q) == 0:
                break
            else:
                Q.append(None)
        else:
            #if curr.hkey not in Key_Dict.keys():
            Key_Dict[curr.hkey] = curr.node.value
            
            if curr.node.left!= None:
                temp = node(curr.node.left, curr.hkey-1)
                Q.append(temp)
            
            if curr.node.right!= None:
                temp = node(curr.node.right, curr.hkey+1)
                Q.append(temp)
    for i in sorted(Key_Dict):
        print(Key_Dict[i])

if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(8)
    root.left.right.left = Node(9)
    root.left.right.right = Node(10)
    root.right.right.right = Node(11)
    root.left.right.right.left = Node(12)
    root.left.right.right.right = Node(13)
    topview(root)