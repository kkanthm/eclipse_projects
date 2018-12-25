package com.company;
import java.util.Random;
import java.lang.*;


public class Main {

    public static void main(String[] args) {
        float a,b,c,d;
        Random rand=new Random();
        a=rand.nextFloat() * (3000-1800)+1800;
        do {
            b = rand.nextFloat() * (2600 - 1400) + 1400;
        }while(b>=a);
        d=rand.nextFloat() * (1350-800)+800;
        do{
            c=rand.nextFloat() * (1200-700)+700;
        }while(c>d);



	    System.out.println("AB="+a+"    EB="+b+"     DB="+c+"    CD="+d);
        float x=c/b;
	    float ans=d/x;
	    System.out.println("Ans= "+ans);
    }
}
