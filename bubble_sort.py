b=[15,7,23,10,5]
n=len(b)
for j in range(0,n):
    for i in range(0,n-1-j):
        if b[i]>b[i+1]:
            b[i],b[i+1]=b[i+1],b[i]
        else:
            pass
print(b[0])