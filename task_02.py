import turtle


def koch_curve(t, length, depth):
    if depth == 0:
        t.forward(length)
    else:
        # Each segment is divided into 3 parts
        new_length = length / 3
        koch_curve(t, new_length, depth - 1)
        t.left(60)
        koch_curve(t, new_length, depth - 1)
        t.right(120)
        koch_curve(t, new_length, depth - 1)
        t.left(60)
        koch_curve(t, new_length, depth - 1)


def draw_koch_snowflake(depth):
    screen = turtle.Screen()

    t = turtle.Turtle()
    t.speed(0)

    side_length = 300 # Set snowflake size 

    # Position to center
    t.penup()
    t.goto(-side_length / 2, side_length / 3)
    t.pendown()

    # Draw 3 sides of the snowflake
    for _ in range(3):
        koch_curve(t, side_length, depth)
        t.right(120)

    t.hideturtle()
    screen.mainloop()


if __name__ == "__main__":
    depth = int(input("Enter recursion level: "))
    draw_koch_snowflake(depth)