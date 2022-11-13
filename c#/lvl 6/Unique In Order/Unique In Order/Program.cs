using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//Implement the function unique_in_order which takes as argument a sequence and returns a 
//    list of items without any elements with the same value next to each other and preserving
//    the original order of elements.

//For example:

//uniqueInOrder("AAAABBBCCDAABBB") == { 'A', 'B', 'C', 'D', 'A', 'B'}
//uniqueInOrder("ABBCcAD") == { 'A', 'B', 'C', 'c', 'A', 'D'}
//uniqueInOrder([1, 2, 2, 3, 3])       == { 1,2,3}
//https://www.codewars.com/kata/54e6533c92449cc251001667/train/csharp

namespace Unique_In_Order
{
    class Program
    {
        public static IEnumerable<T> UniqueInOrder<T>(IEnumerable<T> iterable)
        {
            List<T> result = new List<T>();
            foreach (var item in iterable.Select((Value, Index) => new { Value, Index }))
            {
                Console.WriteLine(default(T));
                // in C# & will evaluate both operands but && won't eval more than needed, same with | and ||.
                if (item.Index > 0 && !result[result.Count() - 1].Equals(item.Value))
                {
                    result.Add(item.Value);
                } else if (item.Index ==0) result.Add(item.Value);
            }

            return result;
        }
        static void Main(string[] args)
        {
            UniqueInOrder("AAAABBBCCDAABBB").ToList().ForEach(p=>Console.Write(p));
            Console.WriteLine();
            UniqueInOrder("ABBCcAD").ToList().ForEach(p => Console.Write(p));
            Console.WriteLine();
            UniqueInOrder(new List<int> { 1, 2, 2, 3, 3 }).ToList().ForEach(p => Console.Write(p));
            Console.WriteLine();
            UniqueInOrder(new List<int> { 1, 2, 3, 3 }).ToList().ForEach(p => Console.Write(p));
            Console.WriteLine();
        }
    }
}
