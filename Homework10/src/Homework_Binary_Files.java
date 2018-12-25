import java.io.*;
import java.math.BigInteger;


/* 	Vijay Reddy Thippana L20469889
 COSC 4304 - Foundations Of Programming
 Homework 10											*/
public class Homework_Binary_Files {
    public static void main(String [] args) {

        // The name of the file to open.
        String fileName = "Forest.BMP";

        try {
            // Use this for reading the data.
            byte[] BMPFileHeader = new byte[14];
            byte[] buffer2 = new byte[2];
            byte[] buffer4 = new byte[4];

            FileInputStream inputStream = 
                new FileInputStream(fileName);

            // read fills buffer with data and returns
            // the number of bytes read (which of course
            // may be less than the buffer size, but
            // it will never be more).
            int total = 0;
            int nRead = 0;
            int b = 0; // is an index into the 14-byte BMPFileHeader
            nRead = inputStream.read(BMPFileHeader);
            if (nRead == 14) {
            	for (int i=0; i<2; i++)
            		buffer2[i] = BMPFileHeader[b++];
            	System.out.println (new String(buffer2));	
            	
            	for (int i=3; i>=0; i--)
            		buffer4[i] = BMPFileHeader[b++];
            	System.out.println ("File size = " + new BigInteger(buffer4).intValue());	
            	total += nRead;
            }
           
            // Example: print the 4 bytes containing the offset image data
            //buffer4[3] = BMPFileHeader[10];
            //buffer4[2] = BMPFileHeader[11];
            //buffer4[1] = BMPFileHeader[12];
            //buffer4[0] = BMPFileHeader[13];
            
            // This for loop does what the above 4 lines of code does
            for (int i=3, k=10; i>=0; i--,k++)
            	buffer4[i] = BMPFileHeader[k];
            
            System.out.println ("Image offset = " + new BigInteger(buffer4).intValue());	
            
        
            // TODO: Read in the next 40 bytes from the file
            //  create a 40-byte buffer called BMPHeader
            //  read into the buffer from the file
            byte[] BMPHeader = new byte[40];
            
            nRead = inputStream.read(BMPHeader);
            
            if(nRead==40) {
            	
            	// TODO: Copy the 4 bytes representing the image width from the BMPHeader into buffer4
                // TODO: Print out (as an integer) the width "Image width = xxxxx"
                
            	for (int i=3, k=4; i>=0; i--,k++) {
            		buffer4[i] = BMPHeader[k];
            	}
            	 System.out.println ("Image width = " + new BigInteger(buffer4).intValue());	
            	 
            	 
            	// TODO: Copy the 4 bytes representing the image height from the BMPHeader into buffer4
                 // TODO: Print out (as an integer) the width "Image height = xxxxx"
            	 for (int i=3, k=8; i>=0; i--,k++) {
             		buffer4[i] = BMPHeader[k];
             	}
             	 System.out.println ("Image height = " + new BigInteger(buffer4).intValue());
             	 
             	  // TODO: Copy the 2 bytes representing the bits-per-pixel from the BMPHeader into buffer2
                 // TODO: Print out (as an integer) the bits-per-pixel "Bits-per-pixel = xxxx"
             	for (int i=1, k=14; i>=0; i--,k++) {
            		buffer2[i] = BMPHeader[k];
            	}
            	 System.out.println ("Bits-per-pixel = " + new BigInteger(buffer2).intValue());
            	 
            	 total+=nRead;
            }
            
            
            
          
            
            
            
            // Always close files.
            inputStream.close();        

            System.out.println("Read " + total + " bytes");
        }
        catch(FileNotFoundException ex) {
            System.out.println(
                "Unable to open file '" + 
                fileName + "'");                
        }
        catch(IOException ex) {
            System.out.println(
                "Error reading file '" 
                + fileName + "'");                  
            // Or we could just do this: 
            // ex.printStackTrace();
        }
    }
}
