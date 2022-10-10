// Ishaan has been given a task by his teacher. He needs to find the Nth term of a series. His teacher gives him some examples to help him out (Refer examples below). He is a bit weak in pattern searching so to help him his teacher told him that the Nth term is related to prime numbers. The Nth term is the difference of N and the closest prime number to N. Help him find the Nth term for a given N.
package Hacktoberfest2022.Java_programs;
// import java.util.*;
// import java.lang.*;
import java.io.*;
public class Closes_prime {
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while(T-->0)
        {
            int N = Integer.parseInt(br.readLine().trim());
            Solution ob = new Solution();
            int ans = ob.NthTerm(N);
            System.out.println(ans);
        }
    }
}
class Solution
{
    public int NthTerm(int N)
    {
        int x = N, i=0;
        while(true){
            if(isprime(x-i)){
                return N- (x-i);
            }
            if(isprime(x+i)){
                return (x+i) -N;
            }
            i++;
        }
    } 
    
    private boolean isprime(int n){
        if(n<2) return false;
        for(int i=2; i<=Math.sqrt(n); i++){
            if(n%i ==0 )return false;
        }
        return true;
    }
}
