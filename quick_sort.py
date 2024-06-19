
def divide(L,Low,High):
    p=L[High]
    pi=High
    j=Low-1
    for i in range(Low,High):
        if L[i]<=p:
            j+=1
            L[i],L[j]=L[j],L[i]
    j+=1
    L[j],L[pi]=L[pi],L[j]
    pi=j
    return pi
def Quick_sort(L,Low,High):
    if Low<High:
        pi=divide(L,Low,High)
        Quick_sort(L,Low,pi-1)
        Quick_sort(L,pi+1,High)
    return
if __name__=='__main__':
    L=list(map(int,input().split()))
    Quick_sort(L,0,len(L)-1)

    print("Sorted array:",L)
    


