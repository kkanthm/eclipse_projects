/* Tarun Tej Challa
 * L20469390
 * Homework 14
 */
public class stack {
	String [] data;
	int max;		// max number of entries this stack can hold
	int nEntries;	// number of current entries in this stack
	int top;		// index of top of stack (starts at 0)
	
	// Constructor
	stack (int max) {
		data = new String [max];
		top = 0;
		nEntries = 0;
		this.max = max;
	}
	// Push operation
	void push (String s) {
		if (nEntries < max) {
			data[top] = s;
			top++;
			nEntries++;
		}	
	}
	// Pop operation
	String pop () {
		String s = null;
		if (nEntries >= 1) {
			top--;
			s = data[top];
			nEntries--;
		}
		return s;
	}
	// Peek operation
	String peek () {
		String s = null;
		if (nEntries >= 1)
			s = data[top-1];
		return s;
	}
	// Clear the stack
	void clear () {
		for (int i=0; i<max; i++)
			data[i] = null;
		nEntries = 0;
		top = 0;
	}
	// Return the current number of entries in this stack
	int count () {
		return nEntries;
	}	
}
