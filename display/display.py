import pygame
from engine.pieces import Piece
from engine.board import Board


pygame.init()

board_size = 8
light_colour = (210, 184, 150)
dark_colour = (173, 114, 74)
square_size = 80

screen_size = board_size * square_size
screen = pygame.display.set_mode((screen_size, screen_size))
pygame.display.set_caption("Chess")

piece_images = {
    "P": pygame.image.load("chess/images/bp.svg.png"),  # Black Pawn
    "p": pygame.image.load("chess/images/wp.svg.png"),  # White Pawn
    "R": pygame.image.load("chess/images/br.svg.png"),  # Black Rook
    "r": pygame.image.load("chess/images/wr.svg.png"),  # White Rook
    "N": pygame.image.load("chess/images/bn.svg.png"),  # Black Knight
    "n": pygame.image.load("chess/images/wn.svg.png"),  # White Knight
    "B": pygame.image.load("chess/images/bb.svg.png"),  # Black Bishop
    "b": pygame.image.load("chess/images/wb.svg.png"),  # White Bishop
    "Q": pygame.image.load("chess/images/bq.svg.png"),  # Black Queen
    "q": pygame.image.load("chess/images/wq.svg.png"),  # White Queen
    "K": pygame.image.load("chess/images/bk.svg.png"),  # Black King
    "k": pygame.image.load("chess/images/wk.svg.png"),  # White King
}

for key in piece_images:
    piece_images[key] = pygame.transform.scale(piece_images[key], (square_size, square_size))

def draw_sqaure(color,position):
    pygame.draw.rect(screen, color, (position[0], position[1], square_size, square_size))

def create_graphical_board():
    for file in range(board_size):
        for rank in range(board_size):
            if (file + rank) % 2 == 0:
                draw_sqaure(light_colour, (rank*square_size, file*square_size))
            else:
                draw_sqaure(dark_colour, (rank*square_size, file*square_size))

def draw_pieces(board):
    for position, piece in board.squares.items():
        if piece[0] != Piece.NONE:
            x, y = position[0] * square_size, (7 - position[1]) * square_size
            piece_char = piece[0][0].lower() if piece[1] == Piece.Color.WHITE else piece[0][0].upper()
            if piece_char in piece_images:
                screen.blit(piece_images[piece_char], (x, y))


running = True
board = Board()
board.set_board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
board.move_piece((0, 1), (0, 4))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255, 255, 255))
    create_graphical_board()
    draw_pieces(board)

    pygame.display.flip()

pygame.quit()