package com.duffj.algorithms.sort;

public abstract class Sort {

	protected void swap(Comparable[] items, int x, int y) {
		Comparable temp = items[x];
		items[x] = items[y];
		items[y] = temp;
	}

	protected boolean less(Comparable x, Comparable y) {
		int cmp = x.compareTo(y);
		if(cmp < 0) {
			return true;
		} else {
			return false;
		}
		
	}
	
	protected void print(Comparable[] items) {
		for(Comparable c : items) {
			System.out.print(c);				
		}
		System.out.print("\n");
	}
//	public Comparable[] sort(Comparable[]);
	
}
