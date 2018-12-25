

/*
 	Vijay Reddy Thippana
 	Homework 8
 */
public class Snake extends Reptile {

	String name;
	String dangerLevel;
	
	public Snake(String name, String dangerLevel) {
		this.name = name;
		this.dangerLevel = dangerLevel;
	}

	public Snake(String color) {
		super(color);
		this.name=" ";
		this.dangerLevel = "poisonous";
		
	}

	 Snake() {
		super();
		this.name=" ";
		this.dangerLevel = "poisonous";
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getDangerLevel() {
		return dangerLevel;
	}

	public void setDangerLevel(String dangerLevel) {
		this.dangerLevel = dangerLevel;
	}

	@Override
	public String toString() {
		return "Snake color=" + this.color + "";
	}
	
	

}
