'''
Created on Jan 25, 2019

@author: Krishnakanth M
'''

'''
1
5
1 0 0 1 0 

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()));
    
    
    count1 = 0;
    for i in range(0,n):
        if arr[i]==0:
            arr[i]=1;
        else:
            count1=count1+1;
            arr[i]=-1;
    curr_max=arr[0];
    max_forever=arr[0];
    for i in range(0,n):
        curr_max = max(arr[i],curr_max+arr[i]);
        max_forever = max(curr_max,max_forever);
    
    print(max_forever+count1)

#GameofXOR
for _ in range(int(input())):
    n=int(input())
    arr=list(map(int, input().split()));
    res=0;
    if n%2==0:
        print(0)
    
    else:
        for i in range(0,n,2):
            res=res^arr[i];
    
        print(res);

import math
def Log2(x): 
    return (math.log10(x) / math.log10(2));
for _ in range(int(input())):
    number=int(input())
    res=Log2(number);
    if res.is_integer():
        print(int(res))
    else:
        print(-1)

for _ in range(int(input())):
    number=int(input())
    b='';
     
    if len(bin(number))%2==0:
        b = bin(number)[2:]
    else:
        b='0'+bin(number)[2:];
    b = list(b);
    for i in range(0, len(b),2):
        b[i],b[i+1]=b[i+1],b[i];
    b = ''.join(b)
    print(int('0b'+b,2));

#PowerOf2
for _ in range(int(input())):
    number=int(input());
    b = bin(number)
    countof1 = 0;
    for each in  b[2:]:
        if each=='1':
            countof1=countof1+1;
        
        if countof1>1:
            print('NO');
            break;
    
    else:
        print('YES')

2
5
1 2 3 5
10
1 2 3 4 5 6 7 8 10

for _ in range(int(input())):
    n=int(input())
    arr=list(map(int, input().split()));
    sumofn = sum(list(range(n+1)));
    missing = sumofn-sum(arr)
    print(missing)
2
6 6
1 2 3 4 7 9
0 1 2 1 1 4
5 7
4 8 7 5 1
4 48 3 0 1 1 5

#ReverseBits
def giveMeReverseNumber(n):
    if n==0:
        return 0;
    binnum = bin(n)[2:].rjust(32,'0');
    rev = str(''.join(list(reversed(binnum))))
    #print(rev)
    return int(rev,2)
    
    return 
for _ in range(int(input())):
    number=int(input())
    print(giveMeReverseNumber(number))
'''
import math
for _ in range(int(input())):
    n=int(input())
    string = input();
    Nsubsets=int(math.pow(2,n))
    subsetList = []
    for i in range(Nsubsets):
        binarystring = ('{0:b}'.format(i)).rjust(n,'0')
        #print(binarystring)
        subs=''
        for i in range(len(binarystring)):
            if binarystring[i]=='1':
                subs=subs+string[n-1-i]
        if subs!='':
            subsetList.append(subs[::-1])  
        
    print(' '.join(sorted(subsetList)))      
                
                
    
    
    
    

            



























