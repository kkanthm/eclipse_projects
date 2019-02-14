package algorithms;

/*
Vijay Reddy Thippana L20469889
COSC 5313 Program #1
Derangement Probability Computation
Used Recursive Algorithm
The program is producing the expected correct outputs

 */
public class DerangementsProblem {

	static long factorial(int n){    
		  if (n == 0)    
		    return 1;    
		  else    
		    return(n * factorial(n-1)); }
	
	public static long derangement(int n) {
		if (n==0) {
			return 1;
		}
		else if (n==1){
			return 0;
		}
		else {
		return (n-1)*(derangement(n-1)+derangement(n-2)); }
	}
	
	public static void main(String args[]) {
		long Dn;
		double Pn;
		
		for(int n=1;n<=20;n=n+1) {
			 Dn=derangement(n);
			 Pn=(double)Dn/factorial(n);
			System.out.println("n="+n+"\tPn="+Pn);
		}
	}
}
