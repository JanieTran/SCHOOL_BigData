# --------------------------------------------------------------------------
# EXERCISE 1: Write a Python function that takes in 3 integers (X,Y and Z)
# and checks whether a triangle with lengths X,Y and Z is equilateral,
# isosceles or scalene, or that no triangle can be formed.
#
# Note, one can assume that X≤Y≤Z. For example, when X=3, Y=4 and Z=4
# the code should print “A triangle of sides X=3, Y=4 and Z=4 is isosceles"
# --------------------------------------------------------------------------


def check_triangle(x, y, z):
    # All positive lengths
    if x < 1 or y < 1 or z < 1:
        return 'Length must be positive'

    message = 'A triangle of sides X={}, Y={} and Z={} is {}'

    # Equilateral
    if x == y and x == z:
        return message.format(x, y, z, 'equilateral')

    # Isoscele
    if x == y or x == z or y == z:
        return message.format(x, y, z, 'isosceles')

    # Scalene
    if x + y > z and x + z > y and y + z > x:
        return message.format(x, y, z, 'scalene')

    # Not a triangle
    return message.format(x, y, z, 'not a triangle')


print(check_triangle(3, 4, 4))
print(check_triangle(3, 4, 5))
print(check_triangle(3, 4, 1))
print(check_triangle(1, 1, 1))
print(check_triangle(-3, 4, 4))
