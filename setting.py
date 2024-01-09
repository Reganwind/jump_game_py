#game options/setting
TITLE = "Jumpy"
WIDTH = 480
HEIGHT = 320
FPS = 60  ##调整游戏速度
SIZE = WIDTH, HEIGHT
FONT_NAME = 'arial'

# Player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAV = 0.8
PLAYER_JUMP = 20

# Starting platforms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH, 40),
                 (WIDTH / 2 - 50, HEIGHT * 3/ 4, 100, 20),
                 (125, HEIGHT - 350, 100, 20),
                 (350, 200, 100, 20),
                 (175, 100, 50, 20)]

#define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTBLUE = (0, 155, 155)

# define player bound
PLAYER_TOP_LIMIT = 100
PLAYER_BOTTOM_LIMIT = 250