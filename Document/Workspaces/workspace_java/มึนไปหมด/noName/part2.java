import java.util.*;

import javax.lang.model.util.ElementScanner14;

import jdk.tools.jlink.internal.SymLinkResourcePoolEntry;

public class part2 {

/*    private static int generateSecretNumber() {
        double X = Math.random();
        int maximum = 100;
        int secretNumber = (int)Math.floor(X*maximum);
        return secretNumber;
    }
*/ 
     
    public static void main (String[] args) {
        Random generator = new Random(50);
        int[][] hoursWorked = new int[12][];

        for(int i = 0; i < 12 ; i++) {
            if (i == 1)
                hoursWorked[i] = new int[28];
            else if ( i == 3 || i == 5 || i == 8 || i == 10)
                hoursWorked[i] = new int[30];
            else
                hoursWorked[i] = new int[31];
        }  
        
        for(int i = 0; i < 12 ; i++) {
            for(int j = 0; j<hoursWorked[i].length; j++) {
                hoursWorked[i][j] = (int)(10*generator.nextFloat());
            }
        
        }

    }
}
