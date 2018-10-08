using System;
using System.Collections.Generic;
using System.Linq;

namespace BasicCellularAutomata
{
    class Program
    {

        private const char cellIcon = 'o';
        private const int maxX = 60;
        private const int maxY = 40;
        //This is the 'Grid' where the cells will live
        private static int[,] field = new int[maxX, maxY];


        /// <summary>
        /// Method to render our cells onto the screen
        /// </summary>
        private static void DrawField()
        {
            Console.CursorLeft = 0;
            Console.CursorTop = 0;

            for (int y = 0; y < maxY; y++)
            {
                for (int x = 0; x < maxX; x++)
                {
                    Console.Write(field[x, y] == 1 ? cellIcon : ' ');
                }
                Console.WriteLine();
            }
        }

        /// <summary>
        /// Method to setup the drawing area
        /// </summary>
        private static void Setup()
        {
            Console.SetWindowSize(maxX + 10, maxY + 10);
            Console.SetWindowPosition(0, 0);
            Console.Title = "Cellular Automata";
            Console.CursorVisible = false;

            //Define random positions for the cells
            Random r = new Random((int)DateTime.Now.Ticks); //Sets the seed based on the datetime ticks
            for (int x = 0; x < maxX; x++)
            {
                for (int y = 0; y < maxY; y++)
                {
                    field[x, y] = r.Next(0, 1 + 1);
                }
            }
        }

        public static int CountLife(int[,] grid, int lifeform = 1)
        {
            int count = 0;
            for (int x = 0; x < grid.GetLength(0); x++)
            {
                for (int y = 0; y < grid.GetLength(1); y++)
                {
                    if (grid[x, y] == lifeform)
                        count++;
                }
            }
            return count;
        }

        /// <summary>
        /// Takes a dict and writes a csv file
        /// </summary>
        /// <param name="data"></param>
        /// <param name="path"></param>
        public static void WriteDictToFile(Dictionary<int, int> data, string path)
        {
            //Saves a csv file
            string csv = string.Join(Environment.NewLine, data.Select(d => d.Key + "," + d.Value));

            System.IO.File.WriteAllText(path, csv);
        }

        static void Main(string[] args)
        {
            Setup();

            Dictionary<int, int> lifeCount = new Dictionary<int, int>();
            int DataSets = 10;

            for (int x = 1; x <= DataSets; x++)
            {
                //Instantiate the desired concrete RuleSet in this Strategy pattern
                RuleSet ruleSet = new ConwaysGameOfLife(field, maxX, maxY);

                //Play the game
                for (int i = 1; i <= 5000; i++)
                {
                    DrawField();

                    //Going to do some checks here
                    int life = CountLife(field);
                    Console.WriteLine($"\nAmount of life forms: {life}, iterations: {i}");

                    lifeCount.Add(i, life);

                    //Check if the amount of life has stabilized
                    if (i > 42)
                    {
                        //What are the chances of the same amount of life occuring 3 times in a row ? Seriously - how would you go about calculating this ? 
                        if (life == lifeCount.GetValueOrDefault(i - 40) && life == lifeCount.GetValueOrDefault(i - 39) && life == lifeCount.GetValueOrDefault(i - 38))
                            break;
                    }

                    ruleSet.Tick();
                }

                WriteDictToFile(lifeCount, $@"C:\Users\mdjco\Documents\datasets\gameOfLife{x}.csv");
                
                //Reset the count
                lifeCount = new Dictionary<int, int>();

                //Reset the Grid
                Setup();
            }

            //MRL
            Console.WriteLine("Done!");
            Console.ReadLine();
        }
    }
}
