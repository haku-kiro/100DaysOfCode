/*

Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

 */

 //My solution
//I don't like it 

 using System;

public static class Kata
{
  public static string Replace(string s)
  {
    var vowels = "aeiouAEIOU".ToCharArray();
    foreach (var x in vowels)
      s = s.Replace(x, '!');
    return s;
  }
}

//This is what i should look like :
using System.Text.RegularExpressions;

public static class Kata
{
  public static string Replace(string s)
   => Regex.Replace(s, @"[aeiou]","!", RegexOptions.IgnoreCase);
}


//Or even:
using System.Text.RegularExpressions;

public static class Kata
{
  public static string Replace(string s) =>
    Regex.Replace(s, @"[aeiouAEIOU]", "!");
}


// A bit of a weird/wonderful one:

using System;
using System.Linq;

public static class Kata
{
  public static string Replace(string s)
  {
    string vowels = "aeiouAEIOU";
    s = string.Concat(s.Select(c => vowels.Contains(c) ? '!' : c));
    return s;
  }
}


//Lol
using System;
public static class Kata
{
  public static string Replace(string s)
  {
      return s.Replace("a","!")
              .Replace("e","!")
              .Replace("i","!")
              .Replace("u","!")
              .Replace("o","!")
              .Replace("A","!")
              .Replace("E","!")
              .Replace("I","!")
              .Replace("U","!")
              .Replace("O","!");
  }
}
