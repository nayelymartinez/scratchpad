class OverloadingExample
{
	public void print_something(char c)
	{
		System.out.println(c);
	}

	public void print_something(char c, int n)
	{
		System.out.println(c + " " + n)
	}
}