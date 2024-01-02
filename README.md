# Gravity Simulator

## Introduction
As a physics student I liked the idea of doing a gravity simulation and diced to begin this project as a way to learn-by-doing. I still have a lot to do in this project and still lot to learn.

Feel free to give me comments or suggestions to improve my code.

## The program
The program, for now, uses the Euler's method to describe the motions of the celestial bodies, but there is still no simulation yet, just a function to calculate the accuracy of my calculations after a set amount of steps.

Every physical unit is from the International System.

# Settings
The settings are quite simple (for now), you just have to set the
delta time dt, which indicates the time from a step to the other.

# bodies.py
In this file, are stored the solar system bodies (Sun, Mercury, Venus, Earth, Moon, Mars, Jupiter, Saturn, Uranus, Neptune) as single bodies and as a list and two function to write a body in an easy way.

There is also the possibility to add your own body with the parameters you wish.

# bodyclass.py
In this file, is defined the class Body, which is used to describe each Body in the file bodies.py.

# mycostants.py
In this file, are stored the constants to define bodies (such as mass, distance and velocity) and other constants (such as G). There is nothing else special about this file.

It needs to be updated with new and better data.

# vectors2D.py
In this file, is stored the class Vector2D, which describes a 2D vector and defines the operations you can do with vector such as addition, scalar multiplication, ecc..