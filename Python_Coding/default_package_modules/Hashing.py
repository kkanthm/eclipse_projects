'''
Created on Jan 10, 2019

@author: Krishnakanth M
'''
#from collections import namedtuple
'''
#Longest Fibonacci Sequence
T=int(input())
for _ in range(T):
    n=int(input())
    arr=list(map(int, input().split()));
    maxele=max(arr);
    a,b=0,1;
    d={}
    d.setdefault(a);
    d.setdefault(b);
    c=a+b;
    while c<=maxele:
        d.setdefault(c);
        a=b;
        b=c;
        c=a+b;
    
    for each in arr:
        if each in d:
            print(each,end=' ');
 
import collections
record = collections.namedtuple('record','first second sum1')
T=int(input())
for _ in range(T):
    nums=list(map(int, input().split()));
    n,X=nums[0],nums[1];
    arr=list(map(int, input().split()));
    
    d={}
    l1=[]
    for i in range(0,n-1):
        for j in range(i+1,n):
            #d[[i,j]]=arr[i]+arr[j];
            d[arr[i]+arr[j]]=[i,j]
    l1=[]
    for i in range(0,n-1):
        for j in range(i+1,n):
            
            sum1 = arr[i]+arr[j];
            
            if X-sum1 in d:
                p=d[X-sum1];
                if p[0] != i and p[1]!= i and p[0] != j and p[1] != j:
                    l=[arr[p[0]],arr[p[1]],arr[i],arr[j]]
                    l.sort()
                    if l not in l1:
                        l1.append(l);
        
    if len(l1)==0:
        print(-1)
    else:
        for each in l1:
            print(' '.join(map(str,each)),end=' $')            
    print()        
    '''
'''
    l1=[]
    z=[]
    for i in range(0,n-1):
        for j in range(i+1,n):
            o = record(first=i,second=j,sum1=arr[i]+arr[j])
            z.append(o)
    
    for p in range(0,len(z)-1):
        for q in range(p+1,len(z)):
            if z[p][2]+z[q][2]==X:
                if z[p][0]!=z[q][0] and z[p][0]!=z[q][1] and z[p][1]!=z[q][0] and z[p][1]!=z[q][1]:
                    l=[arr[z[p][0]],arr[z[q][0]],arr[z[p][1]],arr[z[q][1]]];
                    l.sort()
                    if l not in l1:
                        l1.append(l);
    
    if len(l1)==0:
        print(-1)
    else:
        for each in l1:
            print(' '.join(map(str,each)),end=' $')            
    print() 
    
T=int(input())
for _ in range(T):
    n=int(input())
    arr=list(map(int, input().split()));
    X=int(input())
    d={}
    for each in arr:
        if each not in d:
            d[each]=1;
        else:
            d[each]=d[each]+1;
    count=0;
    if X==0:
        for each in d:
            if d[each]>1:
                count=count+1;
    else:
        for each in d:
            if X+each in d:
                count=count+1;
    print(count);

T=int(input())
for _ in range(T):
    nums=list(map(int, input().split()));
    n,X=nums[0],nums[1];
    arr=list(map(int, input().split()));
    d={}
    decision='No'
    for each in arr:
        if each not in d:
            d[each]=1;
        else:
            d[each]=d[each]+1;
            
    for each in d:
        if X==each//2 and d[each]>1:
            decision='Yes';
            break;
        else:
            if X-each in d:
                decision='Yes';
                break;
    
    print(decision)

#Winner of an election
t=int(input())
for _ in range(t):
    n=int(input())
    arr=input().rstrip().split()
    d={}
    
    for each in arr:
        if each not in d:
            d[each]=1;
        else:
            d[each]=d[each]+1
    
    maxVotes = max(d.values())
    l=[]
    for name, votes in d.items():
        if votes==maxVotes:
            l.append(name);
    
    print('{} {}'.format(min(l),maxVotes))
              
#Group Anagrams Together
T=int(input())
for _ in range(T):
    n=int(input())
    arr=input().rstrip().split()
    d={}
    l=[]
    for each in arr:
        p=''.join(sorted(each))
        if p not in d:
            d[p]=1;
        else:
            d[p]=d[p]+1;
    for i in d.values():
        l.append(i);
    
    l.sort();
    for each in l:
        if each > 1:
            print(each,end=' ')
    
    print()

import collections
T=int(input())
for _ in range(T):
    nums=list(map(int, input().split()));
    n1,n2=nums[0],nums[1];
    arr1,arr2=list(map(int, input().split())),list(map(int, input().split()));
    d=collections.OrderedDict()
    l=[]
    for each in arr2:
        if each not in d:
            d[each]=1;
    
    for each in arr1:
        if each not in d:
            print(each,end=' ')
    
    print()
    
import collections
T=int(input())
for _ in range(T):
    nums=list(map(int, input().split()));
    n,K=nums[0],nums[1];
    arr=list(map(int, input().split()))
    d=collections.OrderedDict()
    for each in arr:
        if each not in d:
            d[each]=1;
        else:
            d[each]=d[each]+1
    
    for each in d:
        if d[each]==K:
            print(each);
            break;
    else:
        print(-1)

import collections
T=int(input())
for _ in range(T):
    n=int(input());
    arr1,arr2=list(map(int, input().split())),list(map(int, input().split()));
    op=1;
    tick=False;
    d=collections.OrderedDict();
    for each in arr1:
        if each not in d:
            d[each]=1;
        else:
            d[each]=d[each]+1
    for each in arr2:
        if each in d:
            d[each]=d[each]-1;
        else:
            tick=True;
            break;
    if tick:
        print(0);
    else:
        for each in d:
            if d[each]!=0:
                print(0);
                break;
        else:
            print(1)

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()))
    for i in range(n):
        arr[i]=arr[i]-1
    print(arr)
    for i in range(n):
        arr[arr[i]%n] = arr[arr[i]%n]+n;
    print(arr)
    for each in arr:
        if each<n:
            print(0,end=' ');
        else:
            print(each//n,end=' ')
    
    print()

T=int(input())
for _ in range(T):
    n=int(input());
    arr1,arr2=input().rstrip().split(),input().rstrip().split();
    d={}
    order = '!#$%&*@^~'
    for each in arr1:
        if each not in d:
            d[each]=1;
    l=[]    
    for each in arr2:
        if each in d:
            d[each]=d[each]+1;
    for each in order:
        if each in d and d[each]==2:
            l.append(each)
    
    print(''.join(l))
    print(''.join(l))
 
T=int(input())
for _ in range(T):
    nums=list(map(int, input().split()));
    n,K=nums[0],nums[1];
    arr1,arr2=list(map(int, input().split())), list(map(int, input().split()));
    d={}
    for each in arr1:
        if each not in d:
            d[each]=1;
        else:
            d[each]=d[each]+1;
    
    for each in arr2:
        if each in d and d[each]>0:
            d[each]=d[each]-1
        else:
            print('No');
            break;
    else:
        for each in d:
            if d[each]<0:
                print('No')
                break;
        else:
            print('Yes')
'''
T=int(input())
for _ in range(T):
    n=int(input());
    arr=list(map(int,input().split()));
    d={}
    for i in range(n):
        for j in range(n):
            if i==0:
                if arr[j] not in d:
                    d[arr[j]]=1;
            else:
                if arr[n*i+j] in d and d[arr[n*i+j]]==i:
                    d[arr[n*i+j]]=i+1;
    
    
    count=0;
    for each in d:
        if d[each]==n:
            count=count+1;
    
    print(count)
        
                    
        
