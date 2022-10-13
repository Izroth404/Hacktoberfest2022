import java.util.Scanner;

public class LCM {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter two numbers");
		int a = sc.nextInt();
		int b = sc.nextInt();
		int n1 = a;
		int n2 = b;
		if (a < b) {
			int temp = a;
			a = b;
			b = temp;
		}
		int gcd = 0;
		while (a % b != 0) {
			int rem = a % b;
			a = b;
			b = rem;
		}
		gcd = b;
		int lcm = (n1 * n2) / gcd;
		System.out.println(lcm);
	}

}
