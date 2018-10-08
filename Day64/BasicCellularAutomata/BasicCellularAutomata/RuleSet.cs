using System;
using System.Collections.Generic;
using System.Text;

namespace BasicCellularAutomata
{
    public abstract class RuleSet
    {
        protected int _maxX = 0;
        protected int _maxY = 0;
        protected int[,] _field;

        /// <summary>
        /// Instantiates the rule set with a copy of the field/grid and the x and y boundries
        /// </summary>
        /// <param name="field">int[][] game field</param>
        /// <param name="maxX">Max x boundry</param>
        /// <param name="maxY">Max Y boundry</param>
        public RuleSet(int[,] field, int maxX, int maxY)
        {
            _field = field;
            _maxX = maxX;
            _maxY = maxY;
        }

        /// <summary>
        /// Returns the number of neigbors for a cell at x,y.
        /// </summary>
        /// <param name="x">X coord of the cell to check</param>
        /// <param name="y">Y coord of the cell to check</param>
        /// <returns>Count of the neigbors</returns>
        protected int GetNumberOfNeigbors(int x, int y)
        {
            int neigbors = 0;

            //Logic to check all the cells around the current cell 
            //Right
            if (x + 1 < _maxX && _field[x + 1, y] == 1)
                neigbors++;

            //Left
            if (x - 1 >= 0 && _field[x - 1, y] == 1)
                neigbors++;

            //up
            if (y + 1 < _maxY && _field[x, y + 1] == 1)
                neigbors++;

            //Down
            if (y - 1 >= 0 && _field[x, y - 1] == 1)
                neigbors++;

            //Diagonal up Right
            if (x + 1 < _maxX && y + 1 < _maxY && _field[x + 1, y + 1] == 1)
                neigbors++;

            //Diagonal up Left
            if (x - 1 >= 0 && y + 1 < _maxY && _field[x - 1, y + 1] == 1)
                neigbors++;

            //Diagonal down left
            if (x - 1 >= 0 && y - 1 >= 0 && _field[x - 1, y - 1] == 1)
                neigbors++;

            //Diagonal down right
            if (x + 1 < _maxX && y - 1 >= 0 && _field[x + 1, y - 1] == 1)
                neigbors++;

            return neigbors;
        }

        /// <summary>
        /// Executes one generation of the game field, causing cells to live, die, or give birth.
        /// This is a template method, which calls the concreate method, TickAlgorithm() to execute the cell movement details
        /// </summary>
        public void Tick()
        {
            int[,] field2 = TickAlgorithm(); // Does something, then copies it to the field

            //Copy field = field2.
            Array.Copy(field2, _field, field2.Length); //source - dest - len
        }

        protected abstract int[,] TickAlgorithm();

    }
}
