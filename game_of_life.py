import arcade 
import copy
import time

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "игра в жизнь. клеточный автомат"

CELL_SIZE = 10
GRID_WIDTH = SCREEN_WIDTH // CELL_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // CELL_SIZE

#цвета
COLOR_BACKGROUND = arcade.color.WHITE 
COLOR_GRID = arcade.color.BLACK 
COLOR_EMPTY = arcade.color.LIGHT_GRAY 
COLOR_FILLED = arcade.color.BLUE 

class GridGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(COLOR_BACKGROUND)

        self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

        self.running = False
        self.time_since_update = 0
        self.update_interval = 0.3

    def on_draw(self):
        """Отрисовка кадра"""
        self.clear()
        
        #клетки
        for row in range(GRID_HEIGHT):
            for col in range(GRID_WIDTH):
                left = col * CELL_SIZE + 1
                right = (col + 1) * CELL_SIZE - 1
                bottom = row * CELL_SIZE + 1
                top = (row + 1) * CELL_SIZE - 1

                # Выбираем цвет в зависимости от значения в сетке
                if self.grid[row][col] == 0:
                    color = COLOR_EMPTY
                else:
                    color = COLOR_FILLED

                # Рисуем заполненный прямоугольник (lrbt - left, right, bottom, top)
                arcade.draw_lrbt_rectangle_filled(left, right, bottom, top, color)
                
                # Рисуем контур
                arcade.draw_lrbt_rectangle_outline(left, right, bottom, top, COLOR_GRID, 2)

    def on_mouse_press(self, x, y, button, modifiers):
        col = int(x // CELL_SIZE)
        row = int(y // CELL_SIZE)

        if 0 <= row < GRID_HEIGHT and 0 <= col < GRID_WIDTH:
            self.grid[row][col] = 1 - self.grid[row][col]
            print(f"клетка [{row}][{col}] = {self.grid[row][col]}")

    def update_grid(self):
        matrix_fantom = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        #print()
        #print("-------------------------------------")
        #print()
        for i in range(GRID_HEIGHT):
            #print()
            for j in range(GRID_WIDTH):
                #print(matrix[i][j], end="")
                flag = True
                vel = 0

                if i == 0 or i == GRID_HEIGHT-1 or j == 0 or j == GRID_WIDTH-1:
                    flag = False

                if self.grid[i][j] == 1 and flag:
                    n = self.grid[i-1][j-1] + self.grid[i-1][j] + self.grid[i-1][j+1] + self.grid[i][j-1] + self.grid[i][j+1] + self.grid[i+1][j-1] + self.grid[i+1][j] + self.grid[i+1][j+1]
                    if n == 2 or n == 3:
                        vel = 1
                    else:
                        vel = 0

                if self.grid[i][j] == 0 and flag:
                    n_none = self.grid[i-1][j-1] + self.grid[i-1][j] + self.grid[i-1][j+1] + self.grid[i][j-1] + self.grid[i][j+1] + self.grid[i+1][j-1] + self.grid[i+1][j] + self.grid[i+1][j+1]
                    if n_none == 3:
                        vel = 1
                    else:
                        vel = 0

                matrix_fantom[i][j] = vel

        self.grid = copy.deepcopy(matrix_fantom)

    def on_update(self, delta_time):
        """вызывается каждый кадр"""
        if self.running:
            self.time_since_update += delta_time
            
            if self.time_since_update >= self.update_interval:
                self.update_grid()
                self.time_since_update = 0

    def on_key_press(self, key, modifiers):
        """Обработка нажатий клавиш"""
        if key == arcade.key.SPACE:
            # Запуск/пауза симуляции
            self.running = not self.running
            print(f"Симуляция: {'запущена' if self.running else 'остановлена'}")
        
        elif key == arcade.key.C:
            # Очистка поля
            self.grid = [[0 for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
            self.running = False
            print("Поле очищено")
        
        elif key == arcade.key.R:
            # Один шаг симуляции
            if not self.running:
                self.update_grid()
                print("Один шаг выполнен")


def main():
    game = GridGame()
    arcade.run()

#    matrix = [[0 for _ in range(50)] for _ in range(50)]
#    matrix[12][20] = 1
#    matrix[12][21] = 1
#    matrix[13][20] = 1
#    matrix[13][19] = 1
#    matrix[14][20] = 1
#    matrix[14][19] = 1
#    matrix[14][18] = 1
#
#
#    while True:
#        time.sleep(1.2)
#        matrix_fantom = [[0 for _ in range(50)] for _ in range(50)]
#        print()
#        print("-------------------------------------")
#        print()
#        for i in range(len(matrix)):
#            print()
#            for j in range(len(matrix[i])):
#                print(matrix[i][j], end="")
#                flag = True
#                vel = 0
#
#                if i == 0 or i == len(matrix)-1 or j == 0 or j == len(matrix[i])-1:
#                    flag = False
#
#                if matrix[i][j] == 1 and flag:
#                    n = matrix[i-1][j-1] + matrix[i-1][j] + matrix[i-1][j+1] + matrix[i][j-1] + matrix[i][j+1] + matrix[i+1][j-1] + matrix[i+1][j] + matrix[i+1][j+1]
#                    if n == 2 or n == 3:
#                        vel = 1
#                    else:
#                        vel = 0
#
#                if matrix[i][j] == 0 and flag:
#                    n_none = matrix[i-1][j-1] + matrix[i-1][j] + matrix[i-1][j+1] + matrix[i][j-1] + matrix[i][j+1] + matrix[i+1][j-1] + matrix[i+1][j] + matrix[i+1][j+1]
#                    if n_none == 3:
#                        vel = 1
#                    else:
#                        vel = 0
#
#                matrix_fantom[i][j] = vel
#
#        matrix = copy.deepcopy(matrix_fantom)




if __name__ == "__main__":
    main()
