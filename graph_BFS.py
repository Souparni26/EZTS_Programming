def BFS(G,e):
    Q=[e]
    V={}
    for i in G[e]:
        V[i]=False
    V[e]=True
    while len(Q)!=0:
        curr=Q.pop(0)
        print(curr)
        for i in G[curr]:
            if V[i[1]]==False:
                Q.append(i[1])
                V[i[1]]=True

if __name__=="__main__":
    G={1:[(1,2),(1,3)],
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
       8:False
        
    }
    e=1
    BFS(G,e)
        
