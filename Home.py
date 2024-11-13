import pygame
import sys
import subprocess
import os

# Khởi tạo Pygame
pygame.init()

# Constants
GRID_SIZE = 3  # Tic Tac Toe 3x3
CELL_SIZE = 120
BOARD_SIZE = GRID_SIZE * CELL_SIZE
WINDOW_WIDTH = 400  # Không gian cho các nút
WINDOW_HEIGHT = 500  # Không gian cho logo và thông báo
LINE_WIDTH = 10

# Colors
PURPLE = (142, 101, 132)  # Background color
WIN_TEXT_COLOR = (255, 255, 255)
BUTTON_COLOR = (200, 175, 190)
BUTTON_TEXT_COLOR = (255, 255, 255)

# Screen setup
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Nhóm 8")

# Fonts
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 60)

# Tải hình ảnh logo
logo_img_path = os.path.join(os.path.dirname(__file__), "logogame.jpg")
logo_img = None
logo_width, logo_height = 0, 0
if os.path.exists(logo_img_path):
    logo_img = pygame.image.load(logo_img_path)
    logo_width, logo_height = logo_img.get_size()

# Function to draw welcome screen
def draw_welcome_screen():
    screen.fill(PURPLE)
    welcome_text = big_font.render("Tic Tac Toe!", True, WIN_TEXT_COLOR)
    instruction_text = font.render("Select game mode", True, WIN_TEXT_COLOR)
    
    # Vẽ văn bản
    screen.blit(welcome_text, (WINDOW_WIDTH // 2 - welcome_text.get_width() // 2, WINDOW_HEIGHT // 2 - 180))
    screen.blit(instruction_text, (WINDOW_WIDTH // 2 - instruction_text.get_width() // 2, WINDOW_HEIGHT // 2 + 5))
    
    # Vẽ các nút chơi
    one_player_button = pygame.draw.rect(screen, BUTTON_COLOR, (100, 300, 200, 50))
    two_player_button = pygame.draw.rect(screen, BUTTON_COLOR, (100, 370, 200, 50))
    
    # Vẽ văn bản trên các nút
    one_player_text = font.render("1 Player", True, BUTTON_TEXT_COLOR)
    two_player_text = font.render("2 Player", True, BUTTON_TEXT_COLOR)
    screen.blit(one_player_text, (WINDOW_WIDTH // 2 - one_player_text.get_width() // 2, 310))
    screen.blit(two_player_text, (WINDOW_WIDTH // 2 - two_player_text.get_width() // 2, 380))
    
    pygame.display.flip()

# Function to handle button clicks
def handle_button_click(pos):
    if 100 <= pos[0] <= 300:
        if 300 <= pos[1] <= 350:  # Chơi 1 Người
            subprocess.Popen(['python', 'main.py'])  
            pygame.quit()
            sys.exit()
        elif 370 <= pos[1] <= 420:  # Chơi 2 Người
            subprocess.Popen(['python', 'UI.py'])  
            pygame.quit()
            sys.exit()

# Main loop
def main():
    draw_welcome_screen()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_button_click(event.pos)

if __name__ == "__main__":
    main()
