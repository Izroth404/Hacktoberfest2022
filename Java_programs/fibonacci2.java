import java.io.*;
public class fibonacci2 {
    public static void main(String[] args)throws IOException {
        InputStreamReader read=new InputStreamReader(System.in);
        BufferedReader in=new BufferedReader(read);
        int n=Integer.parseInt(in.readLine());
        int nth_term= fibo(n, new int[n + 1]);
        System.out.println(nth_term);
    }
    public static int fibo(int n, int[] ar){
        if(n==0 || n==1)
            return n;

        if(ar[n]!=0)
            return ar[n];

        int a=fibo(n-1, ar);
        int b=fibo(n-2, ar);
        ar[n]=a+b;
        System.out.println(ar[n]);
        return ar[n];

    }
}
