'''
Created on Jan 9, 2019

@author: Krishnakanth M
'''
#Floor Squareroot
'''
# Your code goes here
def floorsqrt(n):
    if n==0 or n==1:
        return n;
    
    start=1;
    end=n;
    
    
    
    while start<=end:
        mid=(start+end)//2;
        if mid*mid==n:
            return mid;
        elif mid*mid < n:
            start=mid+1;
            ans=mid
        else:
            end=mid-1;
            
    return ans
    
t = int(input())
for i in range(t):
    n = int(input())
    print(floorsqrt(n))


#missing number in the AP
def findMissing(arr,start,end,diff):
    if(end<=start):
        return
    mid=start+(end-start)//2;
    
    if (arr[mid+1]-arr[mid])!=diff:
        return (arr[mid]+diff);
    if mid>0 and (arr[mid]-arr[mid-1])!=diff:
        return arr[mid-1]+diff;
    
    if arr[mid]==(arr[0]+(diff*mid)):
        return findMissing(arr,mid+1,end,diff);
    
    return findMissing(arr,start,mid-1,diff);
    
    
for i in range(int(input())):
    n=int(input())
    arr=list(map(int,input().split()));
    diff=(arr[n-1]-arr[0])//n;
    print(findMissing(arr, 0, n-1, diff));


#Searching an element in the sorted and rotated array
def search(arr,start,end,pivot):
    if start>end:
        return -1;
    mid=(start+end)//2;
    if pivot==arr[mid]:
        return mid;
    if(arr[start]<arr[mid]):
        if pivot>arr[start] and pivot<arr[mid]:
            return search(arr,start,mid-1,pivot);
        else:
            return search(arr,mid+1,end,pivot);
    else:
        if pivot<arr[end] and pivot>arr[mid]:
            return search(arr,mid+1,end,pivot);
        else:
            return search(arr,start,mid-1,pivot);
        
        
    return
for _ in range(int(input())):
    n=int(input());
    arr=list(map(int,input().split()));
    pivot=int(input());
    print(search(arr,0,n-1,pivot))

#Number of occurences in a sorted array
def binarysearch(arr,start,end,pivot):
    
    while start<=end:
        
        mid=start+(end-start)//2;
        
        if arr[mid]==pivot:
            return mid;
        
        if arr[mid]<pivot:
            start=mid+1;
        
        if arr[mid]>pivot:
            end=mid-1;
    
    
    return -1;
def count(arr,pivot,n):
    ind=binarysearch(arr,0,n-1,pivot);
    if ind==-1:
        return -1;
    
    count=1;
    left=ind-1;
    right=ind+1;
    #calculate left
    while left!=0 and arr[left]==pivot:
        count=count+1;
        left=left-1;
    while right!=(n-1) and arr[right]==pivot:
        count=count+1;
        right = right+1;
    
    return count;
T=int(input());
for _ in range(T):
    nums=list(map(int,input().split()));
    n,pivot=nums[0],nums[1];
    arr=list(map(int,input().split()));
    print(count(arr,pivot,n))
'''
#Floor in sorted array
def findFloor(arr,start,end,pivot):
    while(start<=end):
        mid=start+(end-start)//2
        
        if arr[mid]<=pivot:
            if arr[mid+1]>pivot:
                return mid;
            return findFloor(arr,mid+1,end,pivot)
        if arr[mid]>pivot:
            return findFloor(arr,0,mid-1,pivot)
    return -1;
T=int(input());
for _ in range(T):
    nums=list(map(int,input().split()));
    n,pivot=nums[0],nums[1];
    arr=list(map(int,input().split()));
    print(findFloor(arr,0,n-1,pivot))
    
    
    
    
    
    
    