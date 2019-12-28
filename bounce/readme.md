## Simple bouncing ball

First iteration of simulation:
- Ball under the influence of simplified gravity (g = 9.8m/s^2) without air resistance

Things I want to explore:
- Add simplified air resistance
- Add complex air resistance (quantized collisions with point particles)
- Track temperature and pressure changes around the ball as it moves

Things I want to fix:
- Why are graphics being cut off as the ball moves? (Trying to re-render too fast?)
- Maybe simulate everything and output to a file, then render off the file contents
