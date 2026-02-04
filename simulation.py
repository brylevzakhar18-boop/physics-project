import math

speed = 20
angle = 45

angle_rad = math.radians(angle)

vx = speed * math.cos(angle_rad)
vy = speed * math.sin(angle_rad)

print("Horizontal speed:", round(vx, 2))
print("Vertical speed:", round(vy, 2))
