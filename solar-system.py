import turtle
from math import *

SCEEN_TRACER_SPEED = 50
sun = turtle.Turtle()
sun.shape('circle')
sun.color('yellow')
sun.shapesize(3)


def sceen_setup():
    screen = turtle.Screen()
    screen.tracer(SCEEN_TRACER_SPEED)
    return screen

class Planet(turtle.Turtle):
    def __init__(self,name,radius, color, angular_speed, size): #initialize function
        super().__init__(shape='circle')
        self.name = name
        self.radius = radius
        self.c = color
        self.color(self.c)
        self.up()
        self.pd()
        self.angle = 0
        self.angular_speed = angular_speed
        self.shapesize(size)

    def move(self):
        x = self.radius*cos(self.angle)
        y = self.radius*sin(self.angle)
        self.goto(sun.xcor() + x,sun.ycor() + y)
        self.angle += self.angular_speed

def create_planets():
    return [
        Planet("Mercury", 60, 'grey', 0.05, 0.5),
        Planet("Venus", 110, 'orange', 0.03, 1),
        Planet("Earth", 160,'blue', 0.01, 1.2),
        Planet("Mars", 210, 'red', 0.007, 0.8),
        Planet("Jupiter", 270, 'brown', 0.02, 2),
        Planet("Saturn", 340, 'pink', 0.018, 1.8),
        Planet("Uranus", 410, 'light blue', 0.016, 1.5),
        Planet("Neptune", 470, 'black', 0.005, 1.4),
        Planet("Pluto", 530, 'dark grey', 0.003, 0.6)
        ]

def main():
    screen = sceen_setup()

    planets = create_planets()

    while True:
        screen.update()
        for planet in planets:
            planet.move()

if __name__ == "__main__":
    main()