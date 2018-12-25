package com.company;
import java.io.*;
import java.util.Random;
import static java.lang.Math.*;
class Main
{

    // Prints roots of quadratic
    //equation ax * 2 + bx + x
    void findRoots(int a, int b, int c, int f, int g)
    {
        // If a is 0, then equation is not
        //quadratic, but linear

        int d  = b*b - 4*a*c;
        double sqrt_val = sqrt(abs(d));




            int fb=(int)(-b + sqrt_val) / (2 * a);
            int sb=(int)(-b - sqrt_val) / (2 * a);

            int fa=8-fb;
            int sa=8-sb;

            int fc=(g*fa)+(f*fb);
            int sc=(g*sa)+(f*sb);

            System.out.println("Values of c is: "+fc+" and "+sc);


    }

    // Driver code
    public static void main(String args[])
    {
        int d,f,e,g,h,i;
        Random rand=new Random();
        do{
            h=rand.nextInt(15+1-9)+9;
        }while(h%2!=0 && h%3!=0 && h%5!=0 && h%7!=0);
        f=rand.nextInt(10+1-1)+1;
        g=rand.nextInt(10+1-1)+1;
        i=f*g;
        System.out.println("if (ax+"+f+")(bx+"+g+")="+h+"x²+cx+"+i+" for all values of x, and a+b=8,\n");
        System.out.println("what are two possible values for c?\n");
        //j=a and k=b
        //quadratic equation after solution becomes k^2-8k+h

        Main obj = new Main();
        int l=1;
        int m=-8;
        obj.findRoots(l, m, h, f, g);
    }
}

