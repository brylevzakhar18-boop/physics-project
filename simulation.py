import math

g = 9.81
v0 = 20
angle_deg = 45
dt = 0.05

angle = math.radians(angle_deg)

t = 0.0
x = 0.0
y = 0.0

vx = v0 * math.cos(angle)
vy = v0 * math.sin(angle)

print("t\t x\t y")

while y >= 0:
    print(f"{t:.2f}\t{x:.2f}\t{y:.2f}")
    t += dt
    x += vx * dt
    y += vy * dt
    vy -= g * dt
