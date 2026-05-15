import arcade
import random
import time 
import math

SCREEN_WIDTH = 900
SCREEN_HEIGHT =700
SCREEN_TITLE = "игра в kazino"


class StepGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)
        self.x_cos = 0
        self.y_sin = 0

        self.x = 0
        self.y = 0




    def on_update(self, delta_time):
        self.x_cos+=0.01
        self.y_sin+=0.01
        self.x = math.cos(self.x_cos) *100
        self.y = math.sin(self.y_sin) *100
        time.sleep(0.01)

        #y_fi = 

        #https://en.wikipedia.org/wiki/Slider-crank_linkage
        

    def on_draw(self):
        self.clear()
        arcade.draw_circle_filled(500, 500, 100, arcade.color.DARK_BLUE)
        arcade.draw_point(self.x + 500, self.y + 500, arcade.color.RED, 2)
        arcade.draw_line(self.x + 500, self.y + 500, 500, self.y+50, arcade.color.DARK_BLUE, 1)
        arcade.draw_line(500, 200, 500, 0, arcade.color.WHITE, 1)




def main():
    game = StepGame()
    arcade.run()

if __name__ == "__main__":
    main()