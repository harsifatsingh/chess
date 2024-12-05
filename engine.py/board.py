from pieces import Piece

class Board:
    def __init__(self):
        # Initialize an 8x8 board with positions and `Piece.NONE`
        self.squares = {}
        for rank in range(8):
            for file in range(8):
                position = (file, rank)  # Tuple representing the position
                self.squares[position] = Piece.create_piece(Piece.NONE)

    def get_piece(self, position):
        return self.squares[position]
    
    def set_piece(self, position, piece):
        if position not in self.squares:
            raise ValueError("Invalid position on the board.")
        self.squares[position] = piece

    def board_FEN(self):
        FEN = ""
        for rank in range(7, -1, -1):  # Loop from top to bottom ranks
            empty = 0
            for file in range(8):  # Loop through each file in the rank
                position = (file, rank)
                piece = self.get_piece(position)
                
                if piece[0] == Piece.NONE:
                    empty += 1  # Increment empty square counter
                else:
                    if empty > 0:
                        FEN += str(empty)  # Append count of empty squares
                        empty = 0
                    # Append piece representation (uppercase for Black, lowercase for White)
                    piece_char = piece[0][0].lower() if piece[1] == Piece.Color.WHITE else piece[0][0].upper()
                    FEN += piece_char

            if empty > 0:  # Add remaining empty squares in the rank
                FEN += str(empty)

            if rank > 0:  # Add '/' to separate ranks, but not after the last rank
                FEN += "/"

        return FEN




if __name__ == "__main__":
    # Create a board instance
    board = Board()
    print(board.get_piece((0, 0)))
    print(board.board_FEN())
