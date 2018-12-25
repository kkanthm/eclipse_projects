

/*
 	Vijay Reddy Thippana
 	Homework 8
 */

public class Reptile {

	String color;
	int weight;
	int length;
	Reptile() {
		color = "";
		weight = 10;
		length = 10;
	}
	Reptile(String color){
		this.color = color;
		weight = 10;
		length = 10;
	}
	public String getColor() {
		return color;
	}
	public void setColor(String color) {
		this.color = color;
	}
	public int getWeight() {
		return weight;
	}
	public void setWeight(int weight) {
		this.weight = weight;
	}
	public int getLength() {
		return length;
	}
	public void setLength(int length) {
		this.length = length;
	}
	
	
}
