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
'''

#Anagram
T=int(input())
for _ in range(T):
    string1,string2 = input().split();
    decision = "YES"
    for each in string1:
        if each not in string2:
            decision = "NO";
    print(decision)
    
            