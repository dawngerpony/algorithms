// Bag.java
import java.util.Iterator;

public class Bag<Item> implements Iterable<Item> {

	private Item items = null;
	private int index = 0;

	// Constructor
	public Bag() {
		this.items = new Item[10];
		//@TODO Complete this method.
	}

	public void add(Item item) {

	}

	public boolean isEmpty() {
		return false;
	}

	public int size() {
		return 0;
	}

	public Iterator iterator() {
		return new BagIterator();
	}

	private class BagIterator implements Iterator {
		public boolean hasNext() {
			return false;
		}

		public Item next() {

		}

		public void remove() {

		} 
	}

	public static void main(String[] args) {
		System.out.println("Hello!");
	}
}

