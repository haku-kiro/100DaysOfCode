using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using System;
using System.Collections.Generic;

namespace RealPurpleRain
{
    /// <summary>
    /// This is the main type for your game.
    /// </summary>
    public class PurpleRain : Game
    {
        GraphicsDeviceManager graphics;
        SpriteBatch spriteBatch;

        ParticleEngine particleEngine;
        Random rand;

        private int width;
        private int height;

        public PurpleRain()
        {
            graphics = new GraphicsDeviceManager(this);
            Content.RootDirectory = "Content";
        }

        protected override void Initialize()
        {
            graphics.PreferredBackBufferWidth = 1280;
            graphics.PreferredBackBufferHeight = 720;
            graphics.ApplyChanges();

            Window.Title = "Purple Rain";

            width = graphics.GraphicsDevice.Viewport.Width;
            height = graphics.GraphicsDevice.Viewport.Height;
            rand = new Random(42);

            base.Initialize();
        }

        protected override void LoadContent()
        {
            spriteBatch = new SpriteBatch(GraphicsDevice);

            //Load our rain drops
            List<Texture2D> textures = new List<Texture2D>();
            textures.Add(Content.Load<Texture2D>("dropTest")); // Change to test



            particleEngine = new ParticleEngine(textures, new Vector2(400, 240));

            //Change the rain color : (138, 43, 226)

        }

        protected override void UnloadContent()
        {
        }

        protected override void Update(GameTime gameTime)
        {
            if (GamePad.GetState(PlayerIndex.One).Buttons.Back == ButtonState.Pressed || Keyboard.GetState().IsKeyDown(Keys.Escape))
                Exit();


            particleEngine.EmitterLocation = new Vector2(rand.Next(0, width), -100);
            particleEngine.Update();


            base.Update(gameTime);
        }

        protected override void Draw(GameTime gameTime)
        {
            GraphicsDevice.Clear(new Color(230, 230, 250));

            particleEngine.Draw(spriteBatch);

            base.Draw(gameTime);
        }
    }
}
