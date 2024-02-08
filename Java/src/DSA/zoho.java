package DSA;

import java.util.Arrays;

public class zoho {

	public static void main(String[] args) {
		/*
		 *
		 *  String manipulation
			Input: a1b10
       		Output: abbbbbbbbbb
		 */
		System.out.println(manipulate("a1b3c4"));
			
	}
	static StringBuilder manipulate(String str)
	{
		char[] chararr=str.toCharArray();

		StringBuilder ans=new StringBuilder();
		char c ='0';
		for (char i : chararr)
		{
			if (Character.isDigit(i))
			{
				int digit = Character.getNumericValue(i);
				while (digit > 0)
				{
					ans.append(c);
					digit--;
				}
			}
			else
			{
				c = i;
			}
		}		
		return ans;		
	}

}
