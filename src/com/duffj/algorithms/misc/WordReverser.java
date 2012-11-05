package com.duffj.algorithms.misc;

public class WordReverser {

	/**
	 * reverse the letters in a string.
	 * 
	 * @param input
	 * @return
	 */
	public String reverseString(String input) {
		char[] letters = input.toCharArray();
		for(int i = 0; i < letters.length / 2; i++) {
			letters = this.swap(letters, i, letters.length - i - 1);
		}
		return new String(letters);
	}
	
	private char[] swap(char[] input, int x, int y) {
		char temp = input[x];
		input[x] = input[y];
		input[y] = temp;
		return input;
	}
	
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		WordReverser reverser = new WordReverser();
		String test1 = "hannah";
		String test2 = "abcdef";
		String test1Reversed = reverser.reverseString(test1);
		System.out.println(test1Reversed);
		String test2Reversed = reverser.reverseString(test2); 
		System.out.println(test2Reversed);
	}

}
