/* Tarun Tej Challa
 * L20469390
 * Homework 14
 */

public class queue {
	String [] data;
	int max;		// max number of entries this queue can hold
	int nEntries;	// number of current entries in this stack
	int front;
	int rear;
	
	// Constructor
	queue (int max) {
		data = new String [max];
		front = 0;			// when front == rear, the queue is empty
		rear = 0;
		nEntries = 0;
		this.max = max;
	}
	// Add operation
	void add (String s) {
		if (nEntries < max) {
			data[rear]=s;
		}
		rear=rear-1;
		if(rear==-1){
			rear=max-1;
		}
		nEntries=nEntries+1;
			
	}
	// Remove operation
	String remove () {
		String s = null;
		if (nEntries >= 1) {
				s=data[front];
			}
		front=front-1;
		if(front==-1){
			front=max-1;
			}
		nEntries=nEntries-1;		
		return s;
	}
	// Peek operation
	String peek () {
		// ADD CODE HERE
		
	return null;
		
	}
	// Clear the queue
	void clear () {

		// Set front and rear == 0 (denoting the queue is empty)
		// nEntries = 0;
		front=0;
		rear=0;
		nEntries=0;
	}
		
	
	// Return the current number of entries in this queue
	int count () {
		return nEntries;
	}	
}
