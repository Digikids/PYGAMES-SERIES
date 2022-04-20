import random

size = [700, 600]
snow_list = []
for i in range(50):
    x = random.randrange(0, size[0])
    y = random.randrange(0, size[1])
    snow_list.append([x, y])

print(len(snow_list))