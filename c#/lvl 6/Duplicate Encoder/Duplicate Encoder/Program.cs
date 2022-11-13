using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//The goal of this exercise is to convert a string to a new string where each character in
//the new string is "(" if that character appears only once in the original string, or ")"
//if that character appears more than once in the original string. Ignore capitalization when
//determining if a character is a duplicate.
//https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/csharp
//"din"      =>  "((("
//"recede"   =>  "()()()"
//"Success"  =>  ")())())"
//"(( @"     =>  "))(("


namespace Duplicate_Encoder
{
    class Program
    {
        public static string DuplicateEncode(string word)
        {
            string parsedWord = "";
            word = word.ToLower();
            foreach(char l in word)
            {
                string[] subs = word.Split(l);
                if (subs.Length > 2)
                {
                    parsedWord += ")";
                } else
                {
                    parsedWord += "(";
                }
            }
            return parsedWord;
        }
        static void Main(string[] args)
        {
            //Console.WriteLine(DuplicateEncode("din") == "(((");
            Console.WriteLine(DuplicateEncode("recede") == "()()()");
            Console.WriteLine(DuplicateEncode("Success") == ")())())");
            //Console.WriteLine(DuplicateEncode("(( @") == "))((");
        }
    }
}
