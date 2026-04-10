staty = [15, 180]
x = 10
y = 10
vel_x = 0
vel_y = 0
res_x = x
res_y = y
if staty[0] - x > 10:
    res_x += 10
elif staty[0] - x < -10:
    res_x -= 10
else:
    vel_x = staty[0] - x
    res_x += vel_x
if staty[1] - y > 10:
    res_y += 10
elif staty[1] - y < -10:
    res_y -= 10
else:
    vel_y = staty[1] - y
    res_y += vel_y


print(x, y, res_x, res_y)