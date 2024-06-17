class Bodmas:
    def __init__(self):
        self.items=[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
bod=Bodmas()
string='[3+7{52/11(3+5)}]'
OB="[{("
CB="]})"
flag=0
for i in string:
    if i in OB:
        bod.push(i)
    if i in CB:
        x=bod.pop()
        if x=="(" and i==")":
            pass
        elif x=="{" and i=="}":
            pass
        elif x=="[" and i=="]":
            pass
        else:
            flag=1
            break
if flag==0 and bod.size()==0:
    print("Valid")
else:
    print("Invalid")
