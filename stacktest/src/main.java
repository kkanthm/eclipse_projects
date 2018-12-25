/* Tarun Tej Challa
 * L20469390
 * Homework 14
 */

public class main {
	public static void main(String[] args) {
		
		// Create an empty stack of up to 10 Strings
		stack names = new stack(10);
		
		// Add 3 names to the stack
		names.push ("Elvis");
		names.push ("Johnny");
		names.push ("Ringo");
		
		// Pop off the names and print them (should print in reverse order they were pushed)
		while (names.count() >= 1)
			System.out.println (names.pop());
		
		System.out.println("");
		
		// Create an empty queue of up to 10 Strings
		queue cars = new queue(10);
				
		// Add 3 cars to the queue
		cars.add ("1");
		cars.add ("2");
		cars.add ("3");
		cars.add("4");
		cars.add("5");
				
		// Remove the car names and print them
		while (cars.count() >= 1)
			System.out.println (cars.remove());
		
			

	}

}
