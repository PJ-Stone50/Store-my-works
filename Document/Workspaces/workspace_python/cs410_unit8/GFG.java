import java.util.*;
 
// main class
class GFG {
 
    // Main driver method
    public static void main(String args[])
    {
        // Creating an Arraylist object of string type
        Object[] objects = new Object[3];

        objects[0] = "foo";
        objects[1] = 5;
        Object[] object2 = {"str1",1,"str2"};
        
        System.out.println("Updated ArrayList " + objects[1]);
        System.out.println("Updated ArrayList " + object2[0] + object2[1]+ object2[2]);

    }
}