using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//Complete the solution so that the function will break up camel casing, using a space between words.

//Example
//"camelCasing"  =>  "camel Casing"
//"identifier"   =>  "identifier"
//""             =>  ""
//https://www.codewars.com/kata/5208f99aee097e6552000148/train/csharp

namespace Break_camelCase
{
    class Program
    {
        public static string BreakCamelCase(string str)
        {
            string upper_str = str.ToUpper();
            int count = 0;
            string broken = "";
            foreach (char c in upper_str)
            {
                if (str[count] == c)
                {
                    broken += str.Substring(0, count) + " ";
                    str = str.Substring(count, str.Length - count);
                    count = 0;
                }
                count++;
            }
            broken += str;
            return broken;
        }
        static void Main(string[] args)
        {
            Console.WriteLine(BreakCamelCase("camelCasing"));
            Console.WriteLine(BreakCamelCase("identifier"));
            Console.WriteLine(BreakCamelCase(""));
        }
    }
}
