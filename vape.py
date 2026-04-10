import arcade
import random
import time 
import math

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "игра с random steperam"

 
class StepGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        self.to_clear = False
        self.timer = 0.0
        self.draw_line_flag = False
        self.x_start = 0
        self.y_start = 0
        self.staty = [0,0]
        self.plate_x = []
        self.plate_y = []
        # 0,0 - 600,600            
        for i in range(0,610,30):
            self.plate_x.append(i)
        for i in range(0,610,30):
            self.plate_y.append(i)


    def on_mouse_press(self, x, y, button, modifiers):
        """оброботка мыши"""
        print("x:", x," y:", y)
        print(self.staty)
        #print(self.plate_x)
        #print(self.plate_y)
        self.x_start = x
        self.y_start = y

        self.staty = [self.x_start, self.y_start]
    
    def on_mouse_motion(self, x, y, dx, dy):
        """постояная оброботка мыши"""
        #print("x:", x," y:", y)
        #print(self.staty)
        #print(self.plate_x)
        #print(self.plate_y)
        self.x_start = x
        self.y_start = y

        self.staty = [self.x_start, self.y_start]

    def on_key_press(self, key, modifiers):
        if key == arcade.key.C:
            self.to_clear = True

    def update(self):
        self.timer += 1

        if 1 < self.timer:
            self.draw_line_flag = True
            self.timer = 0

    def create_vector(self, x, y):
        res_x = 0
        res_y = 0

        dx_1 = x - self.staty[0]
        dy_1 = y - self.staty[1]
        dx_2 = x - 300
        dy_2 = y - 300



        angle_1 = math.atan2(dy_1, dx_1)
        angle_2 = math.atan2(dy_2, dx_2)
        res_x = x - math.cos(angle_1+angle_2) * 15
        res_y = y - math.sin(angle_1+angle_2) * 15
        arcade.draw_line(x, y, res_x, res_y, arcade.color.BLUE, 1)

        #print(res_x, res_y)


        dx = x - res_x
        dy = y - res_y
        angle = math.atan2(dy, dx)
        arrow_size = 3
        offset = 10
        x3 = res_x - math.cos(angle - offset) * arrow_size
        y3 = res_y - math.sin(angle - offset) * arrow_size
        x4 = res_x - math.cos(angle + offset) * arrow_size
        y4 = res_y - math.sin(angle + offset) * arrow_size
        arcade.draw_line(res_x, res_y, x3, y3, arcade.color.BLUE, 1)
        arcade.draw_line(res_x, res_y, x4, y4, arcade.color.BLUE, 1)



    def on_draw(self):

        self.update()



        self.clear()


        for i in self.plate_x:
            for h in self.plate_y:
                self.create_vector(i,h)
            
        


        #self.clear()



        if self.draw_line_flag == True:
            


            self.draw_line_flag = False





def main():
    game = StepGame()
    arcade.run()

if __name__ == "__main__":
    main()
