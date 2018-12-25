package com.company;
import java.util.Random;
import java.lang.*;
public class Main {

    public static void main(String[] args) {
	  int x,y;
	  Random rand=new Random();
	  do{
	      x=rand.nextInt(35+1-7)+7;
      }while(x%7!=0);
	  y=x/7;

	  System.out.println("A line in the xy-plane passes through the origin and has a slope of 1/7. Which of \n");
	  System.out.println("the following points lies on the line?");
	  System.out.println("Ans: ("+x+","+y+")");


    }
}
