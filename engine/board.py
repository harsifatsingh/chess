from engine.pieces import Piece

class Board:
    def __init__(self):
        # Initialize an 8x8 board with positions and `Piece.NONE`
        self.squares = {}
        for rank in range(8):
            for file in range(8):
                position = (file, rank)  # Tuple representing the position
                self.squares[position] = Piece.create_piece(Piece.NONE)

    def set_board(self, FEN):
        # Map FEN symbols to piece types
        piece_type_from_symbol = {
            'k': Piece.KING,
            'p': Piece.PAWN,
            'n': Piece.KNIGHT,
            'b': Piece.BISHOP,
            'r': Piece.ROOK,
            'q': Piece.QUEEN
        }

        # Split FEN string to extract the board part
        fen_board = FEN.split(' ')[0]
        file = 0
        rank = 7  # Start from the top rank

        # Parse the FEN board string
        for symbol in fen_board:
            if symbol == '/':
                # Move to the next rank
                file = 0
                rank -= 1
            elif symbol.isdigit():
                # Skip the number of empty squares
                file += int(symbol)
            else:
                # Determine piece color and type
                piece_color = Piece.Color.WHITE if symbol.isupper() else Piece.Color.BLACK
                piece_type = piece_type_from_symbol[symbol.lower()]
                # Place the piece on the board
                self.squares[(file, rank)] = Piece.create_piece(piece_type, piece_color)
                file += 1

    def get_board(self):
        return self.squares
    
    def is_within_bounds(self, position):
        return 0 <= position[0] < 8 and 0 <= position[1] < 8
    
    def is_empty(self, position):
        return self.squares[position][0] == Piece.NONE
    
    def is_enemy(self, position, color):
        return self.squares[position][0] != Piece.NONE and self.squares[position][1] != color


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

    def move_piece(self, start, end):
        """Move a piece from the start position to the end position."""
        # Check if there's a piece at the start position
        piece = self.get_piece(start)
        if piece[0] == Piece.NONE:
            raise ValueError(f"No piece at position {start} to move.")

        # Get legal moves for the piece
        legal_moves = Piece.legal_moves(start, self)

        # Check if the end position is a legal move
        if end not in legal_moves:
            raise ValueError(f"Illegal move for {piece[0]} from {start} to {end}.")

        # Perform the move
        self.squares[end] = piece  # Move the piece to the end position
        self.squares[start] = Piece.create_piece(Piece.NONE)


if __name__ == "__main__":
    # Create a board instance
    board = Board()
