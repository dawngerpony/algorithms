// Bag.java
import java.util.Iterator;
import java.util.List;
import java.util.ArrayList;

public class Bag<Item> implements Iterable<Item> {

	private List<Item> items = null;
	private int size = 0;

	// Constructor
	public Bag() {
		this.items = new ArrayList<Item>();
	}

	public void add(Item item) {
		this.items.add(item);
		this.size++;
	}

	public boolean isEmpty() {
		return false;
	}

	public int size() {
		return this.size;
	}

	public Iterator iterator() {
		return new BagIterator();
	}

	private class BagIterator implements Iterator {

		private int i = 0;

		public boolean hasNext() {
			if(i >= size) {
				return false;
			} else {
				return true;
			}
		}

		public Item next() {
			Item next = items.get(i);
			if(next != null) {
				i++;
				return next;
			} else {
				return null;
			}
		}

		public void remove() {
			// this.items.remove(this.index);
		} 
	}

	public static void main(String[] args) {
		Bag<Banana> bag = new Bag<Banana>();
		Banana first = new Banana("foo");
		Banana second = new Banana("bar");
		bag.add(first);
		bag.add(second);

		for(Banana i : bag) {
			System.out.println(i.value);
		}
	}
}

