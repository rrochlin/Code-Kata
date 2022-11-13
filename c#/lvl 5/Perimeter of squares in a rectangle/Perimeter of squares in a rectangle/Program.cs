

//The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8. It's easy to see that the sum
//of the perimeters of these squares is : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80 

//Could you give the sum of the perimeters of all the squares in a rectangle when there are n + 1 squares disposed
//in the same manner as in the drawing:

//alternative text

//Hint:
//See Fibonacci sequence

//Ref:
//http://oeis.org/A000045

//The function perimeter has for parameter n where n + 1 is the number of squares (they are numbered from 0 to n)
//and returns the total perimeter of all the squares.

//perimeter(5)  should return 80
//perimeter(7)  should return 216
//    https://www.codewars.com/kata/559a28007caad2ac4e000083/csharp

using System;
using System.Numerics;
using System.Collections.Generic;
using System.Linq;


namespace Perimeter_of_squares_in_a_rectangle
{
    internal class Program
    {

        public static IEnumerable<BigInteger> fibx4(BigInteger n)
        {
            BigInteger prev = 0, current = 1, temp;
            yield return 4;
            for (BigInteger count = 0; count < n;count++)
            {
                yield return 4 * (current + prev); 
                temp = prev + current;
                prev = current;
                current = temp;

            }
        }
        public static BigInteger perimeter(BigInteger n)
        {
            return fibx4(n).ToList().Aggregate(BigInteger.Add);
        }
        static void Main(string[] args)
        {
            Console.WriteLine(perimeter(5));
        }
    }
}