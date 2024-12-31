import pygame
import chess

pygame.init()

WIDTH, HEIGHT = 640, 640
SQ_SIZE = WIDTH // 8
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BROWN = (245, 222, 179)
DARK_BROWN = (139, 69, 19)

def draw_board(screen, board):
    font = pygame.font.SysFont(None, 64)
    piece_symbols = {
        'P': '♙', 'N': '♘', 'B': '♗', 'R': '♖', 'Q': '♕', 'K': '♔',
        'p': '♟', 'n': '♞', 'b': '♝', 'r': '♜', 'q': '♛', 'k': '♚'
    }
    
    for row in range(8):
        for col in range(8):
            color = LIGHT_BROWN if (row + col) % 2 == 0 else DARK_BROWN
            pygame.draw.rect(screen, color, pygame.Rect(col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE))

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece:
            symbol = piece_symbols[piece.symbol()]
            row, col = 7 - chess.square_rank(square), chess.square_file(square)
            text_surface = font.render(symbol, True, WHITE if piece.color == chess.WHITE else BLACK)
            screen.blit(text_surface, (col * SQ_SIZE + 10, row * SQ_SIZE + 10))

def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption('Chess Game')
    board = chess.Board()
    running = True
    selected_square = None

    while running:
        draw_board(screen, board)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                col = pos[0] // SQ_SIZE
                row = 7 - (pos[1] // SQ_SIZE)
                square = chess.square(col, row)
                piece = board.piece_at(square)

                if selected_square and (piece is None or piece.color != board.turn):
                    move = chess.Move(selected_square, square)
                    if move in board.legal_moves:
                        board.push(move)
                        selected_square = None
                elif piece and piece.color == board.turn:
                    selected_square = square

    pygame.quit()

if __name__ == "__main__":
    main()
