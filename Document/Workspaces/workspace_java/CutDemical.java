import java.text.DecimalFormat;
import javax.swing.JOptionPane;


public class CutDemical {
 public static void main(String[] args) {
    String inputStr;

    inputStr = JOptionPane.showInputDialog(null, "Radius input");
    double num = 123.4567;
    DecimalFormat df = new DecimalFormat("#.###");

    System.out.println(df.format(num));     
 }
}
