package com.company;

import java.util.Random;
import java.lang.*;


public class Main {

    public static void main(String[] args) {
        Random rand = new Random();
        float a, b, c, d;
            a = rand.nextFloat() * (4 - 1) + 1;
            b = rand.nextFloat() * (4 - 1) + 1;
            do {
                c = rand.nextFloat() * (4 - 1) + 1;
            }while(a<=c);
            do {
                d = rand.nextFloat() * (4 - 1) + 1;
            }while(d<=b);


            System.out.println("          b=" + a + "+" + b + "x\n");
            System.out.println("          c=" + c + "+" + d + "x\n");
            System.out.println("In the equations above b and c represent price per pound in dollars of beef and chicken\n");
            System.out.println("respectively,  x weeks after July 1. What was price per pound of beef when it was equal to the price of chicken?");

            float x = (a - c) / (d - b);
            float ans = a + (b * x);

            double finalans = Math.round(ans * 10) / 10.0;
        System.out.println("Ans: $" + finalans);

    }
}



