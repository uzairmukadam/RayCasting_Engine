
# 3D Ray Casting Engine

Ray casting is the methodological basis for 3D CAD/CAM solid modeling and image rendering. It is essentially the same as ray tracing for computer graphics where virtual light rays are "cast" or "traced" on their path from the focal point of a camera through each pixel in the camera sensor to determine what is visible along the ray in the 3D scene.
In early first person games, raycasting was used to efficiently render a 3D world from a 2D playing field using a simple one-dimensional scan over the horizontal width of the screen. The video game Wolfenstein 3D was built from a square based grid of uniform height walls meeting solid-colored floors and ceilings. In order to draw the world, a single ray was traced for every column of screen pixels and a vertical slice of wall texture was selected and scaled according to where in the world the ray hits a wall and how far it travels before doing so.

# Index

1. [Working](https://github.com/uzairmukadam/RayCasting_Engine/new/master?readme=1#working)
2. [Digital Differential Analyzer (DDA)](https://github.com/uzairmukadam/RayCasting_Engine/new/master?readme=1#digital-differential-analyzer-dda)
3. [To-do tasks](https://github.com/uzairmukadam/RayCasting_Engine/new/master?readme=1#to-do-tasks)
4. [Usage](https://github.com/uzairmukadam/RayCasting_Engine/new/master?readme=1#usage)

# Working

A 2d grid map is created where each block is either empty space to walk through or a wall that cannot be passed through. A point, i.e. the player will move through this map. The program checks every step of the player and if the player is stepping on a wall block the movements are restricted or stopped. For generating a 3d view, a fixed field of view is set along with a fixed draw distance. Within the defined field of view, a number or rays are drawn from the player position to the maximun draw distance in an angle. If the ray meets a block containing the wall, it is stopped there.
The traditional way to check for ray collision would be check for the block type at each unit length for the casted ray. However, this method can be very heavy and can result in low frames per second. An efficient way to perform these checks is to use the Digital Differential Analyzer (DDA) algorithm. This algorith checks ray interception only at block intersections. This can reduce the check drastically.
If a wall collision is detected by the ray, we construct a rectangle whose height is inversely proportional to the ray length and the width is equivalent to the display width / number of rays. The walls generated presents the user with a psudo 3d environment to explore.

# Digital Differential Analyzer (DDA)

In computer graphics, a digital differential analyzer (DDA) is hardware or software used for interpolation of variables over an interval between start and end point. DDAs are used for rasterization of lines, triangles and polygons. They can be extended to non linear functions, such as perspective correct texture mapping, quadratic curves, and traversing voxels.
In the following Engine, ray collision with wall is determined using the DDA algorith for efficiency. This drastically cuts down the number of checks made which in turn presents us with better performance.
For a detailed explanation on how the algorithm is utilized please check out the following video


[![Super Fast Ray Casting in Tiled Worlds using DDA](http://img.youtube.com/vi/NbSee-XM7WA/0.jpg)](https://youtu.be/NbSee-XM7WA)

# To-do Tasks

1. Apply textures to wall.
2. Floor and roof casting.
3. Addition of sprite objects.
4. Optimization.

# Usage

1. Clone the project.
2. In the map.py file modify the game map list.
3. From settings.py modify parameters as per you liking.
4. Run main.py.
