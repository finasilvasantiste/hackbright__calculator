"""Math functions for calculator."""


def add(num1, num2):
    """Return the sum of the two inputs."""
    return (float(num1 + num2))


def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    return(float(num1 - num2))


def multiply(num1, num2):
    """Multiply the two inputs together."""
    return(float(num1 * num2))

def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    return(float(num1 / num2))

def square(num1):
    """Return the square of the input."""
    return float(num1 * num1)


def cube(num1):
    """Return the cube of the input."""
    return float(num1 * num1 * num1)


def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    return float(num1**num2)

def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    return float(num1 % num2)

def add_mult(num1, num2, num3):
    """Return the sum of the first two numbers times the third"""
    return float((num1 + num2) * num3)

def add_cubes(num1 , num2):
    """Cube both numbers and sum them """
    cube1 = cube(num1)
    cube2 = cube(num2)

    return add(cube1, cube2)