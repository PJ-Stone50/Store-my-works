import java.text.DecimalFormat;
 
public class JavaDecimalFormatExample {
 
    private static final String COMMA_SEPERATED = "###,###.###";
        private static double number = 12345.6;
 
    public static void main(String[] args) {
 
        DecimalFormat decimalFormat = new DecimalFormat(COMMA_SEPERATED);
        System.out.println(decimalFormat.format(number));
    }
}