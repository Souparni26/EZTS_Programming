class doublehashing:
    def __init__(self,size):
        self.size=size
        self.table=[None]*size

    def h1(self,k):
        return k%11
    def h2(self,k):
        return 8-(k%8)
    def hash(self,k,i):
        return(self.h1(k)+i*self.h2(k))%11
    def insert(self,k):
        for i in range(self.size):
            pos=self.hash(k,i)
            if self.table[pos] is None:
                self.table[pos]=k
                return pos
        raise Exception("hash table overflow")
    def display(self):
        for i,val in enumerate(self.table):
            print(f"Index {i}: {val}")

hash_table=doublehashing(11)

elements=[20,34,45,70,56,81,104,37,46,39]
for elem in elements:
    hash_table.insert(elem)

hash_table.display()