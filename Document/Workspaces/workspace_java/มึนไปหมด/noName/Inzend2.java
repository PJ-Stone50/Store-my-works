import javax.swing.JOptionPane;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.table.DefaultTableModel;

import java.util.Arrays;

//สุดยอดแห่งความมึน
public class Inzend2 {

   public static void main(String[] args) {
      // Creating array
      int[][] blastTable = new int[][] { { 32, 31, 30, 29, 28, 27, 26, 25 },
            { 24, 23, 22, 21, 20, 19, 18, 17 },
            { 16, 15, 14, 13, 12, 11, 10, 9 }, { 8, 7, 6, 5, 4, 3, 2, 1 },
            { 0, -1, -2, -3, -4, -5, -6, -7 },
            { -8, -9, -10, -11, -12, -13, -14, -15 },
            { -16, -17, -18, -19, -20, -21, -22, -23 },
            { -24, -25, -26, -27, -28, -29, -30, -31 } };

      printArray(blastTable);
   }

   // Method to print two dimensional array in a JOptionPane
   public static void printArray(int[][] num1) {
      String[] columnNames = { "A", "B", "C", "D", "E", "F", "G", "H" };

      // table models expect reference type data, and so
      // int array must be changed to an Integer array
      Integer[][] data = new Integer[num1.length][num1[0].length];
      for (int i = 0; i < data.length; i++) {
         for (int j = 0; j < data[i].length; j++) {
            data[i][j] = num1[i][j];
         }
      }
      DefaultTableModel model = new DefaultTableModel(data, columnNames);
      JTable table = new JTable(model);
      JScrollPane scrollPane = new JScrollPane(table);

      JOptionPane.showMessageDialog(null, scrollPane, "Uitvoer",
            JOptionPane.INFORMATION_MESSAGE);
   }
}