import javax.swing.JOptionPane;


private static int generateSecretNumber() {
    double X = Math.random();
    int maximum = 100;
    int secretNumber = (int)Math.floor(X*maximum);
    return secretNumber;
}
public class disappearPerson {
    public static void main (String[] args) {
        String ipScore, randomNumber;

        ipScore = JOptionPane.showInputDialog(null, "Radius input");
        Integer sc = Integer.parseInt(ipScore);//   rd = radius

        if (ipScore != randomNumber) {
            System.out.println("Not a Correct Number");
        }
        else
            System.out.print("Incorrect");
    }
}

