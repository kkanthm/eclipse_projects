'''
Created on Dec 25, 2018

@author: Krishnakanth M
'''
'''
Palindrome
T=int(input())
for _ in range(T):
    strlen = int(input());
    str1 = input()
    i=0;
    j=strlen-1;
    decision = "Yes"
    while(i<j):
        if(str1[i]==str1[j]):
            i=i+1;
            j=j-1;
        else:
            decision = "No";
            break;
    print(decision);


#Anagram
T=int(input())
for _ in range(T):
    string1,string2 = input().split();
    decision = "YES"
    for each in string1:
        if each not in string2:
            decision = "NO";
    print(decision)
    

#Anagram Palindrome
T=int(input())
for _ in range(T):
    d = {}
    string = input();
    strlen = len(string);
    for eachChar in string:
        if eachChar in d:
            d[eachChar]=d[eachChar]+1;
        else:
            d[eachChar]=1;
    oddcount=0;
    for eachLetter in d:
        if d[eachLetter]%2==1:
            oddcount=oddcount+1;
    
    if oddcount>1:
        print("No")
    else:
        print("Yes")
'''
'''
#Title case conversion
T=int(input())
for i in range(T):
    string = input();
    print(string.title());
2
geeks
for
    #
T=int(input())
for i in range(T):
    string = input()
    print(''.join(reversed(sorted(string))))
    2
Hello Bye
abc def

#Merge the two Strings
#import itertools
T=int(input());
for _ in range(T):
    str1, str2 = input().split();
    n1,n2 = len(str1),len(str2);
    mergedString='';
    i,j=0,0;
    while (i<n1 and j<n2):
        mergedString=mergedString+str1[i];
        mergedString=mergedString+str2[j];
        i,j=i+1,j+1;
    while(i<n1):
        mergedString=mergedString+str1[i];
        i=i+1;
    while(j<n2):
        mergedString=mergedString+str2[j];
        j=j+1;
    print(mergedString)
        
T=int(input())
for _ in range(T):
    strlen = int(input());
    str1 = input()
    i=0;
    j=strlen-1;
    decision = "Yes"
    while(i<j):
        if(str1[i]==str1[j]):
            i=i+1;
            j=j-1;
        else:
            decision = "No";
            break;
    print(decision);
# Save Ironman
T=int(input());
for _ in range(T):
    string = input();
    str1 = ''
    for each in string:
        if each.isalpha() or each.isdigit():
            str1 = str1+each;
    strlen = len(str1);
    #print(strlen)
    i=0;
    j=strlen-1;
    decision = "Yes"
    while(i<j):
        if(str1[i].lower()==str1[j].lower()):
            i=i+1;
            j=j-1;
        else:
            decision = "No";
            break;
    print(decision);
2
aeioup??
bcdaeiou??
 
#GoodorBadString
t=int(input());
for _ in range(t):
    vowel = 'aeiou'
    vcount,ccount=0,0;
    string = input().rstrip();
    decision=1;
    for eachChar in string:
        if eachChar=='?':
            vcount=vcount+1;
            ccount=ccount+1;
        elif eachChar in vowel:
            vcount=vcount+1;
            ccount=0;
        else:
            ccount=ccount+1;
            vcount=0;
        
        if vcount>5 or ccount>3:
            decision=0;
            break;
    
    print(decision);
    

URLifytheString - replacing spaces with %20
t=int(input());
for _ in range(t):
    string=list(input().rstrip());
    
    input()
    n = len(string);
    spaceCount=0;
    for each in string:
        if each==' ':
            spaceCount=spaceCount+1;
    
    for i in range(spaceCount*2):
        string.append('?');
    lenOfURLString = len(string);
    j=lenOfURLString-1;
    i=n-1;
    while i>=0 and j>=0:
        if string[i]!=' ':
            string[j]=string[i];
            i,j=i-1,j-1;
        else:
            string[j]='0'
            string[j-1]='2'
            string[j-2]='%'
            i=i-1;
            j=j-3;
    print(''.join(map(str,string)));
3
100klh564abc365bg
abvhd9sdnkjdfs
abchsd0sdhs        
   
#maximum number extracting
T=int(input())
for _ in range(T):
    string=input();
    n=len(string)
    i=0;
    maxNum = 0
    number = '';
    while(i<n):
        
        if string[i].isdigit():
            number=number+string[i];
        else:
            number=''
        
        i=i+1;
        #number=int(number);
        if number!='':
            maxNum = max(int(number),maxNum);
    
    print(maxNum);
2
i.like.this.program.very.much
pqr.mno
 
#reverse words in a given string
T=int(input())
for _ in range(T):
    stringList=input().split('.');
    n=len(stringList)
    #newOne=[None]*n
    for i in range(n//2):
        stringList[i], stringList[n-i-1] = stringList[n-i-1], stringList[i];
    
    print('.'.join(stringList))
  
#Subsequence String
T=int(input());
for i in range(T):
    str1, str2 = input().split();
    len1, len2 = len(str1), len(str2);
    i,j=0,0;
    while i<len1 and j<len2:
        if str1[i].lower()==str2[j].lower():
            i,j=i+1,j+1;
        else:
            j=j+1;
    
    if i==len1:
        print(1);
    else:
        print(0)
       
#Rotation String
T=int(input());
for i in range(T):
    string1 = input().rstrip();
    string2 = input().rstrip();
    if len(string1)!=len(string2):
        print(0);
    temp = string1+string1;
    if string2 in temp:
        print(1);
    else:
        print(0);


def areKAnagrams(str1, str2, k):
    n=len(str1);
    if n!=len(str2):
        return 0;
    count=0;
    alphabet_array=[0]*26;
    for eachChar in str1:
        p=eachChar-'a';
        alphabet_array[p]=alphabet_array[p]+1;
    for eachChar in str2:
        q=eachChar-'a';
        if alphabet_array[q]>0:
            alphabet_array[q]=alphabet_array[q]-1;
        else:
            count=count+1;
        
        if count>k:
            return 0;
    
    return 1;
t = int(input())
for i in range(t):
    arr = input().strip().split()
    k = int(input())
    if areKAnagrams(arr[0], arr[1], k):
        print(1)
    else:
        print(0)
# Contributed By: Harshit sidhwa

Please note that its Function problem i.e.
you need to write your solution in the form of Function(s) only.
Driver Code to call/invoke your function is mentioned above.

# Your task is to complete this function
# Function should return 1/0 or True/False

    # Code here

#Uncommon Characters
T=int(input());
for _ in range(T):
    str1, str2 = input().rstrip(),input().rstrip();
    n1, n2 = len(str1),len(str2)
    opstring = '';
    aa1,aa2 = [0]*26,[0]*26;
    for each in str1:
        p=ord(each)-ord('a');
        aa1[p]=aa1[p]+1;
    for each in str2:
        q=ord(each)-ord('a');
        aa2[q]=aa2[q]+1;
    
    for i in range(len(aa1)):
        if (aa1[i]==0 and aa2[i]>0):
            opstring=opstring+chr(ord('a')+i);
        elif (aa1[i]>0 and aa2[i]==0):
            opstring=opstring+chr(ord('a')+i);
    
    print(''.join(sorted(opstring)))
 
#Anagram Search         
T=int(input());
for _ in range(T):
    aa = [0]*26;
    count=0;
    badaString = input().rstrip();
    chotaString = input().rstrip();
    for each in badaString:
        p = ord(each)-ord('a');
        aa[p]=aa[p]+1;
    for each in chotaString:
        q= ord(each)-ord('a');
        aa[q]=aa[q]-1
    
    for each in aa:
        if each != 0:
            count=count+abs(each);
            
    print(count);

#Checking Repeated Character
T=int(input());
for _ in range(T):
    string=input();
    aa=[0]*26;
    for each in string:
        p=ord(each)-ord('a');
        aa[p]=aa[p]+1;
        
        if aa[p] > 1:
            print(each);
            break;
    else:
        print(-1)

#First Non Repeating Character
# 3
# 5  
# hello
# 12
# zxvczbtxyzvy
# 6
# xxyyzz
t=int(input());
for _ in range(t):
    n = int(input());
    string = input();
    
    aa=[0]*26;
    for each in string:
        p=ord(each)-ord('a');
        aa[p]=aa[p]+1;
    for each in string:
        q=ord(each)-ord('a');
        if(aa[q]==1):
            print(each);
            break;
    else:
        print(-1)

# 2
# abababcdefababcdab
# geeksforgeeks
#Longest Distinct Characters in a String     
t=int(input());
for _ in range(t):
    string=input();
    n=len(string);
    d={}
    maxi,count = 0,0;
    i=0;
    while i<n:
    #for each in string:
        if string[i] not in d:
            d[string[i]]=i;
            count=count+1;
            i=i+1;
        else:
            
            i=d[string[i]]+1;
            d={};
            if count>=maxi:
                maxi=count;
            count=0
    if count>=maxi:
        maxi=count;
    print(maxi)
'''
# def findLongestPalindromicString(text):
#     return
# t = int(input());
# for _ in range(t):
#     findLongestPalindromicString(input().strip())
'''
def findLongestPalindromicString(text):
    
    n = len(text) 
    table = [[0 for x in range(n)] for y in range(n)]  

    maxLength = 1
    i = 0
    while (i < n) : 
        table[i][i] = True
        i = i + 1
    start = 0
    i = 0
    while i < n - 1 : 
        if (text[i] == text[i + 1]) : 
            table[i][i + 1] = True
            start = i 
            maxLength = 2
        i = i + 1
      
    k = 3
    while k <= n : 
     
        i = 0
        while i < (n - k + 1) :  
            j = i + k - 1
            if (table[i + 1][j - 1] and 
                      text[i] == text[j]) : 
                table[i][j] = True
      
                if (k > maxLength) : 
                    start = i 
                    maxLength = k 
            i = i + 1
        k = k + 1
    print(text[start:(start+maxLength)])
    #printSubStr(st, start, start + maxLength - 1)
    
#     n=len(text);
#     table = [[0]*n]*n;
#     
#     maxlen=1;
#     #keeping all i,i s as True; means substrings of length 1 are making True
#     i = 0
#     while (i < n) : 
#         table[i][i] = True
#         i = i + 1
#     #substrings of length 2 are being made True if they both are equal
#     i=0;
#     start=0;
#     while i < n-1:
#         if text[i]==text[i+1]:
#             table[i][i+1]=True;
#             start=i;
#             maxlen=2;
#         i=i+1;
#     
#     # substrings of len 3 or above
#     k=3
#     while k <= n:
#         p=0;
#         while p < (n-k+1):
#             e = p+k-1;
#             if (table[p+1][e-1] and text[p]==text[e]):
#                 table[p][e]=True;
#                 if k > maxlen:
#                     start = p;
#                     maxlen= k;
#             p=p+1;
#         k=k+1;
#                 
#             
#         
#     print(start)
#     print(maxlen)
#     print(text[start:start+maxlen])
    
    
    
    
    
t = int(input())
for _ in range(t):
    findLongestPalindromicString(input().strip())

'''
#Minimum window substring
def EveryEleZeroOrNegetive(d):
    for each in d:
        if d[each] > 0:
            return False;
    return True;
