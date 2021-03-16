import pygame
# wersja 1.02
from constants import *

from Main.constants import *

pygame.init()

# display size in pixels
display = pygame.display.set_mode((DISPLAY_SIZE_HORIZONTAL, DISPLAY_SIZE_VERTICAL))
# program name
pygame.display.set_caption('Tryryryry')

game_over = False

tractor_horizontal_location = TRACTOR_HORIZONTAL_LOCATION
tractor_vertical_location = TRACTOR_VERTICAL_LOCATION

horizontal_change = 0
vertical_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            print(tractor_horizontal_location, " ", tractor_vertical_location)
            if event.key == pygame.K_LEFT and tractor_horizontal_location > 0:
                horizontal_change = -TRACTOR_WIDTH
                vertical_change = 0
            elif event.key == pygame.K_RIGHT and tractor_horizontal_location < DISPLAY_SIZE_HORIZONTAL - TRACTOR_WIDTH:
                horizontal_change = TRACTOR_WIDTH
                vertical_change = 0
            elif event.key == pygame.K_UP and tractor_vertical_location > 0:
                vertical_change = -TRACTOR_HEIGHT
                horizontal_change = 0
            elif event.key == pygame.K_DOWN and tractor_vertical_location < DISPLAY_SIZE_VERTICAL - TRACTOR_HEIGHT:
                vertical_change = TRACTOR_HEIGHT
                horizontal_change = 0

    tractor_horizontal_location += horizontal_change
    tractor_vertical_location += vertical_change
    display.fill(WHITE)
    for i in range(int(HORIZONTAL_TILES_NUMBER)):
        for j in range(int(VERTICAL_TILES_NUMBER)):
            if board[i][j] == 0:
                color = GREEN
            elif board[i][j] == 1:
                color = BLACK
            elif board[i][j] == 2:
                color = BLACK
            elif board[i][j] == 3:
                color = BLACK


    pygame.draw.rect(display, BLACK,
                     [tractor_horizontal_location, tractor_vertical_location, TRACTOR_WIDTH, TRACTOR_HEIGHT])

    pygame.display.update()
    clock.tick(FPS)
    horizontal_change = 0
    vertical_change = 0
# commit test 2

pygame.quit()
quit()
