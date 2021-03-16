import pygame

pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

display_size_horizontal = 600
display_size_vertical = 600
# display size in pixels
display = pygame.display.set_mode((display_size_horizontal, display_size_vertical))
# program name
pygame.display.set_caption('Tryryryry')

game_over = False

tractor_horizontal_location = 500
tractor_vertical_location = 300

tractor_width = 100
tractor_height = 100

horizontal_change = 0
vertical_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and tractor_horizontal_location > 0:
                horizontal_change = -tractor_width
                vertical_change = 0
            elif event.key == pygame.K_RIGHT and tractor_horizontal_location < display_size_horizontal - tractor_width:
                horizontal_change = tractor_width
                vertical_change = 0
            elif event.key == pygame.K_UP and tractor_vertical_location > 0:
                vertical_change = -tractor_height
                horizontal_change = 0
            elif event.key == pygame.K_DOWN and tractor_vertical_location < display_size_vertical - tractor_height:
                vertical_change = tractor_height
                horizontal_change = 0

    tractor_horizontal_location += horizontal_change
    tractor_vertical_location += vertical_change
    display.fill(white)
    pygame.draw.rect(display, black,
                     [tractor_horizontal_location, tractor_vertical_location, tractor_width, tractor_height])

    print(tractor_horizontal_location, " ", tractor_vertical_location)

    pygame.display.update()
    clock.tick(10)
    horizontal_change = 0
    vertical_change = 0
#commit test 2
#sprawdź czy działa

pygame.quit()
quit()
