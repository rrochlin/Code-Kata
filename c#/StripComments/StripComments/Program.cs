using System;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

    public class StripCommentsSolution
    {
        public static string StripComments(string text, string[] commentSymbols)
        {
            string[] lines = text.Split('\n');
            string result = "";
            foreach(string line in lines)
        {
            Console.WriteLine(line);
        }

            foreach (string line in lines)
            {
                int commentIndex = line.Length;

                IEnumerable<string> commentCheck = commentSymbols.Where(comment => line.Contains(comment));

                if (commentCheck.Count() > 0) commentIndex = commentCheck.Select(c => line.IndexOf(c)).Min();

                result += line.Substring(0, commentIndex).TrimEnd() + '\n';

            }
            
        return result.Substring(0,result.Length-1);
        }
    }

namespace StripComments
{

    internal class Program
    {


        static void Main(string[] args)
        {
            
               
            Console.WriteLine(StripCommentsSolution.StripComments("apples, pears # and bananas\ngrapes\nbananas !apples", new string[] { "#", "!" }));

            Console.WriteLine(StripCommentsSolution.StripComments("a #b\nc\nd $e f g", new string[] { "#", "$" }));

            Console.WriteLine(StripCommentsSolution.StripComments("nothing to do", new string[] { "#", "$" }));

            Console.WriteLine(StripCommentsSolution.StripComments("testing $cash", new string[] { "#", "$" }));

        }
    }
}
