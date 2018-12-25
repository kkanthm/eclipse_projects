package ques11.src.com.company;

import java.util.Random;
import java.lang.*;


public class Ques11 {

    
        static Random rand = new Random();
        static float a,b,c,d;
		
        public static String getQuestion() {
            a = rand.nextFloat() * (4 - 1) + 1;
            b = rand.nextFloat() * (4 - 1) + 1;
            do {
                c = rand.nextFloat() * (4 - 1) + 1;
            }while(a<=c);
            do {
                d = rand.nextFloat() * (4 - 1) + 1;
            }while(d<=b);


            return " 2)         b=" + a + "+" + b + "x\n"+"          c=" + c + "+" + d + "x\n"+"In the equations above b and c represent price per pound in dollars of beef and chicken\n"
            +"respectively,  x weeks after July 1. What was price per pound of beef when it was equal to the price of chicken?";
        }
        
        public static String getResult() {
            float x = (a - c) / (d - b);
            float ans = a + (b * x);

            double finalans = Math.round(ans * 10) / 10.0;
        return  Double.toString(finalans);
        }

    
}



