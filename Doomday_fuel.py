"""
Doomsday Fuel
=============
Making fuel for the LAMBCHOP's reactor core is a tricky process because of the exotic matter involved. It starts as
raw ore, then during processing, begins randomly changing between forms, eventually reaching a stable form. There may
be multiple stable forms that a sample could ultimately reach, not all of which are useful as fuel.
Commander Lambda has tasked you to help the scientists increase fuel creation efficiency by predicting the end state
of a given ore sample. You have carefully studied the different structures that the ore can take and which transitions
it undergoes. It appears that, while random, the probability of each structure transforming is fixed. That is, each
time the ore is in 1 state, it has the same probabilities of entering the next state (which might be the same state).
You have recorded the observed transitions in a matrix. The others in the lab have hypothesized more exotic forms
that the ore can become, but you haven't seen all of them.
Write a function answer(m) that takes an array of array of non-negative ints representing how many times that state
has gone to the next state and return an array of ints for each terminal state giving the exact probabilities of each
terminal state, represented as the numerator for each state, then the denominator for all of them at the end and in
simplest form. The matrix is at most 10 by 10. It is guaranteed that no matter which state the ore is in, there is a
path from that state to a terminal state. That is, the processing will always eventually end in a stable state. The
ore starts in state 0. The denominator will fit within a signed 32-bit integer during the calculation, as long as the
fraction is simplified regularly.
For example, consider the matrix m:
[
    [0,1,0,0,0,1],  # s0, the initial state, goes to s1 and s5 with equal probability
    [4,0,0,3,2,0],  # s1 can become s0, s3, or s4, but with different probabilities
    [0,0,0,0,0,0],  # s2 is terminal, and unreachable (never observed in practice)
    [0,0,0,0,0,0],  # s3 is terminal
    [0,0,0,0,0,0],  # s4 is terminal
    [0,0,0,0,0,0],  # s5 is terminal
]
So, we can consider different paths to terminal states, such as:
s0 -> s1 -> s3
s0 -> s1 -> s0 -> s1 -> s0 -> s1 -> s4
s0 -> s1 -> s0 -> s5
Tracing the probabilities of each, we find that
s2 has probability 0
s3 has probability 3/14
s4 has probability 1/7
s5 has probability 9/14
So, putting that together, and making a common denominator, gives an answer in the form of
[s2.numerator, s3.numerator, s4.numerator, s5.numerator, denominator] which is
[0, 3, 2, 9, 14].
Languages
=========
To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java
Test cases
==========
Inputs:
    (int) m = [
               [0, 2, 1, 0, 0],
               [0, 0, 0, 3, 4],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0]
           ]
Output:
    (int list) [7, 6, 8, 21]
Inputs:
    (int) m = [
               [0, 1, 0, 0, 0, 1],
               [4, 0, 0, 3, 2, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0]
           ]
Output:
    (int list) [0, 3, 2, 9, 14]
"""
"""
Created on Tue May 12 23:45:47 2020

@author: bigbrother
"""
from fractions import Fraction
import math
def HCF(a,b):
    if(b==0):
        return a
    return HCF(b,a%b)
# function to calculate LCM
def LCMofArray(a):
  lcm = a[0]
  for i in range(1,len(a)):
    lcm = lcm*a[i]//math.gcd(lcm, a[i])
  return lcm


def Inverse1(mat):
    
    """  
    for i in range(len(mat)-1,0,-1):
        x=mat[i-1][0][0]/mat[i-1][0][1]
        y=mat[i][0][0]/mat[i][0][1]
        
        if(x<y):
            temp = mat[i]
            mat[i]=mat[i-1]
            mat[i-1]=temp
       """     
            
    for i in range(len(mat)):
        for j in range(len(mat)):
            if(i!=j):
                ratio=mat[j][i]/mat[i][i]
                for k in range(len(mat[0])):
                    mat[j][k]=mat[j][k]-ratio*mat[i][k]
                   
    for i in range(len(mat)):
        divisor=mat[i][i]
        for j in range(len(mat[0])):
           mat[i][j]=mat[i][j]/divisor
    
    return mat                

def multiply(A,B):
    res=[]
    for i in range(len(A)):
        col=[]
        for j in range(len(B[0])):
            sum=0
            for k in range(len(B)):
                sum+=A[i][k]*B[k][j]
            col.append(sum)
        res.append(col)
    return res

def solution(n):
    term,nonter=[],[]
    #nonter=[]
    
    n_deno = []

    for i in range(len(n)):
        flag=0
        sum=0
        
        for j in range(len(n[0])):
            sum+=n[i][j]
            if(n[i][j]!=0 and flag==0):
                nonter.append(i)
                flag=1     
        if(flag==0):
            term.append(i)
        #populating the non terminal with it's probability
        row=[]
        for j in range(len(n[0])):
          
            if(sum!=0):
                row.append(Fraction(n[i][j],sum))
            else:
                row.append(Fraction(n[i][j],1))
        n_deno.append(row)
            
        
    if(len(nonter)==0):
        temp=[1]
        for i in range(len(term)-1):
            temp.append(0)
        temp.append(1)
        return
            
        
    #Got the terminal and the non terminal list
    
    #getting matrix R and Q
    r=[]
    for i in range(len(nonter)):
        c=[]
        for j in range(len(term)):
            c.append(n_deno[nonter[i]][term[j]])
        r.append(c)

    q=[]
    
    for i in range(len(nonter)):
        c=[]
        for j in range(len(nonter)):
            c.append(n_deno[nonter[i]][nonter[j]])
        q.append(c)
    
    #create an identity matrix
    
    for i in range(len(q)):
        row=[]
        for j in range(len(q)):
         
            if(i==j):
        
                q[i][j]=Fraction(1,1)-q[i][j]
                row.append(Fraction(1,1))
                
            else:
                q[i][j]=-q[i][j]
                row.append(Fraction(0,1))
           
        q[i].extend(row)
    #return term,nonter,n_deno,r,q
    T=Inverse1(q)
    F=[]
    for i in range(len(T)):
        row=[]
        for j in range(len(T[0])//2,len(T[0])):
            row.append(T[i][j])
        F.append(row)
        
    ans=multiply(F,r)
    #ans=[[Fraction(0,1),Fraction(7,5),Fraction(1,8)],[Fraction(2,3),Fraction(1,6),Fraction(5,6)]]
    max1=0
    de=[]
    #print(ans)
    for i in range(len(ans[0])):
         de.append(ans[0][i].denominator)
        #max1=max(ans[0][i].denominator,max1)
        
    
    lcm=LCMofArray(de)
    #print(lcm)
    
    final_ans=[]
    for i in range(len(ans[0])):
        fac1=lcm/ans[0][i].denominator
        final_ans.append(int(fac1*ans[0][i].numerator))
    final_ans.append(lcm)  
    return final_ans
    


ans=solution ([
          
         [0, 1, 0, 0, 0, 1],
               [4, 0, 0, 3, 2, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0]
    ])
print(ans)

