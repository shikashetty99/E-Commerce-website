

import math

import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):

    
    
    list=[]
    for i in range(len(a)):
        for j in range(len(b)):
            if(a[i]==b[j]):
                list.append(a[i])
                b[j]='_'

    print(b)        
    x=len(a)+len(b)-2*len(list)    
    return x       


              
        

    

if __name__ == '__main__':
    

    a = input()

    b = input()
    x=list(a)
    y=list(b)

    res = makeAnagram(x,y)
    print(res)
    


    q = int(input())

    for q_itr in range(q):
        s = input()

        print(s)