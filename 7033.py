import math

line_1d = input().strip()
line_2d = input().strip()
line_3d = input().strip()

x1_1d, x2_1d = map(int, line_1d.split())
x1_2d, y1_2d, x2_2d, y2_2d = map(int, line_2d.split())
x1_3d, y1_3d, z1_3d, x2_3d, y2_3d, z2_3d = map(int, line_3d.split())

distance_1d = abs(x1_1d - x2_1d)
distance_2d = math.sqrt((x2_2d - x1_2d) ** 2 + (y2_2d - y1_2d) ** 2)
distance_3d = math.sqrt((x2_3d - x1_3d) ** 2 + (y2_3d - y1_3d) ** 2 + (z2_3d - z1_3d) ** 2)

print(f"{distance_1d:.3f}")
print(f"{distance_2d:.3f}")
print(f"{distance_3d:.3f}")
