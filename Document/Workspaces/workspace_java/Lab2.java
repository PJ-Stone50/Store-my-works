import javax.swing.JOptionPane;
import javax.swing.JFrame;
// import java.text.DecimalFormat;
import java.math.BigDecimal;
import java.math.RoundingMode;

public class Lab2 { 
 public static void main (String[] args) {
  float result, PI = 3.14159265359f ;
  String inputStr;
//   รับ input เป็นค่า String
  inputStr = JOptionPane.showInputDialog(null, "Radius input");
//   เปลี่ยนค่า String ของ input ให้เป็น Integer เพื่อใช้คำนวณ
  Float rd = Float.parseFloat(inputStr);//   rd = radius
// สูตรคำนวณหาพื้นที่วงกลม
  result = (rd*rd) * PI ;

//   .setScale(2, RoundingMode.DOWN) ==> เอาตั้งแต่หลักที่2, ปิดโหมดตัดเศษ
  BigDecimal area = new BigDecimal(result).setScale(2, RoundingMode.DOWN);
//   newrd ถูกชี้ address จาก rd แล้วทำให้ทศนิยมหายไป
  BigDecimal newrd = new BigDecimal(rd).setScale(0, RoundingMode.DOWN);
// สร้างเฟรมใหม่ ไว้โชว์ messageDialog
  JFrame frame = new JFrame("JOptionPane showMessageDialog example");

  
  JOptionPane.showMessageDialog(frame,"The area of circle with radius "+ newrd + " is " + area + "");
  
  

//   System.out.printf("Radius is here ==>" +" %.2f" ,rd);

//   System.out.printf("Area of circle ==> %.2f",result);
  
 }
}
