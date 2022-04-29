

# Game-of-Life
Here I explore several implementations of Conway's Game Of Life and compare their efficiency.

I draw on ideas from graph theory and convolution theory. The functions are flexible enough to
be imported and used for other applications.

The repository contains two implementations, one in python and another in cpp, as well as a jupyter notebook explaining some of the concepts.

### python:

The python script produces an animation by running the following command in the local directory:


```console
python game_of_life.py -i pento -d 128 -s 10000

```
The flag -i sets up the initial condition from a dictionary. You can for now choose from [pento , peri15 , floater]. -d sets the dimensions of the field and -s the number of steps to run for. The settings chosen are also the default ones.

### c++

The cpp implementation is far more efficient. The code uses print statements to produce an animation directly in the bash shell.

To compile the cpp script run this in the directory:

```console
g++ Game_of_Life.cpp -o gol
```

run with:

```console
./gol

```



