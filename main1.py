import pygame
import time
####
#   main1 用于测试
####
# def size
SIZE = WIDTH, HEIGHT = 600, 480
FPS = 10

# def color
BLACK = 0, 0, 0
WHITE = 255, 255, 255

# init
pygame.init()
pygame.mixer.init()

# init screen
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

# enter
running = True
while running:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # update
    font = pygame.font.SysFont('Menlo', 48, True)
    current_time = font.render(time.strftime("%Y:%m:%d %H:%M:%S", time.localtime(time.time())), 1, WHITE)

    # draw
    screen.fill(BLACK)
    screen.blit(current_time, current_time.get_rect(center=(WIDTH/2, HEIGHT/2)))

    # reflesh
    pygame.display.update()

# out
pygame.quit()