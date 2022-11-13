using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//Check to see if a string has the same amount of 'x's and 'o's. The method must return a
//boolean and be case insensitive. The string can contain any char.

//Examples input/output:

//XO("ooxx") => true
//XO("xooxx") => false
//XO("ooxXm") => true
//XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
//XO("zzoo") => false
//https://www.codewars.com/kata/55908aad6620c066bc00002a/train/csharp

namespace Exes_and_Ohs
{
    class Program
    {
        public static bool XO(string input)
        {
            input.ToLower();
            int X = input.Count(chr => chr == 'X' | chr == 'x');
            int O = input.Count(chr => chr == 'O' | chr == 'o');
            return X == O;
        }
        static void Main(string[] args)
        {
            Console.WriteLine( XO("ooxx"));
            Console.WriteLine(XO("xooxx"));
            Console.WriteLine(XO("ooxXm"));
            Console.WriteLine(XO("zpzpzpp"));
            Console.WriteLine(XO("zzoo"));
        }
    }
}
