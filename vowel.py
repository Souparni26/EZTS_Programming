'''no_players=int(input("Enter the number of players:"))
count=[]
for i in range(0,no_players):
    sentence=input("Enter the sentence:")
    n=len(sentence)
    count.append(sentence)
vowels=['a','e','i','o','u']
r=len(count)
result=[]
for k in range(0,r):
    for i in range(0,n):
            if sentence[i] in vowels:
                result.append(sentence[i])
print(result)'''

def count_vowel(s):  #input is a list of list
    dic={"A":0,"E":1,"I":2,"O":3,"U":4}
    for i in s:
        if i=='a' or i=="A":
            dic['A']+=1
        elif i=='E' or i=="e":
            dic['E']+=1
        elif i=='I' or i=="i":
            dic['I']+=1
        elif i=='O' or i=="o":
            dic['O']+=1
        elif i=='U' or i=="u":
            dic['U']+=1
    x=max(dic.values()) #count the maximum occurence of vowels
    result=[]
    for i,j in dic.items():
        if j==x:
            result.append(i) #return the result in list as of key of that value
    return result

l_p=[["jade","hi how are you"],["jack","i am fine"],["reta","such a nice weather"]]
o_p={}
for i in l_p:
    o_p[i[0]]=count_vowel(i[1]) #{i[0]=key,i[1]=value} 
print(o_p)            



