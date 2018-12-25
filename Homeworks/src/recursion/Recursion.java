package recursion;

public class Recursion {
	
	public void numbers (int n) {
		if(n==0) {
			System.out.print(0);
		}
		else {
			numbers(n-1);
			System.out.print(n);
			System.out.print(n);
		}
	}
	
	public static void main(String[] args) {
		
		Recursion r = new Recursion();
		r.numbers(5);
		
	}

}
