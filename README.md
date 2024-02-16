# Gravity Simulator

## Introduction

As a physics student, I liked the idea of doing a gravity simulation and decided to begin this project as a way to learn by doing. I still have a lot to do in this project and still a lot to learn.

Feel free to give me comments or suggestions to improve my code.

## The program

The program, for now, uses Euler's method to describe the motions of the celestial bodies, but there is still no simulation yet, just a function to calculate the accuracy of my calculations after a set amount of steps.

Two examples of simulations
https://github.com/Mattia04/Gravity_Simulator/assets/47697461/17f82a85-eb6f-4b7b-be99-a5756c586d21



https://github.com/Mattia04/Gravity_Simulator/assets/47697461/0ec925f3-1fc1-4bd8-9f29-e40e70b35a45


Note:
Every physical unit is from the International System.

## Fugure_1.png

This figure shows the accuracy of the simulation given the parameters:

Delta time from one iteration to another:
```dt = 648000```

Number of iterations between two analyzed iterations
```interval = 25```

Number of analyzed iterations
```iters = 200000```

All the 9 Bodies contained in the file bodies.py

Which simulated over 100'000 years of the solar system

### Settings.json

The settings are quite simple (for now), you have to set the
delta time $dt$, which indicates the time from one step to the other.

### bodies.py

In this file are stored the solar system bodies (Sun, Mercury, Venus, Earth, Moon, Mars, Jupiter, Saturn, Uranus, Neptune) as single bodies and as a list and two functions to write a body easily.

There is also the possibility to add your own body with the parameters you wish.

### bodyclass.py

In this file, is defined the class Body, which is used to describe each Body in the file bodies.py.

### mycostants.py

In this file, are stored the constants to define bodies (such as mass, distance and velocity) and other constants (such as G). There is nothing else special about this file.

It needs to be updated with new and better data.

### vectors2D.py

In this file, is stored the class Vector2D, which describes a 2D vector and defines the operations you can do with vector such as addition, scalar multiplication, ecc..
