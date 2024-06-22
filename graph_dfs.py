def DFS(A,V,S,E):
    if V[E]==False:
        S.append(E)
        V[E]=True
    else:
        return
    for i in A[E]:
        DFS(A,V,S,i[1])
    print(S.pop())



if __name__=="__main__":
    A={1:[(1,2),(1,3)],
       2:[(2,1),(2,7)],
       3:[(3,1),(3,6),(3,5)],
       4:[(4,7),(4,8)],
       5:[(5,3),(5,7)],
       6:[(6,3),(6,8)],
       7:[(7,2),(7,5),(7,4)],
       8:[(8,4),(8,6),(8,8)]}
    V={1:False,
       2:False,
       3:False,
       4:False,
       5:False,
       6:False,
       7:False,
       8:False}
    S=[]
    E=1
    DFS(A,V,S,E)


    