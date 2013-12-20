/**
Program to convert given string to long
**/

class ConvertStringToLong
{
    long convertFunc(String input)
    {
        //Function which converts given string to long
        long output = 0;
        char[] chars = input.toCharArray();
        int count = 0;
        int length = input.length();

        for(char c : chars)
        {
           if (((int)c) > 48 && ((int) c) < 57)
           {
                output += (((int)c) - 48) * Math.pow(10, length-count-1) ; 
           }
           else
           {
                throw new RuntimeException();
           } 
           count += 1; 
        }
        return output;         
    }
}


class StringToLong
{
    public static void main(String[] args)
    {
        String input = "4243";
        long output = 0;

        try
        {
            //Convert given string to long
            ConvertStringToLong stol = new ConvertStringToLong();
            output = stol.convertFunc(input);
            if ( output== Long.valueOf(input).longValue())
            {
                System.out.println("Successly converted string to long");
            }
        }
        catch (Exception e)
        {
                System.out.println("Warning: Input is not convertible");
            
        }
    }
}
