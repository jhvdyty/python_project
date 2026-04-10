import arcade
import random
import time 

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
        self.staty = []

    def on_mouse_press(self, x, y, button, modifiers):
        """оброботка мыши"""
        print("x:", x," y:", y)
        print(self.staty)
        self.x_start = x
        self.y_start = y
        self.staty = [self.x_start, self.y_start]

    def on_key_press(self, key, modifiers):
        if key == arcade.key.C:
            self.to_clear = True

    def update(self):
        self.timer += 0.1

        if 10 < self.timer:
            self.draw_line_flag = True
            self.timer = 0


    def on_draw(self):

        self.update()


        x2 = random.uniform(self.x_start - 100, self.x_start + 100 ) 
        y2 = random.uniform(self.y_start - 100, self.y_start + 100 ) 


        self.clear()



        if self.draw_line_flag == True:
            arcade.draw_line(self.x_start, self.y_start, x2, y2, arcade.color.BLUE, 3)
            self.staty.append(x2)
            self.staty.append(y2)
            self.x_start = x2
            self.y_start = y2

            self.draw_line_flag = False
        arcade.draw_line(self.x_start, self.y_start, x2, y2, arcade.color.BLUE, 3)

        #for i in range(0,len(self.staty),2):
        #    for h in range(1,len(self.staty),2):
        #        for i2 in range(2,len(self.staty),2):
        #            for h2 in range(3,len(self.staty),2):
        #                arcade.draw_line(self.staty[i], self.staty[h], self.staty[i2], self.staty[h2], arcade.color.BLUE, 3)




def main():
    game = StepGame()
    arcade.run()

if __name__ == "__main__":
    main()
