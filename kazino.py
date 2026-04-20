import arcade
import random
import time 

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "игра в kazino"


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
        pass
    
    def on_mouse_motion(self, x, y, dx, dy):
        pass

    def on_key_press(self, key, modifiers):
        pass

    def create_vector(self, x, y):
        pass



    def on_draw(self):
        pass
    




def main():
    game = StepGame()
    arcade.run()

if __name__ == "__main__":
    main()