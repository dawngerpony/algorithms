package com.dawngerpony.algorithms.misc;

import org.junit.jupiter.api.Test;

import java.math.BigInteger;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class FactorialTest {

    @Test
    public void testFactorialSuccess() {

        Factorial f = new Factorial();

        assertEquals(f.factorial(0), BigInteger.valueOf(1));
        assertEquals(f.factorial(1), BigInteger.valueOf(1));
        assertEquals(f.factorial(2), BigInteger.valueOf(2 * 1));
        assertEquals(f.factorial(3), BigInteger.valueOf(3 * 2 * 1));
        assertEquals(f.factorial(4), BigInteger.valueOf(4 * 3 * 2 * 1));
        assertEquals(f.factorial(5), BigInteger.valueOf(5 * 4 * 3 * 2 * 1));
        assertEquals(f.factorial(10), BigInteger.valueOf(10 * 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1));
    }
}
