package queue;

import java.util.HashSet;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Queue {
    public static void main(String[] args) {
        System.out.println(-1 % 8);
        int[] arr = new int[]{1, 2, 3};
        IntStream.of(arr).boxed().collect(Collectors.toCollection(HashSet::new));
        HashSet<Integer> set = new HashSet<Integer>();
    }
}
