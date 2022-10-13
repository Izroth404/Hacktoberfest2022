import java.util.Scanner;

//perform action by displaying steps
public class TowerOfHanoi {

	public static void main(String[] args) throws Exception {
		Scanner sc = new Scanner(System.in);
		System.out.println("Enter number of disks");
		int n = sc.nextInt();
		System.out.println("Enter first tower id");
		int t1id = sc.nextInt();
		System.out.println("Enter second tower id");
		int t2id = sc.nextInt();
		System.out.println("Enter third tower id");
		int t3id = sc.nextInt();
		toh(n,t1id,t2id,t3id);
    }

    public static void toh(int n, int t1id, int t2id, int t3id){
        if(n==0) {
        	return;
        }
        toh(n-1,t1id,t3id,t2id);
        System.out.println(n + "["+t1id+"->"+t2id+"]");
        toh(n-1,t3id,t2id,t1id);
    }

}
