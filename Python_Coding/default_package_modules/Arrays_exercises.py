'''
Maximum Sub Array
T = int(input())

for _ in range(T):
    
    N = int(input())
    arr = list(map(int, input().rstrip().split()))
    maxSubarray = []
    maxSum = 0;
    i=0
    while i < N:
        temparr = []
        while(i<N and arr[i]>0):
            temparr.append(arr[i]);
            i=i+1;
        sumOfTempArr = sum(temparr);
        if(sumOfTempArr>maxSum):
            maxSum = sumOfTempArr;
            maxSubarray = temparr;
        i=i+1;
    print(' '.join(map(str, maxSubarray))) 
    
        
                                            #IF you find a negetive element,append existing list and empty that, then add elements from then 
'''
'''
Majority Element
def getCount(element, thatList):
    count = 0;
    for eachEle in thatList:
        if eachEle == element:
            count = count+1;
    return count;
        
T = int(input())
for _ in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    flag=False;
    maxele = 0;
    for each in arr:
        eleCount = getCount(each, arr);
        if eleCount>(N/2):
            maxele = each
            flag = True;
    if(flag == True):
        print(maxele)
    if(flag==False):
        print(-1);   
'''
'''
#Wave Array

T = int(input())

for _ in range(T):
    
    N=int(input())
    a = list(map(int, input().split()))
    a.sort();
    
    for i in range(0,N-1,2):
        temp = a[i]
        a[i] = a[i+1]
        a[i+1]=temp
    print(' '.join(map(str,a))) 
    
Example :

A : [3 5 4 2]

Output : 2 
for the pair (3, 4)  
    '''
'''
#Maximum Index
T = int(input())

for _ in range(T):
    
    N=int(input())
    arr = list(map(int, input().split()))
    sortedArr = sorted(arr);
    print(sortedArr)
    maximumIndex = 0;
    i,j = 0,N-1;
    while(j>i):
        maximumDifference = arr.index(sortedArr[j])-arr.index(sortedArr[i])
        if(maximumDifference>=maximumIndex):
            maximumIndex = maximumDifference
        i,j=i+1,j-1;
    print(maximumIndex)
#     maximumIndex = 0
#     for i in range(N-1):
#         for j in range(i+1,N):
#             if(arr[i]<=arr[j] and j-i > maximumIndex):
#                 maximumIndex = j-i;
#     print(maximumIndex)

#Max sum path

T = int(input());
for _ in range(T):
    n1, n2 = list(map(int, input().split()))
    firstArray = list(map(int, input().split()))
    secondArray = list(map(int, input().split()))
    totalsum=0;
    i,j,isum,jsum=0,0,0,0;
    while i<n1 and j<n2:
        if(firstArray[i]==secondArray[j]):
            totalsum+=max(isum,jsum)+firstArray[i];
            isum,jsum=0,0;
            i,j=i+1,j+1;
        elif(firstArray[i]<secondArray[j]):
            isum+=firstArray[i]
            i=i+1;
        else:
            jsum+=secondArray[j]
            j=j+1
        
    while(i<n1):
        isum+=firstArray[i];
        i=i+1;
    while(j<n2):
        jsum+=secondArray[j];
        j=j+1;
    totalsum=totalsum+max(isum,jsum)
    print(totalsum)   
Input
2
5
10 3 5 6 2
2
12 20
Output
180 600 360 300 900
20 12 

#Product Array Construction
T=int(input())

for _ in range(T):
    N=int(input())
    arr=list(map(int, input().split()))
    productOfElements=1;
    i=0;
    while i<N:
        productOfElements = productOfElements * arr[i];
        i=i+1
    print(' '.join([str(productOfElements//i) for i in arr])) 
    
'''
#Find Duplicates In Array

''' Please note that it's Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above. 
Input:
2
4
0 3 1 2
5
2 3 1 2 3 
Output:
-1
2 3 


# your task is to complete this function
# function should print all the duplicate elements
def printDuplicates(arr, n):
    # Code here
    flag=False
    for i in range(n):
        index = arr[i]%n
        arr[index]=arr[index]+n
    for i in range(n):
        if(arr[i]//n>1):
            flag=True;
            print(i, end=' ')
    if(flag==False):
        print(-1)
t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    printDuplicates(arr, n)
    print('')

B-twice
A-missing
    
Input
2
2
1 1 
3 
0 2 2
Output
2 1
3 2
0 1 2 1 3
'''
'''
#Find Missing and Repeating
t=int(input())
for i in range(t):
    #A,B=0,0;
    A,B=0,0
    n = int(input())
    arr = list(map(int, input().strip().split()))
    minusOneArr = [i-1 for i in arr];
    for i in range(n):
        index = minusOneArr[i]%n;
        minusOneArr[index]=minusOneArr[index]+n
    for i in range(n):
        if(minusOneArr[i]//n>1):
            B=i+1;
    #print(B)       
    A= (n*n+n)//2 - sum(arr) + B;
    print("{} {}".format(B,A))
Input:
2
7
100 180 260 310 40 535 695
10
23 13 25 29 33 19 34 45 65 67

Output:
(0 3) (4 6)
(1 4) (5 9)
1
89
6764 3645 5181 5893 4542 6753 3996 5483 585 9895 2657 777 1343 4605 261 2225 959 9884 563 4131 6687 7528 6224 436 3333 110 2037 7007 4710 2310 7596 7827 2307 9129 72 3202 2234 4069 5037 2819 3964 7694 9948 5307 8652 6561 7532 9611 6445 8095 94 9484 1975 6319 9920 5308 6429 1958 8668 7491 620 6264 5318 2927 1745 5391 6129 3979 5812 1167 3150 9776 8861 3098 5083 3865 9659 8968 3476 6104 3415 9923 1940 1743 6242 1861 3403 9023 3819
'''
'''
#Stocks Buy and Sell
T=int(input())

for _ in range(T):
    n=int(input())
    arr=list(map(int, input().split()))
    j=0;
    flag=False;
    count=0;
    while j<n-1:
        k=j;
        if(arr[k]<arr[k+1]):
            while(k<n-1 and arr[k]<arr[k+1]):
                k=k+1;
            print("({} {})".format(j,k),end=' ');
            flag=True;
            j=k+1;
        else:
            count=count+1
            j=j+1;
    
    if(flag==False and count>=1):
        print("No Profit")
    print()
        
  
    j=0;
    k=j+1;
    while j < n-1 and k<n:
        if(arr[j]<arr[k]):
            while(k<n and arr[j]<arr[k]):
                k=k+1;
            print("({} {})".format(j,k-1),end=' ');
            j=k;
            
        elif(arr[j]>arr[k]):
            j,k = j+1,k+1;
        
       
'''   

    