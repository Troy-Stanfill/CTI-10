# Troy Stanfill
# 9/24/26
# P2 Lab1
# using math libary to calculate circle features

import math

# get radious from user as a float

Radius = float(input("What is the radius of the circle as a float? "))

# Calculate Diameter

Diameter = 2 * Radius

# Display diametor as a f-string
print(f"The Diametor of the circle is {Diameter:.1f}")

# Calculate the Circumference
circumference = 2 * math.pi * Radius

# Display the circumference as a f-string
print(f"The circumfrence of the circle is {circumference:.2f}")

# Calculate the area

area = math.pi * Radius ** 2

# Display the area of the circle

print(f"The area of the circle is {area:.3f}")