/*
 * ================================== Vijay Reddy Thippana L20469889 ============================
 * ================================== COSC Program #2 ===========================================
 * ================================== Tiling Problem ============================================
 * ================================== Divide and Conquer Algorithm ==============================
 * ================================== The program is producing the expected correct output ======
 * 
 */
import java.util.Comparator;
public class Tromino {

	public Point position;
	public int q;
	
	
	public static Comparator<Tromino> trominoComparator = new Comparator<Tromino>() {
		public int compare(Tromino T1, Tromino T2) {
			int firstPointx = T1.position.x;
			int secondPointx = T2.position.x;
			int firstPointy = T1.position.y;
			int secondPointy = T2.position.y;
			int xComparator = firstPointx - secondPointx;
			if (xComparator!=0) {
				return xComparator;
			}
			return firstPointy-secondPointy;
		}
	};
	public Tromino(Point position, int q) {
		super();
		this.position = position;
		this.q = q;
	}

	public Point getPosition() {
		return position;
	}

	public void setPosition(Point position) {
		this.position = position;
	}

	public int getQ() {
		return q;
	}

	public void setQ(int q) {
		this.q = q;
	}

	@Override
	public String toString() {
		return "((" + position.x + "," +position.y+"),"+ q + ")";
	}
	
}