# def getSub(somestring,begin,end):
#     
#     return somestring[begin:end+1];
'''
def minWindowSubstring(B,S):
    d={};
    n=len(B)
    sublen=n;
    #Ans='';
    for each in S:
        if each in d:
            d[each]=d[each]+1
        else:
            d[each]=1;
    begin,end=0,0;
    
    while(end<n):
        endchar=B[end];
        if endchar in d:
            d[endchar]=d[endchar]-1;
        
        end=end+1;
        while EveryEleZeroOrNegetive(d):
            if (end-begin) < sublen:
                sublen=end-begin;
                Ans=B[begin:end]
                #print(Ans)
                
            
            beginchar=B[begin];
            if beginchar in d:
                d[beginchar]=d[beginchar]+1;
            begin=begin+1;
                
        
    if Ans=='':
        print(-1)
    else:
        print(Ans)
    
T=int(input())
for _ in range(T):
    B=input().rstrip();
    S=input().rstrip();
    minWindowSubstring(B,S);

#find missing positive number
T=int(input())
for _ in range(T):
    n=int(input())
    
    arr = list(map(int,input().split()));
    for each in arr:
        if each>0:
            break;
    else:
        print(1);
    
    if n==1:
        if arr[0]==1:
            print(2);
        else:
            print(1);
    
    maxele = max(arr);
    l=[0]*maxele;
    
    for i in range(n):
        if arr[i]>0:
            if l[arr[i]-1]!=1:
                l[arr[i]-1]=1;
    
    for j in range(len(l)):
        if l[j]==0:
            print(j+1);
            break;
    else:
        print(j+2);
1
6 5 8
1 5 10 20 40 80
6 7 20 80 100
3 4 15 20 30 70 80 120
'''
#common numbers
'''
for _ in range(int(input())):
    input();
    arr1=list(map(int,input().split()));
    arr2=list(map(int,input().split()));
    arr3=list(map(int,input().split()));
    d={}
    for each in arr1:
        d[each]=1;
    for each in arr2:
        if each in d:
            if d[each]==1 or d[each]==2:
                d[each]=2;
    for each in arr3:
        if each in d:
            if d[each]==2 or d[each]==3:
                d[each]=3;
    
    for each in d:
        if d[each]==3:
            print(each,end=' ')

'''        
            

    
    