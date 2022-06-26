import java.util.Scanner;
 
public class ReverseDigit { 
 
   public static void main(String[] args) { //main method
       Scanner input = new Scanner(System.in);
       System.out.print("Enter the number to be reversed : "); //prompt user to enter number
       int entry = input.nextInt();
       int result = reverse(entry);
       System.out.printf("The reverse of" + entry + "is"+ result); //output original digit and digit reversed
   }
 
   public static int reverse(int n) { //method to reverse digit
       int result = 0;
       int rev;
       while (n > 0) {
           rev = n % 10;
           n = n / 10;
           result = result * 10 + rev;
       }
       return result; //return result to main method
   } //end main method
} //end class ReverseDigit