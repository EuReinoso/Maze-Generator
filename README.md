# Maze Generator

This repository aims to represent maze generation algorithms.

### Recursive Maze.

<img src= "https://github.com/EuReinoso/Maze-Generator/blob/master/assets/mazee20.gif" width= "360" height= "280">

Rules:

- Given a current cell as a parameter,
- Mark the current cell as visited
- While the current cell has any unvisited neighbour cells
    - Choose one of the unvisited neighbours
    - Remove the wall between the current cell and the chosen cell
    - Invoke the routine recursively for a chosen cell

### Learn More

- [Wiki](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- [Youtube](https://www.youtube.com/watch?v=p3mymCWzhV8&t=46s)

## Why?

Maze generation algorithms are widely used in games, but they are also a great way to improve programmimg skills in a fun way.

## How to use?

To run this program you will need to install the libraries Pygame and Numpy.

You can install these using `pip` on terminal:

- Pygame

        pip install pygame

- Numpy

        pip install numpy

### Tips

You can change the size of maze changing the variable `tile_size`

### Controls

After run the code, press key `Enter` to start the maze generation.

## Have Fun!

