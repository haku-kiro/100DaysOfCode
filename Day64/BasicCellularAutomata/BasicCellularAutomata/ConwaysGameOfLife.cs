using System;
using System.Collections.Generic;
using System.Text;

namespace BasicCellularAutomata
{
    public class ConwaysGameOfLife : RuleSet
    {
        //Ctor logic handled in the abstract class
        public ConwaysGameOfLife(int[,] field, int maxX, int maxY) 
            : base(field, maxX, maxY)
        {
        }
        

        /// <summary>
        /// Tick algorithm for Conways game of life
        /// 23/3 - Conways game of life
        /// 
        /// The first number(s) is what is required for a cell to continue.
        /// The second number(s) is the requirement for birth
        /// </summary>
        /// <returns></returns>
        protected override int[,] TickAlgorithm()
        {

            int[,] field2 = new int[_maxX, _maxY];

            for (int y = 0; y < _maxY; y++)
            {
                for (int x = 0; x < _maxX; x++)
                {
                    int neighbors = GetNumberOfNeigbors(x, y);
                    if (neighbors == 3)
                    {
                        //A cell is born
                        field2[x, y] = 1;
                        continue;
                    }

                    if (neighbors == 2 || neighbors == 3)
                    {
                        //Cell continues
                        field2[x, y] = _field[x, y];
                        continue;
                    }

                    //Cell dies
                    field2[x, y] = 0;
                }
            }

            return field2;
        }
    }
}
