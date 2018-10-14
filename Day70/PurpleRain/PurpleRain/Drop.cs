using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;

namespace PurpleRain
{
    class Drop
    {
        //Props
        Texture2D drop;

        float TargetWidth; //this will be the pixel width of the drop
        float TargetHeight;
        public Vector2 scale; // will be the x,y value of the width height

        Vector2 pos;

        Vector2 dropVelocity = new Vector2(0, .25f);

        int width;
        int height;

        public Texture2D[] drops;

        /// <summary>
        /// Refactor
        /// </summary>
        /// <param name="dropSprite"></param>
        /// <param name="dropCount"></param>
        /// <param name="size"></param>
        public Drop(Texture2D dropSprite, int dropCount, float size = 30)
        {
            drops = new Texture2D[dropCount];
            TargetWidth = size;

            drop = dropSprite;

            //Set the width/scale // should be able to set the width
            scale = new Vector2(TargetWidth / (float)drop.Width, TargetWidth / (float)drop.Width);
            TargetHeight = drop.Height * scale.Y;

            
            //Hardcoding the purple color ... bad mike

            //Set the color
            Color[] color = new Color[drop.Width * drop.Height]; 
            for (int i = 0; i < color.Length; i++)
                color[i] = new Color(138, 43, 226);



            for (var x = 0; x < drops.Length; x++)
            {
                //Init the drops randomly
                drops[x] = drop;
                drops[x].SetData<Color>(color);
            }
        }

    }
}
