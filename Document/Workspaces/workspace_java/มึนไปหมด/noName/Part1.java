import java.util.Arrays;

public class Part1 {
    public static void main(String[] args) {
        double[] input = {1,2,3,4,5};
        double[] output = movingAverage(input);
        String str = Arrays.toString(output);
        System.out.println(input.length);
        System.out.println(str);
    }

    static double[] movingAverage(double[] input) {
        if(input==null)
            return null;
        if(input.length==1)
            return input;

        double[] output = new double[input.length];
        output[0] = (input[0]+input[1])/2; // ตัวแรกใน Array
        output[output.length-1] = (input[input.length-1]+input[input.length-2])/2; // ตัวสุดท้ายใน Array

        if(input.length==2)return output;
        for(int i = 1; i < output.length-1; i++) {
            output[i] = (input[i-1]+input[i]+input[i+1])/3;
        }
        return output;
    }
}
