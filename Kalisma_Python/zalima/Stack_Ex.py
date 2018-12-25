'''
Created on Nov 28, 2018

@author: Krishnakanth M
'''

'''
input
7
6 5 8 4 7 10 9

def isReverseSorted(arr):
    i=0;
    while i< len(arr)-1:
        if(arr[i]<arr[i+1]):
            return False;
        i=i+1;
    return True;

def poisonousPlants(p):
    iterations = 0;
    #lengthOfArray = len(p);
    eachTimeUpdatedList = [p[0]]
    
    while not isReverseSorted(p):
        
        for i in range(1, len(p)):
            if(p[i]<=p[i-1]):
                eachTimeUpdatedList.append(p[i])
        
        p[:]=eachTimeUpdatedList[:];
        eachTimeUpdatedList = [p[0]]
        
        iterations=iterations+1;
             
        
    return iterations

    
    
n = int(input())

p = list(map(int, input().rstrip().split()))

result = poisonousPlants(p)
print(result)
'''
#!/bin/python3


#
# Complete the equalStacks function below.
#
'''
equal stacks
def equalStacks(h1, h2, h3):
    h1.reverse();
    h2.reverse();
    h3.reverse();
    sum1 = sum(h1);
    sum2 = sum(h2);
    sum3 = sum(h3);
    
    while(True):
        
        
        if sum1==0 or sum2==0 or sum3==0:
            return 0;
        
        else:
            
            if(sum1==sum2==sum3):
                return sum1;
            
            else:
                maxSum= max(sum1,sum2,sum3);
                
                if(sum1==maxSum):
                    sum1=sum1-h1.pop();
                
                if(sum2==maxSum):
                    sum2=sum2-h2.pop();
                
                if(sum3==maxSum):
                    sum3=sum3-h3.pop();
    


if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    print(result)

    #fptr.close()
    input
1
5 4 10
4 2 4 6 1
2 1 8 5
'''

'''
Largest Rectangle
def largestRectangle(h):
    maxArea=0;
    s = Stack()
    area=0;
    i=0;
    while(i<len(h)):
        if(s.isEmpty() or h[s.peek()]<=h[i]):
            s.push(i);
            i=i+1;
        else:
            top = s.pop();
            if(s.isEmpty()):
                area = h[top]*i;
            else:
                area = h[top]*(i-s.peek()-1);
        
        if(area>maxArea):
            maxArea=area;
    #i=i+1;
    #print(maxArea)
    while(not s.isEmpty()):
        top = s.pop()
        if(s.isEmpty()):
            area = h[top]*i;
        else:
            area = h[top]*(i-s.peek()-1);
        if(area>maxArea):
            maxArea=area;
    
    return maxArea; 
            
            
    
    
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    print(str(result) + '\n')

#     fptr.close()

#A simple text editor
N=int(input());
st = Stack();
S='';
for i in range(N):
    inputCommandList = list(input().split());
    if(inputCommandList[0]=='1'):
        S=S+inputCommandList[1]
        st.push(S);
    elif(inputCommandList[0]=='2'):
        n=int(inputCommandList[1])
        S=S[:-n]
        st.push(S);
    elif(inputCommandList[0]=='3'):
        print(S[int(inputCommandList[1])-1]);
    else:
        st.pop();
        if not st.isEmpty():
            S=st.peek();
        else:
            S='';
'''
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)
    
'''
stock span problem    
T=int(input())
for i in range(T):
    n=int(input());
    arr=list(map(int, input().split()));
    st=Stack();
    spanArray = [0]*len(arr);
    st.push(0);
    spanArray[0]=1;
    for i in range(1,len(arr)):
        while(not st.isEmpty() and arr[i]>=arr[st.peek()]):
            st.pop();
        if(st.isEmpty()):
            spanArray[i]=i+1;
        elif(arr[i]<arr[st.peek()]):
            spanArray[i]=i-st.peek();
        
        
        st.push(i);
    print(' '.join(map(str, spanArray)))            
        
'''
#stock buy and sell problem:

T=int(input())
for _ in range(T):
    n=int(input());
    arr=list(map(int, input().split()));
    st=Stack();
    st.push(0);
    i=1;
    tick = True;
    while i<n:       
        if(st.isEmpty() or arr[i]>=arr[st.peek()]):
            st.push(i);
            i=i+1;
        elif(arr[i]<arr[st.peek()]):
            fir,sec=-1,st.peek();
            while True:
                st.pop();
                if(st.size()==1):
                    fir=st.peek();
                elif(st.isEmpty()):
                    break;
            if(fir!=-1):
                tick=False;
                print("({} {})".format(fir,sec), end=' ');
    if not st.isEmpty():
        fir,sec=-1,st.peek();
        while True:
            st.pop();
            if(st.size()==1):
                fir=st.peek();
            elif(st.isEmpty()):
                break;
        if(fir!=-1):
            tick=False;
            print("({} {})".format(fir,sec));
    
    if tick:
        print("No Profit")   
                
            

            
