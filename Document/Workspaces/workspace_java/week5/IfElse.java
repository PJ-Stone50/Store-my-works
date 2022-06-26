
import javax.swing.*;

public class IfElse {
    public static void main(String[] args) {
        int testScore;
        
        // ส่วนนี้เจ้าจงจำไว้ ไว้ ไว้ ไว้ ไว้
        testScore = Integer.parseInt(JOptionPane.showInputDialog(null, "Enter here :"));
        System.out.println(testScore);

        if( testScore < 70 ) {
            JOptionPane.showMessageDialog(null, "You didn't pass");
            JOptionPane.showMessageDialog(null, "Try harder next time");
        }
        else {
            JOptionPane.showMessageDialog(null, "You did pass");
            JOptionPane.showMessageDialog(null, "Keep up the good work");

        }
    }

}

