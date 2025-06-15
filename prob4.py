import math

def circle_stats(radius):
    area = math.pi * radius ** 2
    circum_ference= 2 *math.pi * radius
    return area,circum_ference


a,c = circle_stats(3)
print(f'{a:.2f} Area', f"{c:.2f} circumference ")