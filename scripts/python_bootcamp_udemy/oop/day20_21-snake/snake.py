from turtle import Turtle
import numpy as np
MOVE_DISTANCE = 20
STARTING_POSITION = [(0,0), (-20,0), (-40,0)]

class Snake():
    "Class that represents the snake in the Snake Game."
    def __init__(self, shape="square", color="white"):
        self.shape = shape
        self.color = color
        
        self.segments = None
        self.initialize_segments()
        
    def initialize_segments(self):
        """Initialize the three first segments of the snake at a fixed position."""
        snake_segment = []

        for start_pos in STARTING_POSITION:
            new_segment = Turtle()
            new_segment.penup()
            new_segment.shape(self.shape)
            new_segment.color(self.color)
            new_segment.goto(start_pos)
            snake_segment.append(new_segment)
            
        self.segments = snake_segment
        
    def move(self):
        """Move the snake in the direction is already heading"""
        for idx in reversed(range(1, len(self.segments))):
            newx, newy = self.segments[idx-1].pos()
            self.segments[idx].goto(newx, newy)
        self.segments[0].forward(MOVE_DISTANCE)

    def _random_direction_change(self, p):
        """Randomly changes the direction the snake is heading to"""
        if np.random.rand() < p:
            self.segments[0].setheading(np.random.choice([0,90,180,270]))
            
    def up(self):
        self.segments[0].setheading(90)
        
    def down(self):
        self.segments[0].setheading(270)
    
    def right(self):
        self.segments[0].setheading(0)
        
    def left(self):
        self.segments[0].setheading(180)
