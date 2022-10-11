import java.util.*;
public class targetSumSubset {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int i,n;
        n=sc.nextInt();
        int[] list=new int[n];
        for(i=0;i<n;i++)
            list[i]=sc.nextInt();
        System.out.println("Target:");
        int target=sc.nextInt();
        int possibility= targetSum(n,list,target);
        if(possibility==1)
            System.out.println("target is possible.");
        else
            System.out.println("Target is not possible.");
    }
    public static int targetSum(int len, int[] list, int target)
    {
        int[][] grid=new int[len+1][target+1];
        int i;
        for(i=0;i<=len;i++)
        {
            for(int j=0;j<=target;j++)
            {
                if(i==0 &&j==0)
                    grid[i][j]=1;
                else if(i==0)
                {
                    grid[i][j]=0;
                }
                else if (j==0) {
                    grid[i][j]=1;
                }
                else
                {
                    if(grid[i-1][j]==1)
                        grid[i][j]=1;
                    int val=list[i-1];
                    if(j>=val){
                        if(grid[i-1][j-val]==1)
                            grid[i][j]=1;
                    }
                }
            }
        }
        return grid[len][target];
    }
}
