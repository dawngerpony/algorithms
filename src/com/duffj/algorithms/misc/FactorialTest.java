package com.duffj.algorithms.misc;

import java.math.BigInteger;

import org.testng.Assert;
import org.testng.annotations.Test;

public class FactorialTest {

	@Test
	public void testFactorialSuccess() {
		Factorial f = new Factorial();

//		Assert.assertEquals(f.factorial(-1), null);
		Assert.assertEquals(f.factorial(0), BigInteger.valueOf(1));
		Assert.assertEquals(f.factorial(1), BigInteger.valueOf(1));
		Assert.assertEquals(f.factorial(2), BigInteger.valueOf(2*1));
		Assert.assertEquals(f.factorial(3), BigInteger.valueOf(3*2*1));
		Assert.assertEquals(f.factorial(4), BigInteger.valueOf(4*3*2*1));
		Assert.assertEquals(f.factorial(5), BigInteger.valueOf(5*4*3*2*1));
		Assert.assertEquals(f.factorial(10), BigInteger.valueOf(10*9*8*7*6*5*4*3*2*1));
	}
}
