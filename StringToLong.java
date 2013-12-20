
class ConvertStringToLong
{
    long convertFunc(String input)
    { 
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
                //throw exception
           } 
           count += 1; 
        }
        return output;         
    }
}

class TestStringToLong
{
    String testCaseOne = "123421";
    String testCaseTwo = "9231233";

    public void checkStringToLong()
    {
        ConvertStringToLong stol = new ConvertStringToLong();
        //Assert.assertEquals(123, 344);
        //Assert.assertEquals(323, 443);
     }
}

class StringToLong
{
    public static void main(String[] args)
    {
        String input;
        ConvertStringToLong stol = new ConvertStringToLong();
        input = "4343";
        System.out.println(stol.convertFunc(input)); 
        
        //Testing logic
        TestStringToLong tstol = new TestStringToLong();
        tstol.checkStringToLong();
    }
}
