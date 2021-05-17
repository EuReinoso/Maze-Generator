# Maze Generator

This repository aims to represent Maze generation algorithms.

## Algorithms :cyclone:

### [Recursive](https://github.com/EuReinoso/Maze-Generator/blob/master/scripts/algorithms/recursive.py)

<img src= "https://github.com/EuReinoso/Maze-Generator/blob/master/assets/recursive_medium.gif" width= "360" height= "280">

Rules:

1. Given a current cell as a parameter.
2. Mark the current cell as visited.
3. While the current cell has any unvisited neighbour cells.
    1. Choose one of the unvisited neighbours.
    2. Remove the wall between the current cell and the chosen cell.
    3. Invoke the routine recursively for a chosen cell.

### [Kruskal](https://github.com/EuReinoso/Maze-Generator/blob/master/scripts/algorithms/kruskal.py)

<img src= "https://github.com/EuReinoso/Maze-Generator/blob/master/assets/kruskal_medium.gif" width= "360" height= "280">

1. Create a list of all walls, and create a set for each cell, each containing just that one cell.
2. For each wall, in some random order.
    1. If the cells divided by this wall belong to distinct sets:
    2. Remove the current wall.
    3. Join the sets of the formerly divided cells.

### [Binary](https://github.com/EuReinoso/Maze-Generator/blob/master/scripts/algorithms/binary.py)

<img src= "https://github.com/EuReinoso/Maze-Generator/blob/master/assets/binaty_medium.gif" width= "360" height= "280">

1. For each cell, randomly remove the left or top wall.

### [Prim](https://github.com/EuReinoso/Maze-Generator/blob/master/scripts/algorithms/prim.py)

<img src= "https://github.com/EuReinoso/Maze-Generator/blob/master/assets/prim_medium.gif" width= "360" height= "280">

1. Start with a grid full of walls.
2. Pick a cell, mark it as part of the maze. Add the walls of the cell to the wall list.
3. While there are walls in the list:
    1. Pick a random wall from the list. If only one of the two cells that the wall divides is visited, then:
        1. Make the wall a passage and mark the unvisited cell as part of the maze.
        1. Add the neighboring walls of the cell to the wall list.
    2. Remove the wall from the list.

### Learn More

- [Wiki](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- [Youtube](https://www.youtube.com/watch?v=p3mymCWzhV8&t=46s)

## Why? :bulb:

Maze generation algorithms are widely used in games, but they are also a great way to improve programmimg skills in a fun way.

## How to use? :page_with_curl:

To run this program you will need Python and to install the libraries Pygame and Numpy.

You can install these using `pip` on terminal:

- Pygame

        pip install pygame

- Numpy

        pip install numpy

(If pip didn't work try `pip3`)

After running the program, select the type of algorithm, the size of the maze and click on `Generate!`.

### Play :soccer:

After the maze has been generated, you can click on `PLAY` to start. Try to get to the black dot in shortest time possible!

<img src= "https://github.com/EuReinoso/Maze-Generator/blob/master/assets/play.gif" width= "360" height= "280">

## Contact :telephone_receiver:

Bugs? Ideas? Questions? 
Contact-me: lucas.reinoso.br@gmail.com

## Have Fun!
