package main.java.com.dawngerpony.katas;

import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.HashSet;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Set;
import java.util.stream.Collectors;

public class EnoughIsEnough {

    public static int[] deleteNth(int[] elements, int maxOccurrences) {
        List<Integer> list = Arrays.stream(elements).boxed().collect(Collectors.toList());
        List<Integer> output = new ArrayList<>();
        Map<Integer, Integer> counts = new HashMap<>();
        Set<Integer> set = new HashSet<>();
        set.addAll(list);
        for(int i : set) {
            counts.put(i, 0);
        }
        for(int i : elements) {
            int occurrences = counts.get(i);
            if(occurrences < maxOccurrences) {
                output.add(i);
                counts.put(i, occurrences + 1);
            }
        }
        return output.stream().mapToInt(Integer::intValue).toArray();
    }
}
