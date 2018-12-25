package ques12.src.com.company;
import java.util.Random;
import java.lang.*;
public class Ques12 {
	static int x;
	static int y;
    public static void main(String[] args) {
	  
	  

	  System.out.println("3) A line in the xy-plane passes through the origin and has a slope of 1/7. Which of \n");
	  System.out.println("the following points lies on the line?");
	  System.out.println("Ans: ("+x+","+y+")");


    }

	public static String getQuestion() {
		// TODO Auto-generated method stub
		return "3) A line in the xy-plane passes through the origin and has a slope of 1/7. Which of \\n"+"the following points lies on the line?";
	}

	public static String getResult() {
		// TODO Auto-generated method stub
		
		Random rand=new Random();
		  do{
		      x=rand.nextInt(35+1-7)+7;
	      }while(x%7!=0);
		  y=x/7;
		return Integer.toString(x+y);
	}
}
