package com.company;
import java.util.Random;
import java.lang.*;


public class Main {

    public static void main(String[] args) {
        int a,b,c,d,e,f,x,y;
        Random rand=new Random();
            a = rand.nextInt(10 + 1 - 2) + 2;
            b = rand.nextInt(10 + 1 - 2) + 2;
            c = rand.nextInt(10 + 1 - 2) + 2;
            d = rand.nextInt(10 + 1 - 2) + 2;
            e = rand.nextInt(10 + 1 - 2) + 2;
            f = rand.nextInt(10 + 1 - 2) + 2;

        String stra = Integer.toString(a);
        String strb =  "+" + Integer.toString(b);
        String strc = Integer.toString(c);
        String strd = Integer.toString(d);
        String stre =  "+" +Integer.toString(e);
        String strf = Integer.toString(f);

        System.out.println("           "+stra+"x"+strb+"y="+strc+"\n");
        System.out.println("           "+strd+"x"+stre+"y="+strf+"\n");
        System.out.println("What is the solution (x,y) of the system of equations above?\n");
        System.out.println("Your answer should be an integer. For e.g: 1.9 should be 1.");

        x=(b*f-c*e)/(b*d-a*e);
        y=(a*f-c*d)/(a*e-b*d);

        System.out.println("The answer is ("+x+","+y+")");

    }
}
