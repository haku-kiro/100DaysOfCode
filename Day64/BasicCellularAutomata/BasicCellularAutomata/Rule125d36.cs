using System;
using System.Collections.Generic;
using System.Text;

namespace BasicCellularAutomata
{

    public class Rule125d36 : RuleSet
    {
        public Rule125d36(int[,] field, int maxX, int maxY)
            : base(field, maxX, maxY)
        {
        }
        protected override int[,] TickAlgorithm()
        {
            int[,] field2 = new int[_maxX, _maxY];
            // 125/36
            // The first number(s) is what is required for a cell to continue.
            // The second number(s) is the requirement for birth.
            for (int y = 0; y < _maxY; y++)
            {
                for (int x = 0; x < _maxX; x++)
                {
                    int neighbors = GetNumberOfNeigbors(x, y);
                    if (neighbors == 3 || neighbors == 6)
                    {
                        // cell is born.
                        field2[x, y] = 1;
                        continue;
                    }
                    if (neighbors == 1 || neighbors == 2 || neighbors == 5)
                    {
                        // cell continues.
                        field2[x, y] = _field[x, y];
                        continue;
                    }
                    // cell dies.
                    field2[x, y] = 0;
                }
            }
            return field2;
        }
    }
}