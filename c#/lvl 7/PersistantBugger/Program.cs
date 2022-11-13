using System;

namespace PersistantBugger
{
    class Program
    {
        public static long Persistance(long n)
        {
            string number = System.Convert.ToString(n);
            int count = 0;
            while (n >= 10)
            {
                long total = 1;
                foreach (char num in number)
                {
                    total *= System.Convert.ToInt64(num) - 48;
                }
                n = total;
                number = System.Convert.ToString(n);
                count++;
            }


            return count;
        }
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World");
            Console.WriteLine(Persistance(25));
        }
    }
}
