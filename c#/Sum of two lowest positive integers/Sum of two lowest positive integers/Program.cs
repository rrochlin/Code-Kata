using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//Create a function that returns the sum of the two lowest positive numbers given an array of
//minimum 4 positive integers. No floats or non-positive integers will be passed.

//For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

//[10, 343445353, 3453445, 3453545353453] should return 3453455.
//https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/csharp

namespace Sum_of_two_lowest_positive_integers
{
    class Program
    {
        public static int sort_method_sumTwoSmallestNumbers(int[] numbers)
        {
            var watch = new System.Diagnostics.Stopwatch();
            watch.Start();
            Array.Sort(numbers);
            watch.Stop();
            Console.WriteLine($"Execution Time for sort method: {watch.ElapsedMilliseconds} ms");
            return numbers[0] + numbers[1];
        }
        public static int comp_method_sumTwoSmallestNumbers(int[] numbers)
        {
            var watch = new System.Diagnostics.Stopwatch();
            watch.Start();
            var x = int.MaxValue;
            var y = int.MaxValue;

            foreach (var z in numbers)
            {
                if (z < x)
                {
                    y = x;
                    x = z;
                }
                else if (z < y)
                {
                    y = z;
                }
            }
            watch.Stop();
            Console.WriteLine($"Execution Time for comparison method: {watch.ElapsedMilliseconds} ms");
            return x + y;
        }
        static void Main(string[] args)
        {
            int[] small_test = new int[10];
            int[] med_test = new int[1000];
            int[] mid_test = new int[10000];
            int[] large_test = new int[1000000];
            Random randNum = new Random();

            for (int i = 0; i < small_test.Length; i++)
            {
                small_test[i] = randNum.Next(0, small_test.Length * 10);
            }
            for (int i = 0; i < med_test.Length; i++)
            {
                med_test[i] = randNum.Next(0, small_test.Length*10);
            }
            for (int i = 0; i < large_test.Length; i++)
            {
                large_test[i] = randNum.Next(0, small_test.Length * 10);
            }

            Console.WriteLine("testing with arrays of size 10");
            sort_method_sumTwoSmallestNumbers(small_test);
            comp_method_sumTwoSmallestNumbers(small_test);
            Console.WriteLine("testing with arrays of size 1000");
            sort_method_sumTwoSmallestNumbers(med_test);
            comp_method_sumTwoSmallestNumbers(med_test);
            Console.WriteLine("testing with arrays of size 10,000");
            sort_method_sumTwoSmallestNumbers(mid_test);
            comp_method_sumTwoSmallestNumbers(mid_test);
            Console.WriteLine("testing with arrays of size 10^6");
            sort_method_sumTwoSmallestNumbers(large_test);
            comp_method_sumTwoSmallestNumbers(large_test);
        }
    }
}
