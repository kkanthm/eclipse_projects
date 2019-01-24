'''
Created on Jan 14, 2019

@author: Krishnakanth M

def fun(n,m,count,tp):
    if count!=1 and n==m:
        print(m)
        return
    
    count=count+1;
    if tp and m>0:
        print(m, end=' ')
        m=m-5
        if m<=0:
            tp=False
    if tp==False:
        print(m,end=' ')
        m=m+5
    
    fun(n,m,count,tp)

t=int(input())
for _ in range(t):
    n=int(input());
    fun(n,n,1,True)
    print()

#Catalan Number
def getCatalan(m):
    if m==0 or m==1:
        return 1;
    count=0;
    
    for i in range(m):
        count= count+getCatalan(i)*getCatalan(m-i-1);
    
    return count;
         
t=int(input())
for _ in range(t):
    n=int(input());
    if n%2 != 0:
        print('invalid');
    else:
        m=n//2
        print(getCatalan(m))
#TowersOfHanoi
def TowersOfHanoi(n,src,target,aux,count):
    if n==1:
        print("Move disk {} from rod {} to rod {}".format(n,src,target))
        
        
        return count+1;
    else:
        count=TowersOfHanoi(n-1, src, aux, target,count);
        print("Move disk {} from rod {} to rod {}".format(n,src,target))
        
        return TowersOfHanoi(n-1, aux, target, src,count+1)
        
t=int(input())
for _ in range(t):
    n=int(input())
    A,B,C = 1,2,3;
    count=0;
    count1=TowersOfHanoi(n, A, C, B,count)
    print(count1)

#Josephus Problem
def josephus(n,k):
    if n==1:
        return 1;
    return (josephus(n-1,k)+k-1)%n + 1;
for _ in range(int(input())):
    nums=list(map(int,input().split()));
    n,k=nums[0],nums[1];
    print(josephus(n,k))
'''
#Recursively remove duplicates
'''
2
geeksforgeek
acaaabbbacdddd

def checkIfAllAdjacentUnique(s):
    i=1;
    n=len(s);
    while(i<n):
        if s[i]==s[i-1]:
            return False;
        i=i+1;
    return True;
    
def rrad(s):
    n=len(s)
    if checkIfAllAdjacentUnique(s):
        print(s)
        return s;
    else:
        newS='';
        i=1
        while(i<n):
            if s[i]!=s[i-1]:
                newS=newS+s[i-1];
            else:
                while i<n and s[i]==s[i-1]:
                    i=i+1;
            i=i+1;
        if s[n-1]!=s[n-2]:
            newS=newS+s[n-1]
        
        rrad(newS)    
                 
t=int(input());       
for _ in range(t):
    string=input().rstrip();
    rrad(string)
1
3
2 3 4
'''
#Possible words from phone digits
'''
def cartesianProduct(listOfStringsTemp, string2):
    somefuckingtemplist=[]
    if len(listOfStringsTemp)==1:
        for eachval in listOfStringsTemp[0]:
            for each in string2:
                somefuckingtemplist.append(eachval+each);
    else:    
        for eachString in listOfStringsTemp:
            for eachValue in string2:
                somefuckingtemplist.append(eachString+eachValue)
    
    return somefuckingtemplist;
            
    return 
def cartesian(l):
    temp=[l[0]]
    for i in range(1,len(l)):
        temp=cartesianProduct(temp,l[i])
    return temp
t=int(input())
for _ in range(t):
    no_of_digits=int(input())
    d={0:'',1:'',2:'ABC',3:'DEF',4:'GHI',5:'JKL',6:'MNO',7:'PQRS',8:'TUV',9:'WXYZ'};
    nums=list(map(int,input().split()));
    listofStrings = [d[each] for each in nums]
    l = cartesian(listofStrings)
    print(' '.join(l))

def floodFillAlgo(screen,x,y,prevColor,newColor,M,N):
    if (x<0 or x>=N or y<0 or y>=M):
        return
    if screen[x][y]!=prevColor:
        return
    
    screen[x][y]=newColor;
    
    floodFillAlgo(screen, x+1, y, prevColor, newColor,M,N)
    floodFillAlgo(screen, x-1, y, prevColor, newColor,M,N)
    floodFillAlgo(screen, x, y+1, prevColor, newColor,M,N)
    floodFillAlgo(screen, x, y-1, prevColor, newColor,M,N)
    
    return screen;

t=int(input())
for _ in range(t):
    N,M = map(int, input().split())
    screen = [[0 for x in range(M)] for y in range(N)];
    temp = list(map(int, input().split()));
    count=-1;
    for i in range(N):
        for j in range(M):
            count=count+1
            screen[i][j]=temp[count];
    x,y,K = map(int, input().split())
    previousColor = screen[x][y];
    newColor = K;
    updatedScreen = floodFillAlgo(screen,x,y,previousColor,newColor,M,N)
    for each in updatedScreen:
        print(' '.join(map(str,each)),end=' ')
    
    print()

def insertAt(p,c,index):
    if index==0:
        return c+p[index:len(p)]
    elif index==len(p):
        return p[0:len(p)]+c;
    else:
        return p[0:index]+c+p[index:len(p)];

def permutations(longStr):
    n=len(longStr)
    extendingList=[longStr[0]];
    
    for each in longStr[1:n]:
        p_list=[]
        for eachEL in extendingList:
            for i in range(n):
                p_list.append(insertAt(eachEL, each, i))
        #print(p_list)
        extendingList = p_list
    return set(extendingList);
t=int(input())
for _ in range(t):
    string = input().rstrip()
    print(' '.join(permutations(string)))


'''
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        