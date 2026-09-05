# Implement an algorithm for calculating an approximation 
# for the value of pi (π).
import random

n_points = int(input("How many random points to generate? "))

inside_circle = 0

for _ in range(n_points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        inside_circle += 1

pi_approx = 4 * inside_circle / n_points
print(f"Approximation of pi: {pi_approx}")