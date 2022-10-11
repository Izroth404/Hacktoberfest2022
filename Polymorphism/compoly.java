               /* Method Overloading */
class compoly
{
	void add()
	{
		int a=10,b=20,c;
		c=a+b;
		System.out.println(c);
	}
	void add(int x,int y)
	{
		int c;
		c=x+y;
		System.out.println(c);
	}
	void add(int x,double y)
	{
		double c;
		c=x+y;
		System.out.println(c);
	}
	public static void main(String[] args) {
		compoly r=new compoly();
		r.add(); r.add(243,232); r.add(332,323.33);
	}
}