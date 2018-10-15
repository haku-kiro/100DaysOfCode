using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TexturesAndSpriteBatches
{
    public static class Helpers
    {
        public static double ToRadians(this int val)
        {
            return (Math.PI / 180) * val;
        }
    }
}
