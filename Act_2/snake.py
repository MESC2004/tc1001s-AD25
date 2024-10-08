"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to mouse clicks.
"""

from random import choice, randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

# List of 5 different colors excluding red
colors = ['blue', 'green', 'yellow', 'purple', 'orange']

# Select random colors for the snake and food ensuring they are different
snake_color = choice(colors)
food_color = choice([color for color in colors if color != snake_color])

# Dentro de la función 'move', dibujar la serpiente y la comida con los colores seleccionados
# Draw snake with random color
for body in snake:
    square(body.x, body.y, 9, snake_color)  # <--- SE ASIGNA EL COLOR ALEATORIO DE LA SERPIENTE

# Draw food with random color
square(food.x, food.y, 9, food_color)  # <--- SE ASIGNA EL COLOR ALEATORIO DE LA COMIDA

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y


def inside(head):
    """Return True if head inside boundaries."""
    return -200 < head.x < 190 and -200 < head.y < 190

def move_food():
    """Move food randomly by one step and keep it inside boundaries."""
    directions = [vector(10, 0), vector(-10, 0), vector(0, 10), vector(0, -10)]
    move = choice(directions)
    
    new_food_pos = food + move

    if inside(new_food_pos):
        food.move(move)

def move():
    """Move snake forward one segment."""
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

     # Move food randomly
    move_food()  # <--- SE AGREGÓ ESTA LÍNEA PARA MOVER LA COMIDA

    for body in snake:
        square(body.x, body.y, 9, snake_color)

    square(food.x, food.y, 9, food_color)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
