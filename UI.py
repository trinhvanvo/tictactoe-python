import pygame
import sys
import subprocess
import os

# Khởi tạo Pygame
pygame.init()

# Tải nhạc nền


# Constants
GRID_SIZE = 11  # Tic Tac Toe 3x3
CELL_SIZE = 40
BOARD_SIZE = GRID_SIZE * CELL_SIZE
WINDOW_WIDTH = BOARD_SIZE + 120  # Không gian cho các nút
WINDOW_HEIGHT = BOARD_SIZE + 150  # Không gian cho thông báo
LINE_WIDTH = 2
WIN_CONDITION = 5  # Điều kiện thắng

# Colors
PURPLE = (142, 101, 132)  # Background color
LIGHT_PINK = (255, 203, 192)  # Color for 'O'
SOFT_YELLOW = (242, 214, 143)  # Color for 'X'
BUTTON_COLOR = (200, 175, 190)
BUTTON_TEXT_COLOR = (255, 255, 255)
WIN_TEXT_COLOR = (255, 255, 255)
GRID_COLOR = (255, 255, 255)

# Screen setup
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Nhóm 8")

# Fonts
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 100)
score_font = pygame.font.Font(None, 28)

# Game variables
board = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
current_player = 'X'
game_over = False
winner = None
x_wins = 0
o_wins = 0
move_history = []  # Lịch sử các nước đi

