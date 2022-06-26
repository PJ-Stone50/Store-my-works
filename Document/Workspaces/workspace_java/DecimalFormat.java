import java.text.DecimalFormat;

public class DecimalFormat {
	public static void main(String[] args) {
 		float oneNum = 3.14159F;
 		double nextNum = 3827967.29836598263987649826395809384756;

 		DecimalFormat commaFormat;
			commaFormat = new DecimalFormat("#,###.##");
 		String myPi = commaFormat.format(oneNum);

 		System.out.println("oneNum = " + commaFormat.format(oneNum));
 		System.out.println("nextNum = " + commaFormat.format(nextNum));
	 }
 }