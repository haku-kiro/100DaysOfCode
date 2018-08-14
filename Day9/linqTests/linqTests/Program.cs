using System;
using System.Collections.Generic;
using System.Linq;

namespace linqTests
{
    class Program
    {
        static void Main(string[] args)
        {
            //Data sets
            Dictionary<string, int> d = new Dictionary<string, int>()
            {
                {"cat", 2},
                {"dog", 1},
                {"llama", 0},
                {"iguana", -1}
            };

            List<int> primes = new List<int>(new int[] { 2, 3, 5, 7, 11, 13 });

            string[] arr1 = new string[] { "one", "two", "three", "four", "five", "six", "seven" };



            var fruits = new List<Fruit>()
            {
                new Fruit() { Id = 1, Name = "Orange", Color = "Orange", Quantity = 3   },
                new Fruit() { Id = 2, Name = "Strawberry", Color = "Red",    Quantity= 12  },
                new Fruit() { Id = 3, Name = "Grape",      Color = "Purple", Quantity= 25  },
                new Fruit() { Id = 4, Name = "Pineapple",  Color = "Yellow", Quantity= 1   },
                new Fruit() { Id = 5, Name = "Apple",      Color = "Red",    Quantity= 5   },
                new Fruit() { Id = 6, Name = "Mango",      Color = "Yellow", Quantity= 2   }
            };

            //LINQ

            //Linq first
            //Returns the first element that satisfies an optional, given param
            //Throws an InvalidOperationException if nothing is found

            //This is without param
            var firstFruit = fruits.First(); //Returns orange

            //This is with a param
            var firstYellowFruit = fruits.First(f => f.Color == "Yellow"); //Returns Pineapple
            Console.WriteLine(firstYellowFruit.Name);

            //Linq FirstOrDefault
            //Same as first, but if nothing is found returns the default value
            var firstFruit2 = fruits.FirstOrDefault(); //returns orange
            var firstGreenFruit = fruits.FirstOrDefault((f) => { return f.Color == "Green"; }); //Just using longhand lambda as well, cos



            //Return the amount of mangos in the dataset
            var mangoQt = fruits.FirstOrDefault(f => f.Name == "Mango").Quantity;
            Console.WriteLine(mangoQt); //should return 2


            //Console.WriteLine(firstGreenFruit.Name); //This would be null, which means it will through a null ref exception

            //Linq Where
            // Filters data based on predicate
            var yellowFruits = fruits.Where(f => f.Color == "Yellow");
            foreach (Fruit fruit in yellowFruits)
            {
                Console.WriteLine(fruit.Name);
            }


            //Linq Select
            //Projects data
            var dataProjected = fruits.Where(f => f.Name == "Mango").Select(f => f.Quantity); //should return 2
            Console.WriteLine(dataProjected.FirstOrDefault());


            //Linq ToDictionary
            //Returns a dictionary from a dataset
            var fruitsById = fruits.ToDictionary(k => k.Id, v => v.Name); //key value, k = id, v = name
            foreach (var item in fruitsById)
            {
                Console.WriteLine($"K:{item.Key}|V:{item.Value}");
            }

            //Can group by beforehand (Look at this again in depth)
            var fruitsByColorDict = fruits.GroupBy(g => g.Color).ToDictionary(k => k.Key, v => v.ToList()); // creates a dict that is grouped, and has the data as a list in the value
            foreach (var item in fruitsByColorDict)
            {
                Console.WriteLine($"Key: {item.Key}");
                foreach (var item2 in item.Value)
                {
                    Console.WriteLine($"\t Value = {item2.Name}");
                }
            }

            //Linq ToList
            //Can create a list 

            //Using select to get a specific value
            var listofnames = fruits.Select(f => f.Name).ToList();

            //returns all the names in the collection as a list
            foreach (var item in listofnames)
            {
                Console.WriteLine(item);
            }

            //another where clause
            //Fruits where we're runing out of stock!

            //Note that you should make a PR to the fcc examples as they are very wrong
            var almostOutOfStockGasp = fruits.Where(f => f.Quantity <= 3).Select(f => f.Name).ToList();
            Console.WriteLine("THE STOCK");
            foreach (var item in almostOutOfStockGasp)
            {
                Console.WriteLine(item);
            }

            //mrl
            Console.ReadLine();
        }
    }
}
