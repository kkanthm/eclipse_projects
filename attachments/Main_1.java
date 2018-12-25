package com.company;
import java.util.Random;
import java.lang.*;


public class Main {

    public static void main(String[] args) {
        Random rand=new Random();
        float x,y,z;
        do {
            x = rand.nextInt(6 + 1 - (-6)) + (-6);
        }while(x%2.0!=0.0 || x==4.0);
        do{
            z = rand.nextInt(30+1-12)+12;
        }while(z%2.0!=0.0);

        System.out.println("               g(x)=ax²+"+z+"\n");
        System.out.println("For the function g defined above, a is a constant and g(4)=8.\n");
        System.out.println("What is the value of g("+x+")?\n");
        float a=(8-z)/(16);
        float ans=(a*(x*x))+z;
        System.out.println("Ans: "+ans);

        }

    }

