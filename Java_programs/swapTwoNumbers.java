import java.util.*;

class swapTwoNumbers{
  public static void main(String[] args){
    Scanner sc = new Scanner(System.in);
    int a = sc.nextInt();
    int b = sc.nextInt();
    int temp = a;
    System.out.println("Before swap a:"+a+"and b:"+b);
    a = b;
    b = temp;
    System.out.println("After swap a:"+a+"and b:"+b);
  }
}  
