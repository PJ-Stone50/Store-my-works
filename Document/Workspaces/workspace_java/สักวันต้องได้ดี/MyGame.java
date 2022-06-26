import javax.swing.JOptionPane;
import javax.swing.JFrame;

public class MyGame {
private static int generateSecretNumber() {
    double X = Math.random();
    int maximum = 100;
    int secretNumber = (int)Math.floor(X*maximum);
    return secretNumber;
}
public static void main (String[] args) {
    String ipScore;
    Integer sc;
    Integer secretNumber = generateSecretNumber();
    int cnt = 0;
    
    ipScore = JOptionPane.showInputDialog(null, "Radius input");
    sc = Integer.parseInt(ipScore);
    cnt++;
    // create a jframe
    JFrame frame = new JFrame("JOptionPane showMessageDialog example");
    
    for (int i = 0; i <= 10; i++) {
        do{
        if (cnt == 10) {
            if (sc != secretNumber)
                if (sc > secretNumber){
                    
                    JOptionPane.showMessageDialog(null,"Too High\n"+"You did guess "+cnt+" times");
                } 
                else{
                    JOptionPane.showMessageDialog(null,"Too Low\n"+"You did guess "+cnt+" times");
                }
            else if (cnt == 1){  // Incorrect in one time
                JOptionPane.showMessageDialog(frame,"Secret number is "+secretNumber+"\nYou Win!\nYou've just won by one guess.");
                break; // ไม่ควรใส่ break แล้วต้องทำยังไง? สั่ง reset function ยังไง, เรื่อง Link มันเอามาใช้กับงานนี้ได้มั้ย ใช้แล้วดียังไง โอ๊ะโอ่ 
            }else{  // Incorrect many times
                 JOptionPane.showMessageDialog(frame,"Secret number is "+secretNumber+"\nYou Win!\nYou guessed it in "+cnt+" times");
                 break;
            }
        }
    }while (sc > 0 && sc <= 100);    
    }
    
    
    
    
    
    
     
    //   rd = radius  
}
}

// ยังไม่สั่ง print count
//