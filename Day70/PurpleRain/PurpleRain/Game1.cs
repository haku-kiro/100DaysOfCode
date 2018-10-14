using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using System;

namespace PurpleRain
{
    /// <summary>
    /// This is the main type for your game.
    /// </summary>
    public class Game1 : Game
    {

        //Colors 
        // (138, 43, 226) //Rain
        // (230, 230, 250) // Background

        GraphicsDeviceManager graphics;
        SpriteBatch spriteBatch;


        Texture2D drop;
        Vector2 dropVelocity = new Vector2(0, .25f);
        Vector2 pos = new Vector2(0, 0);


        float TargetWidth = 30; //this will be the pixel width of the drop
        float TargetHeight;
        Vector2 scale; // will be the x,y value of the width height


        int width;
        int height;


        Drop drops;

        public Game1()
        {
            graphics = new GraphicsDeviceManager(this);
            Content.RootDirectory = "Content";
        }

        /// <summary>
        /// Allows the game to perform any initialization it needs to before starting to run.
        /// This is where it can query for any required services and load any non-graphic
        /// related content.  Calling base.Initialize will enumerate through any components
        /// and initialize them as well.
        /// </summary>
        protected override void Initialize()
        {

            graphics.PreferredBackBufferHeight = 360;
            graphics.PreferredBackBufferWidth = 640;
            graphics.ApplyChanges();

            // TODO: Add your initialization logic here

            width = graphics.GraphicsDevice.Viewport.Width;
            height = graphics.GraphicsDevice.Viewport.Height;

            base.Initialize();
        }

        /// <summary>
        /// LoadContent will be called once per game and is the place to load
        /// all of your content.
        /// </summary>
        protected override void LoadContent()
        {
            // Create a new SpriteBatch, which can be used to draw textures.
            spriteBatch = new SpriteBatch(GraphicsDevice);

            // TODO: use this.Content to load your game content here
            drop = this.Content.Load<Texture2D>("raindrop");

            //Creates 10 Drops with color purple
            drops = new Drop(drop, 10);
            

            scale = new Vector2(TargetWidth / (float)drop.Width, TargetWidth / (float)drop.Width);
            TargetHeight = drop.Height * scale.Y;

            //Repaints the whole drop (Should just open in photo shop and paint purple...)
            Color[] color = new Color[drop.Width * drop.Height];
            for (var x = 0; x < color.Length; x++)
            {
                color[x] = new Color(138, 43, 226);
            }

            drop.SetData<Color>(color);

        }

        /// <summary>
        /// UnloadContent will be called once per game and is the place to unload
        /// game-specific content.
        /// </summary>
        protected override void UnloadContent()
        {
            // TODO: Unload any non ContentManager content here
        }

        /// <summary>
        /// Allows the game to run logic such as updating the world,
        /// checking for collisions, gathering input, and playing audio.
        /// </summary>
        /// <param name="gameTime">Provides a snapshot of timing values.</param>
        protected override void Update(GameTime gameTime)
        {
            if (GamePad.GetState(PlayerIndex.One).Buttons.Back == ButtonState.Pressed || Keyboard.GetState().IsKeyDown(Keys.Escape))
                Exit();

            // TODO: Add your update logic here
            pos += dropVelocity * (float)gameTime.ElapsedGameTime.TotalMilliseconds;


            base.Update(gameTime);
        }

        /// <summary>
        /// This is called when the game should draw itself.
        /// </summary>
        /// <param name="gameTime">Provides a snapshot of timing values.</param>
        protected override void Draw(GameTime gameTime)
        {
            //Rain color : new Color(138, 43, 226)


            GraphicsDevice.Clear(new Color(230, 230, 250));

            // TODO: Add your drawing code here

            spriteBatch.Begin();

            foreach (Texture2D drop in drops.drops)
            {
                int xVal = RandomX(width);
                pos.X = xVal;

                spriteBatch.Draw(drop, position: pos, scale: drops.scale);
            }

            
            spriteBatch.Draw(drop, position: pos,scale:scale);
            spriteBatch.End();

            base.Draw(gameTime);
        }

        public static int RandomX(int end)
        {
            Random ran = new Random();
            return ran.Next(0, end);
        }
    }
}
