/*
 * ================================== Vijay Reddy Thippana L20469889 ============================
 * ================================== COSC Program #2 ===========================================
 * ================================== Tiling Problem ============================================
 * ================================== Divide and Conquer Algorithm ==============================
 * ================================== The program is producing the expected correct output ======
 * 
 */
import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

public class Tiling_Trominoes {

	
	public static void tiling_trominoes(int n, Point location, Point missing, ArrayList<Tromino> trominoesList) {
		
		if(n==2) {
			if(missing.x==location.x) {
				if (missing.y==location.y) {
	                trominoesList.add(new Tromino(location,0));
				}
	            if (missing.y==location.y+1) {
	                trominoesList.add(new Tromino(location,1));
	            }
			}
			else if(missing.y==location.y) {
				if (missing.x==location.x+1) {
	                trominoesList.add(new Tromino(location,3));
				}
			}
			if ((missing.x==location.x+1) && (missing.y==location.y+1)) {
	            trominoesList.add(new Tromino(location,2));
			}
			
			return;
		}
		
		
		 Point m1=null;
		 Point m2=null;
		 Point m3=null;
		 Point m4=null;
		 
		 Point center =new Point(location.x+n/2, location.y+n/2);
		    
		 Point l1 = location;
		 Point l2 = new Point(location.x,center.y);
		 Point l3 = center;
		 Point l4 = new Point(center.x,location.y);
		    
		    if (missing.x<center.x) { 
		        if (missing.y<center.y) { 
		            trominoesList.add(new Tromino(new Point(center.x-1,center.y-1),0));
		            
		            m1 = missing;
		            m2 = new Point(center.x-1,center.y);
		            m3 = center;
		            m4 = new Point(center.x,center.y-1);
		        }
		        else {
		            trominoesList.add(new Tromino(new Point(center.x-1,center.y-1),1));
		            
		            m1 = new Point(center.x-1,center.y-1);
		            m2 = missing;
		            m3 = center;
		            m4 = new Point(center.x,center.y-1);
		           
		            
		        }
		    }
		    else if (missing.x>=center.x) {
		        if (missing.y>=center.y) {
		            trominoesList.add(new Tromino(new Point(center.x-1,center.y-1),2));
		            
		            m1 = new Point(center.x-1,center.y-1);
		            m2 = new Point(center.x-1,center.y);
		            m3 = missing;
		            m4 = new Point(center.x,center.y-1);
		            
		            
		        }
		        else {
		            trominoesList.add(new Tromino(new Point(center.x-1,center.y-1),3));
		            
		            m1 = new Point(center.x-1,center.y-1);
		            m2 = new Point(center.x-1,center.y);
		            m3 = center;
		            m4 = missing;
		            
		            
		        }
		    }    
		    tiling_trominoes(n/2, l1, m1, trominoesList);
		    tiling_trominoes(n/2, l2, m2, trominoesList);
		    tiling_trominoes(n/2, l3, m3, trominoesList);
		    tiling_trominoes(n/2, l4, m4, trominoesList);
	}
	public static void main(String[] args) {
		
		ArrayList<List<Object>> inputcases = new ArrayList<List<Object>>();
		List<Object> input1 = new ArrayList<Object>();
		input1.add(4);
		input1.add(new Point(3,3));
		List<Object> input2 = new ArrayList<Object>();
		input2.add(8);
		input2.add(new Point(4,5));
		List<Object> input3 = new ArrayList<Object>();
		input3.add(8);
		input3.add(new Point(4,4));
		List<Object> input4 = new ArrayList<Object>();
		input4.add(16);
		input4.add(new Point(0,0));
		inputcases.add(input1);
		inputcases.add(input2);
		inputcases.add(input3);
		inputcases.add(input4);
		
		int inputCount=1;
		for (List<Object> each : inputcases) {
			
			ArrayList<Tromino> trominoesList=new ArrayList<Tromino>();
			int n=(int)each.get(0);
			Point Origin = new Point(0,0);
			Point missingSquare = (Point)each.get(1);
			System.out.println("\n\nINPUT COUNT :: "+inputCount);
			System.out.println("\tBOARD SIZE: "+n);
			System.out.println("\tLOCATION AT: "+Origin.x+" AND "+Origin.y);
			System.out.println("\tMISSING SQUARE AT: "+missingSquare.x+" AND "+missingSquare.y);
			System.out.println("\tTOTAL OF TROMINOES COMPUTED::: "+((n*n)-1)/3);
			System.out.println();
			System.out.println("ALL TROMINOES FOLLOW :::\n");
			
			tiling_trominoes(n,Origin,missingSquare,trominoesList);
			// Sort the Function
			Collections.sort(trominoesList,Tromino.trominoComparator);
			int index=1;
			for(Tromino eachTromino: trominoesList) {
				System.out.printf("\t %2d: ((%2d, %2d), %2d)",index,eachTromino.position.x,eachTromino.position.y,eachTromino.q);
				System.out.println();
				index=index+1;
			}
			
			inputCount=inputCount+1;
			
		}
		
	}

}
