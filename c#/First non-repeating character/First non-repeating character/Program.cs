using System;

public class Kata
{
    public static string FirstNonRepeatingLetter(string s)
    {
        for (int i = 0;i < s.Length; i++)
        {
            string everythingBut = s.Substring(0, i) + s.Substring(i + 1, s.Length - i - 1);
            if (!everythingBut.ToLower().Contains(s[i].ToString().ToLower())) return s[i].ToString();
        }
        return "";
    }
}



namespace First_non_repeating_character
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(Kata.FirstNonRepeatingLetter("a"));
            Console.WriteLine(Kata.FirstNonRepeatingLetter("stress"));
            Console.WriteLine(Kata.FirstNonRepeatingLetter("moonmen"));
        }
    }
}
