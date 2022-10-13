import java.util.*;
public class Batonpassing {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int t = sc.nextInt();

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = i+1;
        }
        int k=0,flag=0;
        for(int i = 0; i < t; i++) {
            if(k==n){
                flag=1;
            }
            if(k==0){
                flag=0;
            }
            if (flag==1) {
                k--;
            } else {
                k++;
            }
        }
        List<Integer> list = new ArrayList<>();
        if(flag==1)
        {
            list.add(arr[k-1]);
            list.add(arr[k-2]);
        }else{
            list.add(arr[k-1]);
            list.add(arr[k]);
        }
        return list;
    }
}
