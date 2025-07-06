import math

def area_of_equilateral_triangle(side):
    return (math.sqrt(3) / 4) * side * side

def area_of_isosceles_triangle(base, height):
    return 0.5 * base * height

def area_of_scalene_triangle(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def area_of_triangle_base_height(base, height):
    return 0.5 * base * height

def area_of_trapezium(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def area_of_rectangle(length, width):
    return length * width

def area_of_sphere(radius):
    return 4 * math.pi * radius * radius

def volume_of_cuboid(length, width, height):
    return length * width * height
