using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//Create a function named divisors/Divisors that takes an integer n > 1 and returns an
//array with all of the integer's divisors(except for 1 and the number itself), from
//smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#)
//(use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

//Example:
//Kata.Divisors(12) => new int[] { 2, 3, 4, 6 };
//Kata.Divisors(25) => new int[] { 5 };
//Kata.Divisors(13) => null;
//https://www.codewars.com/kata/544aed4c4a30184e960010f4/train/csharp

namespace Find_the_divisors
{
    class Program
    {
        public static int[] Divisors(int n)
        {
            int divisor = 2;
            List<int> val = new List<int>();
            // better solution space/time is to go to divisor =< sqrt of n. Then parse the list for the pairs
            // of the numbers you will get that way. saves a HUGE amount of time the larger the number.
            // I.E. for 1,000,000 you only need to check the first 1,000 numbers, then solve the rest.
            while (divisor < n)
            {   
                if ((n % divisor) == 0)
                {
                    val.Add(divisor);
                }
                divisor++;
            }
            

            return val.Count != 0 ? val.ToArray() : null;
        }
        static void Main(string[] args)
        {
            Console.WriteLine(Divisors(12));
            Console.WriteLine(Divisors(25));
            Console.WriteLine(Divisors(13));
        }
    }
}
