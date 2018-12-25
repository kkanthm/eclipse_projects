package com.company;
import static java.lang.Math.abs;
import static java.lang.Math.sqrt;
import java.lang.*;
import java.util.Random;

public class Main {

    public static void main(String[] args) {
        Random rand=new Random();
        int b=rand.nextInt(10+1-2)+2;
        int c=rand.nextInt(10+1-2)+2;
        int d=rand.nextInt(4+1-2)+2;
        System.out.println("If a="+b+"√"+c+" and 2a=√"+d+"√x, what is the value of x with no decimal places?");
        double a=2*b* sqrt(c);
        double x=(a*a)/d;
        System.out.println("\nAns: x="+(int)(x));







    }
}
