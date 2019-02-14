'''
Created on Jan 23, 2019

@author: Krishnakanth M

def printPat(n):
    string=''
    count=n;
    
    while count>=1:
        p=n;
        while p>=1:
            string=string+(str(p)+' ')*count
            p=p-1;
        string=string+' $'
        count=count-1;
    
    return string;
t=int(input())
for _ in range(t):
    n = int(input());
    print(printPat(n))
    '''
# t=int(input())
# for _ in range(t):
#     num = int(input())
#     for i in range(1,11):
#         print(num*i,end=' ')
#     
#     print()
from lib2to3.pgen2.token import GREATER
'''
def pow(n,r):
    count=1;
    i=1;
    while(i<=r):
        count=count*n;
        i=i+1;
    return count;
    
        
t=int(input());
for _ in range(t):
    a,b = map(int, input().split());
    n=int(input())
    r=b/a;
    print(int(a*pow(r,n-1)))
2
13 4
-15 6

t=int(input());
for _ in range(t):
    N,M = map(int, input().split());
    p,r=abs(N),abs(M)
    q=p//r;
    if p-r*q >= r*(q+1)-p:
        if N<0 or M<0:
            print(-(r*(q+1)))
        else:
            print(r*(q+1))
    else:
        if N<0 or M<0:
            print(-r*q)
        else:
            print(r*q)

def GCD(a,b):
    if b%a==0:
        print(a);
    else:
        k=b%a;
        GCD(k,a);
t=int(input())
for _ in range(t):
    p,q=map(int,input().split());
    if p>q:
        GCD(q,p)
    elif p<q:
        GCD(p,q)
    else:
        print(p)   
 
t=int(input())
for _ in range(t):
    LCM=1;
    p,q=map(int,input().split());
    for i in range(1,q+1):
        if (p*i)%q==0:
            LCM=p*i;
            break;
    GCD = int((p*q)/LCM);
    print('{} {}'.format(LCM,GCD));
   
import math
t=int(input())
for _ in range(t):
    n,r=map(int,input().split())
    if n>=r:
        ncr= math.factorial(n)//(math.factorial(n-r)*math.factorial(r));
    else:
        print(0);
    
    print(ncr%(int(math.pow(10,9)+7)))

#Largest Prime Number
t=int(input())
for _ in range(t):
    N=int(input())
    x=N
    lpf,counter = 1,2;
    while counter>1:
        while x%counter == 0:
            x=x//counter;
            lpf=counter;
        counter=counter+1;
        
        if counter*counter>x:
            if x>1:
                lpf=x;
            break
    print(lpf)

from math import ceil
from math import sqrt 
t=int(input())
for _ in range(t):
    N=int(input())
    sum=0;
    for i in range(1,ceil(sqrt(N))+1):
        if N%i==0:
            sum=sum+i;
    
    if sum==N:
        print(1);
    else:
        print(0)

import math
for _ in range(int(input())):
    n=int(input())
    count=0;
       
    p=math.pow(n,1/3);
    #print(p)
    if p.is_integer():
        if p==1.0:
            p=2;
    else:
        p=math.ceil(p)+1;
    
    for a in range(1,p):
        b3 = n-a*a*a;
        b = int(math.pow(b3,1/3));
        #print(b)
        if b*b*b == b3:
            count=count+1;
    
    print(count)
'''

#Sieve of Eratosthenes | Practice | GeeksforGeeks
'''
for _ in range(int(input())):
    N=int(input())
    arr = [False]*(N+1);
    i=2;
    sum1=0;
    while i<len(arr):
        p=i*i;
        while arr[i]==False and p<=N and p>=i*i:
            if p%i==0:
                arr[p]=True;
            p=p+1;
        if arr[i]==False:
            sum1=sum1+i;    
        i=i+1;
    print(sum1)

import math
for _ in range(int(input())):
    N=int(input());
    if N<=2:
        print(2);
    else:
        p = math.sqrt(N)
        sum1=2;
        if p.is_integer():
            p=int(p);
        else:
            p=math.ceil(p)
        q=3;
        
        while q<=N:
            primeN = True;
            i=2;
            while i<p:
                if q!=i and q%i==0:
                    primeN=False;
                i=i+1;
            if primeN:
                sum1=sum1+q;
            q=q+1;
    
    print(sum1);

def SieveOfEratosthenes(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    sum1=0
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    primesArray=[]
    for p in range(2, n): 
        if prime[p]:
            primesArray.append(p);
    
    return primesArray;
for _ in range(int(input())):
    n=int(input());
    print(SieveOfEratosthenes(n));

def SieveOfEratosthenes(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    primesArray=[]
    for p in range(2, n): 
        if prime[p]:
            primesArray.append(p);
    
    return primesArray;
# for _ in range(int(input())):
#     n=int(input());
#     pairs=[]
#     primesArray = SieveOfEratosthenes(n);
#     for i in range(len(primesArray)-1):
#         if primesArray[i]*primesArray[i]<=n:
#             pairs.append([primesArray[i],primesArray[i]]);
#         for j in range(i+1,len(primesArray)):
#             if primesArray[i]*primesArray[j]<=n:
#                 pairs.append([primesArray[i],primesArray[j]]);
#                 #pairs.append([primesArray[j],primesArray[i]])
#             else:
#                 break;
#     
#     for eachPair in pairs:
#         print(' '.join(map(str,eachPair)),end=' ')
#     
#     print()
for _ in range(int(input())):
    n=int(input());
    pairs=[]
    primesArray = SieveOfEratosthenes(n);
    for i in range(len(primesArray)):
        for j in range(len(primesArray)):
            if primesArray[i]*primesArray[j]<=n:
                pairs.append([primesArray[i],primesArray[j]]);
                #pairs.append([primesArray[j],primesArray[i]])
            else:
                break;
    
    for eachPair in pairs:
        print(' '.join(map(str,eachPair)),end=' ')
    
    print()

for _ in range(int(input())):
    string=input().rstrip();
    oddpos, epos = 'acegikmoqsuwy','bdfhjlnprtvxz';
    d={};
    for each in string:
        if each not in d:
            d[each]=1;
        else:
            d[each]=d[each]+1;
    
    X,Y=0,0;
    for each in string:
        if each in oddpos:
            if d[each]%2!=0:
                Y=Y+1;
        else:
            if d[each]%2==0:
                X=X+1;
    
    if (X+Y)%2==0:
        print('EVEN');
    else:
        print('ODD');
                
   ''' 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    