def draw_board():
    screen.fill(PURPLE)
    board_start_x = (WINDOW_WIDTH - BOARD_SIZE) // 2
    board_start_y = 50

    # Vẽ các ô và các kí tự X, O
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(board_start_x + col * CELL_SIZE, board_start_y + row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRID_COLOR, rect, LINE_WIDTH)
            if board[row][col] != '':
                color = SOFT_YELLOW if board[row][col] == 'X' else LIGHT_PINK
                text = font.render(board[row][col], True, color)  # Vẽ kí tự lớn X và O
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)         

    # Vẽ số lần thắng
    score_offset_x = WINDOW_WIDTH - 550  # Vị trí hiển thị ở bên phải
    screen.blit(score_font.render("WIN", True, WIN_TEXT_COLOR), (score_offset_x, board_start_y))
    screen.blit(score_font.render(f"X: {x_wins}", True, SOFT_YELLOW), (score_offset_x, board_start_y + 50))
    screen.blit(score_font.render(f"O: {o_wins}", True, LIGHT_PINK), (score_offset_x, board_start_y + 100))

    # Vẽ các nút
    button_width = 150
    button_height = 50
    button_y = WINDOW_HEIGHT - button_height - 30

    # Nút New Game
    new_game_button_x = (WINDOW_WIDTH - 3 * button_width) // 2
    new_game_button = pygame.Rect(new_game_button_x, button_y, button_width, button_height)
    pygame.draw.rect(screen, BUTTON_COLOR, new_game_button, border_radius=10)
    new_game_text = font.render("New Game", True, BUTTON_TEXT_COLOR)
    screen.blit(new_game_text, (new_game_button.x + (new_game_button.width - new_game_text.get_width()) // 2, new_game_button.y + (new_game_button.height - new_game_text.get_height()) // 2))

    # Nút Undo
    undo_button_x = new_game_button_x + button_width + 20
    undo_button = pygame.Rect(undo_button_x, button_y, button_width, button_height)
    pygame.draw.rect(screen, BUTTON_COLOR, undo_button, border_radius=10)
    undo_text = font.render("Undo", True, BUTTON_TEXT_COLOR)
    screen.blit(undo_text, (undo_button.x + (undo_button.width - undo_text.get_width()) // 2, undo_button.y + (undo_button.height - undo_text.get_height()) // 2))

    # Nút Home
    ai_game_button_x = undo_button_x + button_width + 20
    ai_game_button = pygame.Rect(ai_game_button_x, button_y, button_width, button_height)
    pygame.draw.rect(screen, BUTTON_COLOR, ai_game_button, border_radius=10)
    ai_game_text = font.render("Home", True, BUTTON_TEXT_COLOR)
    screen.blit(ai_game_text, (ai_game_button.x + (ai_game_button.width - ai_game_text.get_width()) // 2, ai_game_button.y + (ai_game_button.height - ai_game_text.get_height()) // 2))

def check_winner():
    global game_over, winner, x_wins, o_wins

    # Kiểm tra các hàng, cột, và đường chéo
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] != '':
                if check_direction(row, col, 1, 0) or check_direction(row, col, 0, 1) or check_direction(row, col, 1, 1) or check_direction(row, col, 1, -1):
                    winner = board[row][col]
                    if winner == 'X':
                        x_wins += 1
                    else:
                        o_wins += 1
                    game_over = True
                    return

def check_direction(row, col, d_row, d_col):
    consecutive_count = 0
    for i in range(WIN_CONDITION):
        r = row + i * d_row
        c = col + i * d_col
        if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE and board[r][c] == board[row][col]:
            consecutive_count += 1
        else:
            break
    return consecutive_count == WIN_CONDITION

def display_winner():
    if winner:
        text = font.render(f'{winner} WIN!', True, WIN_TEXT_COLOR)
        screen.blit(text, (WINDOW_WIDTH // 2 - text.get_width() // 2, WINDOW_HEIGHT - 578))
        pygame.display.update()

def reset_game():
    global board, current_player, game_over, winner, move_history
    board = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    current_player = 'X'
    game_over = False
    winner = None
    move_history.clear()

# Main game loop
show_welcome = True  # Biến kiểm tra có hiển thị màn hình chào mừng không
while True:
        draw_board()
        if game_over:
            display_winner()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouseX, mouseY = pygame.mouse.get_pos()

                # Kiểm tra nếu người chơi click vào nút
                button_width = 150
                button_height = 50
                button_y = WINDOW_HEIGHT - button_height - 30
                new_game_button_x = (WINDOW_WIDTH - 3 * button_width) // 2
                undo_button_x = new_game_button_x + button_width + 20
                ai_game_button_x = undo_button_x + button_width + 20

                # Nút New Game
                if new_game_button_x <= mouseX <= new_game_button_x + button_width and button_y <= mouseY <= button_y + button_height:
                    reset_game()

                # Nút Undo
                elif undo_button_x <= mouseX <= undo_button_x + button_width and button_y <= mouseY <= button_y + button_height:
                    if len(move_history) > 0:
                        last_move = move_history.pop()  # Xóa nước đi cuối
                        board[last_move[0]][last_move[1]] = ''  # Xóa nước đi đó khỏi bàn cờ
                        current_player = 'O' if current_player == 'X' else 'X'  # Đổi lượt chơi
                        game_over = False  # Tiếp tục trò chơi

                # Nút Home (chuyển về màn hình chính)
                elif ai_game_button_x <= mouseX <= ai_game_button_x + button_width and button_y <= mouseY <= button_y + button_height:
                    pygame.quit()
                    subprocess.run(["python", "Home.py"])

                # Người chơi đánh dấu X hoặc O lên bàn cờ
                else:
                    board_start_x = (WINDOW_WIDTH - BOARD_SIZE) // 2
                    board_start_y = 50
                    if board_start_x <= mouseX < board_start_x + BOARD_SIZE and board_start_y <= mouseY < board_start_y + BOARD_SIZE:
                        row = (mouseY - board_start_y) // CELL_SIZE
                        col = (mouseX - board_start_x) // CELL_SIZE

                    if board[row][col] == '' and not game_over:
                        board[row][col] = current_player
                        move_history.append((row, col))  # Lưu lịch sử nước đi
                        check_winner()
                        if not game_over:
                            current_player = 'O' if current_player == 'X' else 'X'  # Đổi lượt chơi
        pygame.display.update()
