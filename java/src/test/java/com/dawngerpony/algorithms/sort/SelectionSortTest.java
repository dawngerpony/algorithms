package com.dawngerpony.algorithms.sort;

import org.apache.commons.lang3.ArrayUtils;
import org.junit.jupiter.api.Test;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class SelectionSortTest {
    @Test
    public void testAdd() {
        assertEquals(42, Integer.sum(19, 23));
    }

    @Test
    public void testSortSuccess() {
        String unsorted = "cba";
        String expected = "abc";
        Character[] c = ArrayUtils.toObject(unsorted.toCharArray());

        SelectionSort sorter = new SelectionSort();
        Character[] sorted = (Character[]) sorter.sort(c);

        String actual = new String(ArrayUtils.toPrimitive(sorted));
        assertEquals(expected, actual);
    }
}
