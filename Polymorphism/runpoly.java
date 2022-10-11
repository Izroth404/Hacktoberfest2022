                   /* Method Overriding */
class Demo
{
	void draw()
	{
		System.out.println("Can't say shape type");
	}
}
class square extends Demo
{
	@Override
	void draw()
	{
		System.out.println("square shape");
	}
}
class runpoly
{
	public static void main(String[] args) {
		Demo r=new square();
		r.draw();
	}
}