
/*
 	Vijay Reddy Thippana
 	Homework 8
 */
public class Lizard extends Reptile {

	String name;
	String status;

	Lizard(String color) {
		super(color);
		this.name = " ";
		this.status = "meat-eater";
	}
	 
	 public String getName() {
			return name;
		}

		public void setName(String name) {
			this.name = name;
		}

		public String getStatus() {
			return status;
		}

		public void setStatus(String status) {
			this.status = status;
		}

		@Override
		public String toString() {
			return "Lizard color=" + this.color + "";
		}
		
		
	 

}
