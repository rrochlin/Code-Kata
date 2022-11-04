using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] arr = { 9, 4, 10, 42 };
            Array.Sort(arr);
            double x = Math.Sqrt(arr[1]);
            Console.WriteLine(x);
        }
    }
}
