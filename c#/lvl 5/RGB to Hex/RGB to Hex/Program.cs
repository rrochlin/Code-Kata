using System;
using Microsoft.VisualBasic;


//The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal
//representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range
//must be rounded to the closest valid value.

//Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

//The following are examples of expected output values:

//Rgb(255, 255, 255) # returns FFFFFF
//Rgb(255, 255, 300) # returns FFFFFF
//Rgb(0, 0, 0) # returns 000000
//Rgb(148, 0, 211) # returns 9400D3


namespace RGB_to_Hex
{
    internal class Program
    {
        public static string Rgb(int r, int g, int b)
        {
            string result = "";
            foreach (int c in new int[] { r, g, b } ){
                if (c >= 0 && c <= 255)
                {
                    string hex = Conversion.Hex(c);
                    result += hex.Length == 1 ? "0"+hex : hex;
                }
                else result += c > 0 ? "FF" : "00";
            }
            return result;
        }
        static void Main(string[] args)
        {
            Console.WriteLine(Rgb(255, 255, 255));
            Console.WriteLine(Rgb(255, 255, 300));
            Console.WriteLine(Rgb(0, 0, 0));
            Console.WriteLine(Rgb(148, 0, 211));
        }
    }
}
