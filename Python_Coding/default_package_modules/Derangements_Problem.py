'''
Created on Sep 6 2019
@author: Manohar Goud Balagonu
Analysis of Algorithms Program #1
Derangement Probability Computation
Recursive Algorithm
The program is producing the expected correct outputs
'''
import math

def computeDn(n):
    if n==0:
        return 1;
    elif n==1:
        return 0;
    else:
        return (n-1)*(computeDn(n-1)+computeDn(n-2));

if __name__=='__main__':
    for n in range(1,21):
        Dn = computeDn(n);
        Pn = Dn/math.factorial(n);
        print('n={0}\tDn={1:<18d}\tPn={2:.20f}'.format(n,Dn,Pn))
        
        
    
