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
        self.staty = [0,0]
        self.ti = 0

        self.to_draw_x = 0
        self.to_draw_y = 0
        self.to_draw_x2 = 0
        self.to_draw_y2 = 0

    def on_mouse_press(self, x, y, button, modifiers):
        """оброботка мыши"""
        print("x:", x," y:", y)
        print(self.staty)
        self.x_start = x
        self.y_start = y
        self.staty.append(self.x_start)
        self.staty.append(self.y_start)
        self.staty.pop(len(self.staty)-2)
        self.staty.pop(len(self.staty)-2)


        #self.staty = [self.x_start, self.y_start]

    def on_key_press(self, key, modifiers):
        if key == arcade.key.C:
            self.to_clear = True

    def update(self):
        self.timer += 1

        if 1 < self.timer:
            self.draw_line_flag = True
            self.timer = 0


    def on_draw(self):

        self.update()

        way = random.randint(1,4)
        #if way == 1:
        #    x2 = random.uniform(self.x_start, self.x_start + 100 ) 
        #    y2 = random.uniform(self.y_start, self.y_start) 
        #elif way == 2:
        #    x2 = random.uniform(self.x_start - 100, self.x_start) 
        #    y2 = random.uniform(self.y_start, self.y_start) 
        #elif way == 3:
        #    x2 = random.uniform(self.x_start, self.x_start) 
        #    y2 = random.uniform(self.y_start, self.y_start + 100 ) 
        #elif way == 4:
        #    x2 = random.uniform(self.x_start, self.x_start) 
        #    y2 = random.uniform(self.y_start - 100, self.y_start) 


        if way == 1:
            x2 = random.choice((self.x_start + 10, self.x_start + 20))
            y2 = self.y_start
        elif way == 2:
            x2 = random.choice((self.x_start - 10, self.x_start - 20))
            y2 = self.y_start
        elif way == 3:
            x2 = self.x_start
            y2 = random.choice((self.y_start + 10, self.y_start + 20))
        elif way == 4:
            x2 = self.x_start
            y2 = random.choice((self.y_start - 10, self.y_start - 20))


        #x2 = random.uniform(self.x_start - 100, self.x_start + 100 ) 
        #y2 = random.uniform(self.y_start - 100, self.y_start + 100 ) 


        self.clear()



        if self.draw_line_flag == True:
            arcade.draw_line(self.x_start, self.y_start, x2, y2, arcade.color.BLUE, 3)
            #self.to_draw_x = self.x_start
            #self.to_draw_y = self.y_start
            #self.to_draw_x2 = x2
            #self.to_draw_y2 = y2
#---
            self.staty.append(self.x_start)
            self.staty.append(self.y_start)
            self.x_start = x2
            self.y_start = y2
            #if self.ti > 2:
            #    self.ti = 0
            #    self.staty.pop(0)
            #    self.staty.pop(0)
            #else:
            #    self.ti += 1

            self.draw_line_flag = False
        #arcade.draw_line(self.to_draw_x, self.to_draw_y, self.to_draw_x2, self.to_draw_y2, arcade.color.BLUE, 3)

        i=0
        h=1
        i2=2
        h2=3


        while h2 < len(self.staty):
            arcade.draw_line(self.staty[i], self.staty[h], self.staty[i2], self.staty[h2], arcade.color.BLUE, 3)
            i+=2
            h+=2
            i2+=2
            h2+=2
            



def main():
    game = StepGame()
    arcade.run()

if __name__ == "__main__":
    main()
