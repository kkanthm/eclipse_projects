package com.company;

import java.io.*;
import java.util.Random;
import static java.lang.Math.*;

public class Main {

    public static void main(String[] args) {
        Random rand=new Random();
        int x=rand.nextInt(-4+1-(-100))+(-100);
        System.out.println("If t>0 and t²"+x+"=0, what is the value of t?\n");
        double ans = sqrt(abs(x));
        System.out.println("Ans: "+ans);
    }
}
