package com.duffj.algorithms.misc;

/**
 * Implementation of a stack using arrays.
 * 
 * @author dafydd
 *
 * @param <Item>
 */
public class Stack<Item> {
	
	private Item[] items;
	private int size = 0;
	
	public Stack(int capacity) {
		this.items = (Item[]) new Object[capacity];
	}
	
	private void resize(int newSize) {
		Item[] newItems = (Item[]) new Object[newSize];
		for(int i = 0; i < this.items.length; i++) {
			newItems[i] = items[i];
		}
		this.items = newItems;
	}
	
	/**
	 * Push a new item onto the stack.
	 * 
	 * @param item
	 */
	public void push(Item item) {
		if(this.items.length == this.size) {
			this.resize(this.size*2);
		}
		this.items[size++] = item;
	}

	/**
	 * Pop an item off the stack.
	 * Do we want to throw the ArrayOutOfBoundsException here?
	 * 
	 * @return
	 */
	public Item pop() {
		return this.items[--size];			
	}
	
	public boolean isEmpty() {
		if(this.size == 0) {
			return true;
		} else {
			return false;
		}
	}

	public static void main(String[] args) {
		Stack<String> stack = new Stack<String>(2);
		String first = "red";
		String second = "orange";
		String third = "yellow";
		String fourth = "green";
		String fifth = "blue";
		String sixth = "indigo";
		String seventh = "violet";
		stack.push(first);
		stack.push(second);
		stack.push(third);
		stack.push(fourth);
		stack.push(fifth);
		stack.push(sixth);
		stack.push(seventh);

		while(!stack.isEmpty()) {
			System.out.println(stack.pop());
		}
	}
	
}