class Palindrome

{

    public String is_palindrome(int n)

    {
        if(n>0 &&n<10)
        return "Yes";
        //1
        String s = Integer.toString(n);
        int l = s.length();
        int j=l-1;
        for(int i=0;i<=l/2;i++)
        {
            char c1=s.charAt(i);
            char c2=s.charAt(j);      

            if(c1==c2)

            {
                j--;
                continue;
            }

            else

            {
                return "No";
            }
        }
        return "Yes";
        int num = n;
        int temp =0,res = 0;
        while(n!=0)
        {

            temp = n%10;
            n=n/10;
            res = (res*10)+temp;
        }
        if(res == num)
        {
            return "Yes";
        }
        return "No";
   }

}