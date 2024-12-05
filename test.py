import pygame

pygame.init()

board_size = 8
light_colour = (210, 184, 150)
dark_colour = (173, 114, 74)
square_size = 50

screen_size = board_size * square_size
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("Chess")



def draw_sqaure(color,position):
    pygame.draw.rect(screen, color, (position[0], position[1], square_size, square_size))

def create_graphical_board():
    for file in range(board_size):
        for rank in range(board_size):
            if (file + rank) % 2 == 0:
                draw_sqaure(light_colour, (rank*square_size, file*square_size))
            else:
                draw_sqaure(dark_colour, (rank*square_size, file*square_size))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    create_graphical_board()

    pygame.display.flip()


pygame.quit()