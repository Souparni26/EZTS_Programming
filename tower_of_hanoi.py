def tower_of_hanoi(n,frm,aux,to):
    if n==0:
        return
    if n==1:
        print(f"Move disk 1 from {frm} to {to}")
        return
    tower_of_hanoi(n-1,frm,to,aux)
    print(f"Move disk {n} from {frm} to {to}")
    ctr[0]+=1
    tower_of_hanoi(n-1,aux,frm,to)
ctr=[0]
n=3
tower_of_hanoi(n,'A','B','C')
print(ctr)