class Piece:
    class Color:
        WHITE = "white"
        BLACK = "black"

    PAWN = "Pawn"
    ROOK = "Rook"
    KNIGHT = "Knight"
    BISHOP = "Bishop"
    KING = "King"
    QUEEN = "Queen"
    NONE = None

    def create_piece(piece_type, color=None):
        if piece_type == Piece.NONE:
            return [Piece.NONE, None]
        if color not in (Piece.Color.WHITE, Piece.Color.BLACK):
            raise ValueError("Invalid color. Choose 'white' or 'black'.")
        return [piece_type, color]