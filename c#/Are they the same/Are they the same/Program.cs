using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) that checks whether the two
//arrays have the "same" elements, with the same multiplicities (the multiplicity of a member is the
//number of times it appears). "Same" means, here, that the elements in b are the elements in a squared,
//regardless of the order.

//Examples
//Valid arrays
//a = [121, 144, 19, 161, 19, 144, 19, 11]
//b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
//comp(a, b) returns true because in b 121 is the square of 11, 14641 is the square of 121, 20736 the
//square of 144, 361 the square of 19, 25921 the square of 161, and so on. It gets obvious if we write
//b's elements in terms of squares:

//a = [121, 144, 19, 161, 19, 144, 19, 11]
//b = [11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19]
//Invalid arrays
//If, for example, we change the first number to something else, comp is not returning true anymore:

//a = [121, 144, 19, 161, 19, 144, 19, 11]
//b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
//comp(a, b) returns false because in b 132 is not the square of any number of a.

//a = [121, 144, 19, 161, 19, 144, 19, 11]
//b = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
//comp(a, b) returns false because in b 36100 is not the square of any number of a.

//Remarks
//a or b might be [] or
//{ } (all languages except R, Shell).
//a or b might be nil or null or None or nothing (except in C++, COBOL, Crystal, D, Dart, Elixir, Fortran,
//F#, Haskell, Nim, OCaml, Pascal, Perl, PowerShell, Prolog, PureScript, R, Racket, Rust, Shell, Swift).
//If a or b are nil (or null or None, depending on the language), the problem doesn't make sense so return false.

//Note for C
//The two arrays have the same size (> 0) given as parameter in function comp.
//    https://www.codewars.com/kata/550498447451fbbd7600041c/train/csharp

namespace Are_they_the_same
{
    class Program
    {
        public static bool comp(int[] a, int[] b)
        {
            // square a and see if we're lucky
            if (a == null | b == null)
            {
                return false;
            }
            int[] squared_a =  a.Select(x=>x*x).ToArray();
            if (squared_a == b)
            {
                return true;
            }
            // convert a & b to dictionaries with values as the number of occourances of each 
            Dictionary<int, int> a_dict = squared_a.Distinct().ToDictionary(key => key, value => squared_a.Count(x => x == value));
            Dictionary<int, int> b_dict = b.Distinct().ToDictionary(key => key, value => b.Count(x => x == value));

            a_dict.ToList().ForEach(p => Console.WriteLine(p));
            b_dict.ToList().ForEach(p => Console.WriteLine(p));
            
            return a_dict.Count == b_dict.Count && !a_dict.Except(b_dict).Any();
        }
        static void Main(string[] args)
        {
            int[] a = new int[] { 121, 144, 19, 161, 19, 144, 19, 11 };
            int[] b = new int[] { 11 * 11, 121 * 121, 144 * 144, 19 * 19, 161 * 161, 19 * 19, 144 * 144, 19 * 19 };
            bool r = comp(a, b); // True
            System.Diagnostics.Debug.Assert(r);

        }
    }
}
