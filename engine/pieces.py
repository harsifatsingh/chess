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

    @staticmethod
    def create_piece(piece_type, color=None):
        if piece_type == Piece.NONE:
            return [Piece.NONE, None]
        if color not in (Piece.Color.WHITE, Piece.Color.BLACK):
            raise ValueError("Invalid color. Choose 'white' or 'black'.")
        return [piece_type, color]

    @staticmethod
    def legal_moves(position, board):
        """Calculate legal moves for a piece given its position and the current board state."""
        from engine.board import Board

        piece_type, color = board.get_piece(position)
        file, rank = position
        moves = []

        if piece_type == Piece.PAWN:
            direction = 1 if color == Piece.Color.WHITE else -1
            # Move forward one square
            if (file, rank + direction) in board.squares and board.squares[
                (file, rank + direction)
            ][0] == Piece.NONE:
                moves.append((file, rank + direction))
            # Initial two-square move
            if (color == Piece.Color.WHITE and rank == 1) or (
                color == Piece.Color.BLACK and rank == 6
            ):
                if (
                    board.squares.get((file, rank + 2 * direction), [Piece.NONE])[0]
                    == Piece.NONE
                ):
                    moves.append((file, rank + 2 * direction))
            # Capture diagonally
            for capture_file in [file - 1, file + 1]:
                if (capture_file, rank + direction) in board.squares:
                    target_piece = board.squares[(capture_file, rank + direction)]
                    if target_piece[0] != Piece.NONE and target_piece[1] != color:
                        moves.append((capture_file, rank + direction))

        elif piece_type == Piece.ROOK:
            moves.extend(
                Piece._line_moves(position, board, [(0, 1), (1, 0), (0, -1), (-1, 0)])
            )

        elif piece_type == Piece.BISHOP:
            moves.extend(
                Piece._line_moves(position, board, [(1, 1), (-1, 1), (1, -1), (-1, -1)])
            )

        elif piece_type == Piece.QUEEN:
            moves.extend(
                Piece._line_moves(
                    position,
                    board,
                    [
                        (0, 1),
                        (1, 0),
                        (0, -1),
                        (-1, 0),
                        (1, 1),
                        (-1, 1),
                        (1, -1),
                        (-1, -1),
                    ],
                )
            )

        elif piece_type == Piece.KNIGHT:
            knight_moves = [
                (file + 1, rank + 2),
                (file - 1, rank + 2),
                (file + 2, rank + 1),
                (file - 2, rank + 1),
                (file + 1, rank - 2),
                (file - 1, rank - 2),
                (file + 2, rank - 1),
                (file - 2, rank - 1),
            ]
            for move in knight_moves:
                if move in board.squares:
                    target_piece = board.squares[move]
                    if target_piece[0] == Piece.NONE or target_piece[1] != color:
                        moves.append(move)

        elif piece_type == Piece.KING:
            king_moves = [
                (file + dx, rank + dy)
                for dx, dy in [
                    (-1, 0),
                    (1, 0),
                    (0, -1),
                    (0, 1),
                    (-1, -1),
                    (-1, 1),
                    (1, -1),
                    (1, 1),
                ]
            ]
            for move in king_moves:
                if move in board.squares:
                    target_piece = board.squares[move]
                    if target_piece[0] == Piece.NONE or target_piece[1] != color:
                        moves.append(move)

        return moves

    @staticmethod
    def _line_moves(position, board, directions):
        """Helper function to calculate moves in straight or diagonal lines."""
        file, rank = position
        moves = []

        for dx, dy in directions:
            x, y = file + dx, rank + dy
            while (x, y) in board.squares:
                target_piece = board.squares[(x, y)]
                if target_piece[0] == Piece.NONE:
                    moves.append((x, y))
                elif target_piece[1] != board.squares[position][1]:  # Opponent's piece
                    moves.append((x, y))
                    break
                else:  # Own piece
                    break
                x += dx
                y += dy

        return moves


if __name__ == "__main__":
    # Initialize a board and set some pieces
    from engine.board import Board

    board = Board()
    board.set_piece((0, 6), [Piece.PAWN, Piece.Color.BLACK])
    board.set_piece((0, 0), [Piece.ROOK, Piece.Color.WHITE])

    # Get legal moves for a white pawn at (0, 1)
    white_pawn_moves = Piece.legal_moves((0, 1), board)
    print("White Pawn Moves:", white_pawn_moves)

    # Get legal moves for a white rook at (0, 0)
    white_rook_moves = Piece.legal_moves((0, 0), board)
    print("White Rook Moves:", white_rook_moves)
