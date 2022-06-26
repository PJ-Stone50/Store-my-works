import javax.swing.JOptionPane;
import javax.swing.JFrame;

public class MyGame3 {
    private static int generateSecretNumber() {
        double X = Math.random();
        int maximum = 50;
        int secretNumber = (int)Math.floor(X*maximum);
        return secretNumber;
    }
    public static void main (String[] args) {
        String ipScore;
        Integer sc,i=1;
        Integer secretNumber = generateSecretNumber();
        
        // create a jframe
        JFrame frame = new JFrame("JOptionPane showMessageDialog example");
    
        for (int cnt = 1; cnt <= 10; cnt++) {
            i++;
            ipScore = JOptionPane.showInputDialog(null, "Radius input");
            sc = Integer.parseInt(ipScore);
            
            if (sc == secretNumber)
                JOptionPane.showMessageDialog(frame,"Secret number is "+secretNumber+"\nYou Win!\nYou guessed it in "+cnt+" times");
            else   // Incorrect many times
                if (cnt == 10)
                     JOptionPane.showMessageDialog(frame,"Youlose");
                     
                else 
                    JOptionPane.showMessageDialog(frame,"Secret number is "+secretNumber+"\nYou Win!\nYou guessed it in "+cnt+" times");   
        }
        //JOptionPane.showMessageDialog(frame,"Secret number is "+secretNumber+"\nYou guessed it in "+cnt+" times");
    }  
}
    
    
    
    
    
    


// ยังไม่สั่ง print count
//