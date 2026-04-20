import arcade
import random
import time 

SCREEN_WIDTH = 700
SCREEN_HEIGHT =500
SCREEN_TITLE = "игра в kazino"


class StepGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        self.sprite_list = arcade.SpriteList()
        self.sprite = arcade.Sprite("OIP-2262200329.png", scale=0.8)
        self.sprite.center_x = SCREEN_WIDTH//2
        self.sprite.center_y = SCREEN_HEIGHT//2
        self.sprite_list.append(self.sprite)
        self.i = random.randint(120, 200)
        self.flag = True

        self.state = 0        


    def on_mouse_press(self, x, y, button, modifiers):
        self.i = random.randint(120, 200)
        self.kazino()
        if self.state == 12:
            print("max win!!!")
        elif self.state > 0 and self.state < 11:
            print("lose")
        self.flag = True

    def on_key_press(self, key, modifiers):
        pass

    def kazino(self):
        self.sprite.angle = 0
        if random.randint(0,6) == 1:
            self.state = 12
        else:
            self.state = random.randint(0,11)
        print(self.state, "her")

    def on_update(self, delta_time):
        if self.state == 12:
            if self.flag:
                self.i -= 1
                self.sprite.angle += self.i
            if self.i < 20 and self.sprite.angle % 360 < 10:
                self.flag = False
        elif self.state > 0 and self.state <= 11:
            #print("> 0 , < 11")
            if self.flag:
                self.i -= 1
                self.sprite.angle += self.i
            if self.i < 50 and self.sprite.angle % (self.state * 30) < 10 and self.sprite.angle % 360 > 10:
                self.flag = False

    def on_draw(self):
        self.clear()
        self.sprite_list.draw()
    




def main():
    game = StepGame()
    arcade.run()

if __name__ == "__main__":
    main()