import javax.swing.JOptionPane;
import javax.swing.JFrame;

public class MyGame2 {
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
        
        // create a jframe
        //JFrame frame = new JFrame("JOptionPane showMessageDialog example");
        // sadsad
        for (int cnt = 1; cnt <= 10; cnt++) {
            ipScore = JOptionPane.showInputDialog(null, "Radius input");
            sc = Integer.parseInt(ipScore);
            
            if (sc != secretNumber){
                if(cnt < 10){
                    if (sc > secretNumber)
                        JOptionPane.showMessageDialog(null,"Too High\n"+"You did guess "+cnt+" times");
                    else
                        JOptionPane.showMessageDialog(null,"Too Low\n"+"You did guess "+cnt+" times");
                }
                else{ //After 10 times
                    JOptionPane.showMessageDialog(null,"Secret number is "+secretNumber+"\n you guessed it in "+cnt+" times");
                    JOptionPane.showMessageDialog(null,"You lose!");
                }
                
            }else { //Before 10 times
                JOptionPane.showMessageDialog(null,"Secret number is \n"+secretNumber+" You Win!\n"+"you guessed it in "+cnt+" times");
                break;
            }
        }
    }  
}
    
    
    
    
    
    


// ยังไม่สั่ง print count
//