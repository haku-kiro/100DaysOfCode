using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using System;
using System.Collections.Generic;

/// <summary>
/// Particle tests
/// </summary>
namespace TexturesAndSpriteBatches
{

    public struct ParticleData
    {
        public float BirthTime;
        public float MaxAge;
        public Vector2 OriginalPosition;
        public Vector2 Accelaration;
        public Vector2 Direction;
        public Vector2 Position;
        public float Scaling;
        public Color ModColor;
    }

    public class Game2 : Game
    {
        GraphicsDeviceManager graphics;
        SpriteBatch spriteBatch;
        private Texture2D explosionTexture;

        private int width;
        private int height;

        List<ParticleData> particleList = new List<ParticleData>();

        public Game2()
        {
            graphics = new GraphicsDeviceManager(this);
            Content.RootDirectory = "Content";
        }

        protected override void Initialize()
        {

            width = graphics.GraphicsDevice.Viewport.Width;
            height = graphics.GraphicsDevice.Viewport.Height;

            base.Initialize();
        }

        protected override void LoadContent()
        {
            spriteBatch = new SpriteBatch(GraphicsDevice);
            explosionTexture = Content.Load<Texture2D>("explosion");
        }

        protected override void UnloadContent()
        {
        }

        protected override void Update(GameTime gameTime)
        {
            if (GamePad.GetState(PlayerIndex.One).Buttons.Back == ButtonState.Pressed || Keyboard.GetState().IsKeyDown(Keys.Escape))
                Exit();

            if (Keyboard.GetState(PlayerIndex.One).IsKeyDown(Keys.E))
            {
                //Add the explosions to the center of the screen
                AddExplosion(new Vector2(width / 2.0f, height / 2.0f), 5, 30.0f, 100000.0f, gameTime);
            }

            base.Update(gameTime);
        }

        protected override void Draw(GameTime gameTime)
        {
            GraphicsDevice.Clear(Color.White);

            spriteBatch.Begin();
            DrawExplosion(); // iterates over the list of particles, rendering them

            spriteBatch.End();

            base.Draw(gameTime);
        }

        //Add the explosion at the center of the screen
        private void AddExplosion(Vector2 explosionPos, int numberOfParticles, float size, float maxAge, GameTime gameTime)
        {
            for (int i = 0; i < numberOfParticles; i++)
            {
                AddExplosionParticle(explosionPos, size, maxAge, gameTime);
            }
        }

        private void AddExplosionParticle(Vector2 explosionPos, float size, float maxAge, GameTime gameTime)
        {
            ParticleData particle = new ParticleData();

            particle.OriginalPosition = explosionPos;
            particle.Position = particle.OriginalPosition;

            particle.BirthTime = (float)gameTime.TotalGameTime.TotalMilliseconds;
            particle.MaxAge = maxAge;
            particle.Scaling = .25f;
            particle.ModColor = Color.Red;


            Random rand = new Random(42);

            //Gen a random direction
            float particleDistance = (float)rand.NextDouble() * size;
            Vector2 displacement = new Vector2(particleDistance, 0);
            float angle = (float)rand.Next(360).ToRadians();
            displacement = Vector2.Transform(displacement, Matrix.CreateRotationZ(angle));

            particle.Direction = displacement;
            particle.Accelaration = 3.0f * particle.Direction;

            particleList.Add(particle);
        }

        private void DrawExplosion()
        {
            for (int i = 0; i < particleList.Count; i++)
            {
                ParticleData particle = particleList[i];
                spriteBatch.Draw(explosionTexture, particle.Position, null, particle.ModColor, i, new Vector2(256, 256), particle.Scaling, SpriteEffects.None, 1);
            }
        }
    }
}
