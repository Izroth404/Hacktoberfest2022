//2d matrix start from left go towards right. u can jump 1 step up-right, right, down-right. find the max u can collect in 1 route

import java.io.*;
public class goldmine {
    public static void main(String[] args)throws IOException {
        InputStreamReader read=new InputStreamReader(System.in);
        BufferedReader in=new BufferedReader(read);
        int n, i, j;
        n=Integer.parseInt(in.readLine());
        int[][] grid=new int[n][n];
        for(i=0;i<n;i++)
            for(j=0;j<n;j++)
                grid[i][j]=Integer.parseInt(in.readLine());
        int cost=findGold(n,grid);
        System.out.println(cost);
    }
    public static int findGold(int n, int[][] mine)
    {
        int i,j;
        int [][] maxGold=new int[n][n];
        for(j=n-1;j>=0;j--)
            for(i=n-1;i>=0;i--)
            {
                if(j==n-1) {
                    maxGold[i][j]=mine[i][j];
                }
                else if(i==0){
                    maxGold[i][j]=mine[i][j]+Math.max(maxGold[i][j+1],maxGold[i+1][j+1]);
                }
                else if(i==n-1)
                {
                    maxGold[i][j]=mine[i][j]+ Math.max(maxGold[i][j+1],maxGold[i-1][j+1]);
                }
                else
                {
                    maxGold[i][j]=mine[i][j]+Math.max(Math.max(maxGold[i][j+1],maxGold[i+1][j+1]),maxGold[i-1][j+1]);
                }
            }
        int max=maxGold[0][0];
//        for(i=0;i<n;i++) {
//            for (j = 0; j < n; j++)
//                System.out.print(maxGold[i][j] + "\t");
//            System.out.println();
//        }
        for(i=0;i<n;i++)
        {
            if(maxGold[i][0]>max)
                max=maxGold[i][0];
        }
        return max;
    }
}

