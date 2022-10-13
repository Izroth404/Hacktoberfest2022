import java.util.*;
public class Math_MaxAndMin {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int num1 = sc.nextInt();
        int num2 = sc.nextInt();

        //Finding Maximum of two numbers
        System.out.println("Maximum = " + Math.max(num1,num2));

        //Finding minimum of two number
        System.out.println("Minimum = " + Math.min(num1,num2));
    }
}
