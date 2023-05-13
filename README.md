
# 3D Ray Casting Engine

Ray casting is the methodological basis for 3D CAD/CAM solid modeling and image rendering. It is essentially the same as ray tracing for computer graphics where virtual light rays are "cast" or "traced" on their path from the focal point of a camera through each pixel in the camera sensor to determine what is visible along the ray in the 3D scene.
In early first person games, raycasting was used to efficiently render a 3D world from a 2D playing field using a simple one-dimensional scan over the horizontal width of the screen. The video game Wolfenstein 3D was built from a square based grid of uniform height walls meeting solid-colored floors and ceilings. In order to draw the world, a single ray was traced for every column of screen pixels and a vertical slice of wall texture was selected and scaled according to where in the world the ray hits a wall and how far it travels before doing so.

# Controls

- W - Move forwards
- S - Move backwards
- A - Move left
- D - Move right
- Up Arrow - Look up
- Down Arrow - Look down
- Left Arrow - Rotate to left
- Right Arrow - Rotate to right

# Index

1. Working
2. Digital Differential Analyzer (DDA)
3. Class files

# Working

A 2d grid map is created where each block is either empty space to walk through or a wall that cannot be passed through. A point, i.e. the player will move through this 2d map. The program checks every step of the player and if the player is stepping on a wall block the movements are restricted.
For generating a 3d view, a fixed field of view is set along with a fixed draw distance to minimize processing. Within the defined field of view, a number or rays are drawn from the player position to the maximun draw distance. If the ray touches a block containing the wall, its distance is recorded. Using this recorded distance, the height of the wall block is determined and drawn.
The traditional way to check for ray collision would be check for the block type at each unit length for the casted ray. However, this method can be very heavy and can result in very low frames per second. An efficient way to perform these checks is to use the Digital Differential Analyzer (DDA) algorithm. This algorithm checks for ray interception only at block intersections. This can reduce the check drastically. A detailed explanation can be found in the next section.
If a wall collision is detected by the ray, we construct a rectangle whose height is inversely proportional to the ray length and the width is equivalent to the display width / number of rays. The walls generated presents the user with a psudo 3d environment to explore.

# Digital Differential Analyzer (DDA)

In computer graphics, a digital differential analyzer (DDA) is hardware or software used for interpolation of variables over an interval between start and end point. DDAs are used for rasterization of lines, triangles and polygons. They can be extended to non linear functions, such as perspective correct texture mapping, quadratic curves, and traversing voxels.
In the following Engine, ray collision with wall is determined using the DDA algorith for efficiency. This drastically cuts down the number of checks made which in turn presents us with better performance.
For a detailed explanation on how the algorithm is utilized please check out the following video


[![Super Fast Ray Casting in Tiled Worlds using DDA](http://img.youtube.com/vi/NbSee-XM7WA/0.jpg)](https://youtu.be/NbSee-XM7WA)

# Class files

1. main.py - This is the starting point of the project and it is responsible for importing all the other required classes and creating the pygame windows for drawing the graphics.
2. settings.py - This class is just used to define parameters to be used by the game engine like window resolution, asset location, and render method, etc.
3. map.py - This imports the map json file and segregates the data in it into different variables.
4. player.py - This class is responsible for dealing with the movement of the player. It modifies the player position based on the key pressed and restricts movement if collision with wall is detected.
5. ray_caster.py - This class is used to calculate the ray lenghts for each vertical pixel column. It uses the player position from the player class and draws a number of rays within the field of view set in the settings and checks for wall collision. In the updated variable height block update, the ray_caster does not stop when it detects a wall. It continues till the max draw distance and records all the wall collision detected in the path.
6. texture_renderer.py - As the name suggests, this class is responsible for drawing the scene with textures. With the data obtained from the ray_caster class it draws the wall column by slicing the texture into thin vertical columns equivalent to the width of the scanned vertical pixel columns.
