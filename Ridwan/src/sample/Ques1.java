package sample;
import java.lang.*;
import java.util.Random;

public class Ques1 {
    // create instance of Random class
    static Random rand = new Random();
    static int c, e, f, d;
    static String result;
	static String ques;

    // Generate random integers in range -5 to 5
    Ques1() {
    	
    	this.setQues();
    	
    }

    public static String getResult() {
    	
    if(c+e == 0 && d+f ==0) {
    	result = "0";
    }
    if(d+f==0) {
    	result = Integer.toString(d+f);
    }
        // Returns the sum.
        result = (c+e) + "+" +
                (d+f) + "i";
        return result;
    }

    public void setResult(String result) {
        this.result = result;
    }

    public static String getQues() {
    	setQues();
        return ques;
    }

    public static void setQues() {
    	
         c = rand.nextInt(5 + 1 - (-5)) + (-5);

         do {
             e = rand.nextInt(5 + 1 - (-5)) + (-5);
         }
         while (c == -e);

         do {
             f = rand.nextInt(5 + 1 - (-5)) + (-5);
         }
         while (f == 0);

         do {
             d = rand.nextInt(5 + 1 - (-5)) + (-5);
         }
         while (d == -f);

         ques="1) For i=√-1, what is the sum "+"("+c+"+"+d+"i"+")"+"+"+"("+e+"+"+f+"i"+") ?";

        
    }
}

