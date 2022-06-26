import java.util.*;

public class twoDimensional {
    public static void main(String[] args) {
        int[][] myArray = new int[3][3];
        // Scanner sc = new Scanner(System.in);

        // System.out.println("Enter here => ");
        for(int i=0; i<myArray.length;i++) {
            for(int j=0; j<myArray.length;j++) {
                //  myArray[i][j]= sc.nextInt();
            }
        }

        for(int i=0; i<myArray.length;i++) {
            for(int j=0; j<myArray.length;j++) {
                System.out.print(myArray[i][j]+" ");
            }
            System.out.println(); // มันคือ \n งมหาตั้งนาน โง่ชะมัดเลย 555555555555555555
        }
    }

}

