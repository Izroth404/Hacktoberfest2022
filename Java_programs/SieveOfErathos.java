import java.util.Arrays;
import java.util.Scanner;

//Algorithm to print prime numbers
public class SieveOfErathos {

	static void sieve(int n) {
		boolean[] list = new boolean[n+1];
		Arrays.fill(list, true);
		for(int i=2;i*i<=n;i++) {
			if(list[i]) {
				for(int j=i*2;j<=n;j+=i) {
					list[j] = false;
				}
			}
		}
		
		for(int i=2;i<=n;i++) {
			if(list[i]) {
				System.out.print(i+" ");
			}
		}
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter a number");
		int n = sc.nextInt();
		System.out.println("Prime Numbers");
		sieve(n);
		sc.close();
	}

}
