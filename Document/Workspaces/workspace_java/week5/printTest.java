public class printTest {
    public static void printVariableType(String[] theVariable){
        String name = theVariable.getClass().getSimpleName();
        System.out.println(theVariable.getClass());
    }
}
