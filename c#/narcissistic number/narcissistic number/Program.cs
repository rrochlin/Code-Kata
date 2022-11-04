using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


//A Narcissistic Number is a positive number which is the sum of its own digits, each raised
//to the power of the number of digits in a given base. In this Kata, we will restrict ourselves to decimal (base 10).

//For example, take 153 (3 digits), which is narcisstic:
//    1 ^ 3 + 5 ^ 3 + 3 ^ 3 = 1 + 125 + 27 = 153

//and 1652(4 digits), which isn't:
//    1^4 + 6^4 + 5^4 + 2^4 = 1 + 1296 + 625 + 16 = 1938

//  The Challenge:

//Your code must return true or false (not 'true' and 'false') depending upon whether the given number
//is a Narcissistic number in base 10. This may be True and False in your language, e.g. PHP.

//Error checking for text strings or other invalid inputs is not required, only valid positive non-zero
//integers will be passed into the function.
//https://www.codewars.com/kata/5287e858c6b5a9678200083c/train/csharp

namespace narcissistic_number
{
    class Program
    {
        public static bool Narcissistic(int value)
        {
            int total = 0;
            int power = value.ToString().Length;
            int narcissus = value;
            while (value > 0)
            {
                total += (int) Math.Pow(value % 10, power);
                value = value / 10;
            }

            return narcissus == total;
        }
        static void Main(string[] args)
        {
            Console.WriteLine(Narcissistic(1));
            Console.WriteLine(Narcissistic(371));
            Console.WriteLine(Narcissistic(300));
        }
    }
}
