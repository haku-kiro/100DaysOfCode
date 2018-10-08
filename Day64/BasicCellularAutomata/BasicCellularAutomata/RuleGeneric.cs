using System;
using System.Collections.Generic;
using System.Text;

namespace BasicCellularAutomata
{
    class RuleGeneric : RuleSet
    {

        private int _a; // Cell to continue
        private int _b; // Cell to give birth


        public RuleGeneric(int[,] field, int maxX, int maxY, int a, int b) 
            : base(field, maxX, maxY)
        {
            _a = a;
            _b = b;
        }


        /// <summary>
        /// Converts a number to an list of digits, 123 becomes 1,2,3
        /// </summary>
        /// <param name="Digits">The number, such as 123</param>
        /// <returns>List of numbers 1,2,3</returns>
        protected List<int> ToDigitArray(int Digits)
        {
            List<int> result = new List<int>();

            string digitString = Digits.ToString();
            foreach (char digit in digitString)
            {
                result.Add(Convert.ToInt32(digit.ToString()));
            }

            return result;
        }

        
        protected override int[,] TickAlgorithm()
        {

            int[,] field2 = new int[_maxX, _maxY];

            for (int y = 0; y <= _maxY; y++)
            {
                for (int x = 0; x <= _maxX; x++)
                {
                    bool processed = false;
                    int neighbors = GetNumberOfNeigbors(x, y);

                    List<int> birthDigits = ToDigitArray(_b);

                    foreach (int digit in birthDigits)
                    {
                        if (neighbors == digit)
                        {
                            //Cell is born
                            field2[x, y] = 1;
                            processed = true;
                            break;
                        }
                    }

                    if (processed)
                        continue;

                    List<int> liveDigits = ToDigitArray(_a);

                    foreach (int digit in liveDigits)
                    {
                        if (neighbors == digit)
                        {
                            //Cell continues
                            field2[x, y] = _field[x, y];
                            processed = true;
                            break;  
                        }
                    }

                    if (processed)
                        continue;

                    //cell dies
                    field2[x, y] = 0;
                }
            }


            return field2;
        }
    }
}
