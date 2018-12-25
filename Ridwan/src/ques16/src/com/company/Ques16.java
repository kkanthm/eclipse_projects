package ques16.src.com.company;

import java.io.*;
import java.util.Random;
import static java.lang.Math.*;

public class Ques16 {
static int x;
    public static void main(String[] args) {
       
        
    }

	public static String getQuestion() {
		// TODO Auto-generated method stub
		
		 Random rand=new Random();
	       x =rand.nextInt(-4+1-(-100))+(-100);
	        System.out.println();
		return "If t>0 and t²"+x+"=0, what is the value of t?\n";
	}

	public static String getResult() {
		// TODO Auto-generated method stub
		double ans = sqrt(abs(x));
      //  System.out.println("Ans: "+ans);
		return Double.toString(ans);
	}
}
