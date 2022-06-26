public class StringToFloat {


  public static void main (String[] args)
  {

    // String s = "fred";    // do this if you want an exception

    String s = "100.00";

    try
    {
      float f = Float.valueOf(s.trim()).floatValue();
      System.out.println("float f = " + f);
    }
    catch (NumberFormatException nfe)
    {
      System.out.println("NumberFormatException: " + nfe.getMessage());
    }
  }
}