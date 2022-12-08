using System;
using System.Collections.Generic;
using System.Linq;

//https://www.codewars.com/kata/515bb423de843ea99400000a/train/csharp

namespace PaginationHelper
{

    public class PagnationHelper<T>
    {
        // TODO: Complete this class

        /// <summary>
        /// Constructor, takes in a list of items and the number of items that fit within a single page
        /// </summary>
        /// <param name="collection">A list of items</param>
        /// <param name="itemsPerPage">The number of items that fit within a single page</param>
        /// 
        private List<T> allItems;
        private int itemLimitPerPage;
        Dictionary<string, List<T>> Pages = new Dictionary<string, List<T>>();
        public PagnationHelper(IList<T> collection, int itemsPerPage)
        {
            Console.WriteLine(collection.Count);
            Console.WriteLine(itemsPerPage);
            allItems = collection.ToList();
            itemLimitPerPage = itemsPerPage;
            foreach (T item in collection)
            {
                string currentPage = (collection.IndexOf(item) / itemLimitPerPage).ToString();
                if (!Pages.ContainsKey(currentPage)) Pages.Add(currentPage, new List<T>());
                Pages[currentPage].Add(item);
            }

        }

        /// <summary>
        /// The number of items within the collection
        /// </summary>
        public int ItemCount
        {
            get
            {
                return allItems.Count;
            }
        }

        /// <summary>
        /// The number of pages
        /// </summary>
        public int PageCount
        {
            get
            {
                double result = allItems.Count / itemLimitPerPage;
                return (int) Math.Ceiling(result+1);
            }
        }

        /// <summary>
        /// Returns the number of items in the page at the given page index 
        /// </summary>
        /// <param name="pageIndex">The zero-based page index to get the number of items for</param>
        /// <returns>The number of items on the specified page or -1 for pageIndex values that are out of range</returns>
        public int PageItemCount(int pageIndex)
        {
            if (!Pages.ContainsKey(pageIndex.ToString())) return -1;
            return Pages[pageIndex.ToString()].Count;
        }

        /// <summary>
        /// Returns the page index of the page containing the item at the given item index.
        /// </summary>
        /// <param name="itemIndex">The zero-based index of the item to get the pageIndex for</param>
        /// <returns>The zero-based page index of the page containing the item at the given item index or -1 if the item index is out of range</returns>
        public int PageIndex(int itemIndex)
        {
            if (itemIndex < 0 || itemIndex >= allItems.Count) return -1;
            int page = itemIndex / itemLimitPerPage;
            if (Pages[page.ToString()].Count() >= itemIndex % itemLimitPerPage) return page;
            return -1;
        }
    }
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
        }
    }
}
