/*

Character recognition software is widely used to digitise printed texts. Thus the texts can be edited, searched and stored on a computer.

When documents (especially pretty old ones written with a typewriter), are digitised character recognition softwares often make mistakes.

Your task is correct the errors in the digitised text. You only have to handle the following mistakes:

    S is misinterpreted as 5
    O is misinterpreted as 0
    I is misinterpreted as 1


 */

 // My solution:

 public class Kata
{
  public static string Correct(string text)
  {
    var x = text.ToCharArray();
    for (var y = 0; y < x.Length; y++)
    {
       switch(x[y])
       {
         case '5':
           x[y] = 'S';
         break;
         case '0':
           x[y] = 'O';
         break;
         case '1':
           x[y] = 'I';
         break;
       }
    }
    return new string(x);
  }
}


// Best practise:
public class Kata
{
  public static string Correct(string text)
  {
    return text
    .Replace("0", "O")
    .Replace("1", "I")
    .Replace("5", "S");
  }
}

// One I found really cool:

using System.Linq;

public class Kata
{
    public static string Correct(string text)
    {
        return new string(text.Select(x => 
        {
           switch (x)
           {
               case '0': return 'O';
               case '1': return 'I';
               case '5': return 'S';
               default: return x;
           }
           
        }).ToArray());
    }
}