package com.dawngerpony.algorithms.sort;

/**
 * Selection sort implementation on an array of Items.
 * 
 * @author dawngerpony
 *
 * @param <Item>
 * @param <T>
 */
public class SelectionSort extends Sort {

	public Comparable[] sort(Comparable[] items) {
		
		for(int i = 0; i < items.length; i++) {
			int min = i;
			for(int j = i+1; j < items.length; j++) {
				if(less(items[j], items[min])) {
					min = j;
				}
			}
			swap(items, i, min);
			print(items);
		}
		return items;
	}
	
	public static void main(String[] args) {
//		String s = "0987654321";
//		String s = "FEDCBA";
		String s = "vngjoispdgpiwenlkanbasuocabievbkjacnioc";
		char[] charArray = s.toCharArray();
		Character[] c = new Character[charArray.length];
		for(int i = 0; i < charArray.length; i++) {
			c[i] = new Character(charArray[i]);
		}
		
		SelectionSort sorter = new SelectionSort();
		Character[] sorted = (Character[]) sorter.sort(c);
		String sortedString = "";
		for(Character x : sorted) {
			sortedString += x;
		}
		System.out.println(sortedString);
	}
}
