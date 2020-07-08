package com.dawngerpony.algorithms.misc;

import java.math.BigInteger;

public class Factorial {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		Factorial f = new Factorial();
		for(int i=1; i <= 10; i++) {
			System.out.println(i + " = " + f.factorial(i));			
		}
	}
	
	BigInteger factorial(int x) {
		if(x < 0) {
			throw new IllegalArgumentException();
		} else if(x == 0) {
			return BigInteger.ONE;
		} else {
			return BigInteger.valueOf(x).multiply(factorial(x-1));
		}
	}

}
