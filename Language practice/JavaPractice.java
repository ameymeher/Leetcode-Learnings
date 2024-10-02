import java.util.Arrays;
import java.util.HashSet;
public class JavaPractice {

    public static void main(String[] args){

        //String manipulations
        String str = "Hello";
        System.out.println(str.length());
        System.out.println(str.charAt(0));
        System.out.println(str.substring(0, 2));
        System.out.println(str.indexOf("l"));
        System.out.println(str.equals("Hello"));
        System.out.println(str.compareTo("ZYC"));

        //Put all elements of string in a HashSet
        HashSet<Character> set2 = new HashSet<Character>();
        for(char c : str.toCharArray()){
            set2.add(c);
        }

        

        //Creating a HashSet
        HashSet<Integer> set = new HashSet<Integer>();
        set.add(1);
        set.add(2);
        set.remove(1);
        System.out.println(set.contains(1));
        System.out.println(set.size());

        //Get the max elemnt in a HashSet
        int max = Integer.MIN_VALUE;
        for(int i : set){
            max = Math.max(max, i);
        }

        //Working with HashMap
        HashMap<Integer, Integer> map = new HashMap<Integer, Integer>();
        map.put(1, 2);
        map.put(2, 3);
        map.remove(1);
        System.out.println(map.containsKey(1));
        System.out.println(map.get(2));
        System.out.println(map.size());
        
        //Get all the keys
        for(int key : map.keySet()){
            System.out.println(key);
        }

        //Get all the values
        for(int value : map.values()){
            System.out.println(value);
        }

        //Increment a key
        map.put(1, map.getOrDefault(1, 0) + 1);

        //Sort a HashMap by keys
        TreeMap<Integer, Integer> sortedMap = new TreeMap<Integer, Integer>(map);

        

        //Sort an array
        int[] arr = {1, 2, 3, 4, 5};
        Arrays.sort(arr);
        
        //Binary search
        int index = Arrays.binarySearch(arr, 3);

        //Create a 2D array
        int[][] arr2D = new int[2][3];
        arr2D[0][0] = 1;
        arr2D[0][1] = 2;
        arr2D[0][2] = 3;
        arr2D[1][0] = 4;
        arr2D[1][1] = 5;
        arr2D[1][2] = 6;

        //Iterate through a 2D array
        for(int i = 0; i < arr2D.length; i++){
            for(int j = 0; j < arr2D[0].length; j++){
                System.out.println(arr2D[i][j]);
            }
        }

        //Create a heap
        int[] heap = new int[10];
        int size = 0;
        heap[size++] = 1;
        heap[size++] = 2;
        heap[size++] = 3;
        int parent = (size - 1) / 2;
        int leftChild = 2 * parent + 1;
        int rightChild = 2 * parent + 2;

        //Isnt there a package for heap in Java?

        //Printing an array


    }
}