package com.dawngerpony.algorithms.misc;

/**
 * FIFO queue implementation using a single linked list.
 * 
 * @author dawngerpony
 *
 * @param <Item>
 */
public class Queue<Item> {
	private Node first;
	private Node last;
	private int N;
	
	/**
	 * Singly linked list.
	 * 
	 * @author dawngerpony
	 *
	 */
	private class Node {
		Item item;
		Node next;
	}
	
	public boolean isEmpty() {
		return first == null;
	}
	
	public int size() {
		return N;
	}
	
	public void enqueue(Item item) {
		Node oldlast = last;
		last = new Node();
		last.item = item;
		last.next = null;
		if(isEmpty()) {
			first = last;
		} else {
			oldlast.next = last;			
		}
		N++;
	}
	
	public Item dequeue() {
		Item item = first.item;
		first = first.next;
		N--;
		if(isEmpty()) {
			last = null;
		}
		return item;
	}
	
	public static void main(String[] args) {
		Queue<String> q = new Queue<String>();
		String test = "BEAUTIFUL";
		for(int i = 0; i < test.length(); i++) {
			String item = "" + test.charAt(i);
			q.enqueue(item);
		}
		while(!q.isEmpty()) {
			System.out.println(q.dequeue());
		}
	}
}
