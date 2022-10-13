import java.util.Scanner;

//calculate power in logn time
public class PowerLogarithmic {

	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter number");
		int x = sc.nextInt();
		System.out.println("Enter power");
		int n = sc.nextInt();
		System.out.println(power(x, n));
	}

	public static int power(int x, int n) {
		if (n == 0) {
			return 1;
		}
		int p = power(x, n / 2);
		int ans = p * p;
		if (n % 2 != 0) {
			ans *= x;
		}
		return ans;
	}

}
