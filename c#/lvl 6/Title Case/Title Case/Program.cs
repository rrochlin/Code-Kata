using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//A string is considered to be in title case if each word in the string is either(a) capitalised
//(that is, only the first letter of the word is in upper case) or(b) considered to be an exception
//and put entirely into lower case unless it is the first word, which is always capitalised.

//Write a function that will convert a string into title case, given an optional list of exceptions
//(minor words). The list of minor words will be given as a string with each word separated by a space.
//Your function should ignore the case of the minor words string -- it should behave in the same way
//even if the case of the minor word string is changed.

//First argument (required): the original string to be converted.
//Second argument (optional): space - delimited list of minor words that must always be lowercase except
//for the first word in the string. The JavaScript/CoffeeScript tests will pass undefined when this argument is unused.
//###Example

//Kata.TitleCase("a clash of KINGS", "a an the of")   => "A Clash of Kings"
//Kata.TitleCase("THE WIND IN THE WILLOWS", "The In") => "The Wind in the Willows"
//Kata.TitleCase("the quick brown fox")               => "The Quick Brown Fox"
//https://www.codewars.com/kata/5202ef17a402dd033c000009/train/csharp

namespace Title_Case
{
    class Program
    {
        public static string TitleCase(string title, string minorWords = "")
        {
            string[] words = title.Split(' ');
            HashSet<string> minorWordSet;
            try
            {
                minorWordSet = new HashSet<string>(minorWords.ToLower().Split(' '));
            }
            catch (System.NullReferenceException)
            {
                minorWordSet = new HashSet<string>();
            }
            string new_title = "";
            int index = 0;
            foreach(string word in words)
            {
                if (!minorWordSet.Contains(word.ToLower()) | index == 0)
                {
                    char[] x = word.ToLower().ToCharArray();
                    try
                    {
                        x[0] = (char)(x[0] - 32);
                        new_title += new string(x);
                    }
                    catch (System.IndexOutOfRangeException)
                    {
                        continue;
                    }
                }
                else
                {
                    new_title += word.ToLower();
                }
                if (index < words.Length-1)
                {
                    new_title += " ";
                }
                index++;
            }

            return new_title;
        }
        static void Main(string[] args)
        {
            Console.WriteLine(TitleCase("a clash of KINGS", "a an the of")+'a');// == "A Clash of Kings");
            Console.WriteLine(TitleCase("THE WIND IN THE WILLOWS", "The In") == "The Wind in the Willows");
            Console.WriteLine(TitleCase("the quick brown fox") == "The Quick Brown Fox");
            Console.WriteLine(TitleCase(""));
            Console.WriteLine(TitleCase("First a of in","an often into"));
            Console.WriteLine(TitleCase("First a of in",null));
        }
    }
}
