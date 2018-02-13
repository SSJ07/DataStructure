/**
 * 
 * Arrays are fixed in size.
 * Arrays can hold homogeneous data only. (collection can hold any type of data)
 * Arrays is worst case in insertion and deletion frequently.
 * Arrays are best data structure in retrieval application.
 * 
 */
public class ArrayExample {

	public static void main(String[] args) {

		int[] x = new int[]{1,2,3,4,6};
		int[] x1 = new int[10];
		int[] x2 = {1,2,3,5,6};
		
//		int[10]x; //invalid
		int[] x3;
		
		
//	     int[] a = new int[]; // compiler will give error . It's require size when array creation.
	     int[] b = new int[0]; //It's legal array with size zero.
	     int[] c = new int[-3]; // compiler time is fine.  Runtime exception will occure. NegativeArraySizeException

	     int[] d = new int['a']; // valid
	     byte e = 10;
	     int [] f = new int[e]; // valid
	     short g = 20;
	     int[] h = new int[g]; //valid

		
	}

}
