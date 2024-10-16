import pygame
import sys
import subprocess
import os

# Khởi tạo Pygame
pygame.init()

# Kích thước cửa sổ
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 700

# Màu sắc
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Tạo cửa sổ
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("GAME TIC TAC TOE NHÓM 2")

# Font cho văn bản
font = pygame.font.Font(None, 36)
big_font = pygame.font.Font(None, 50)

# Văn bản cho label
member_info_text1 = "VO VAN TRINH                   2254810220"
member_info_text2 = "NGUYEN LUONG TRI       2254810222"
member_info_text3 = "NGUYEN KHANH DUY    2254810237"
member_info_font = pygame.font.Font(None, 28)  # Tăng cỡ chữ
member_info_color = BLACK

# Tải nhạc nền
music_path = os.path.join(os.path.dirname(__file__), "nhacnen.mp3")
if os.path.exists(music_path):
    try:
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play(-1)  # Phát nhạc lặp vô hạn
    except pygame.error as e:
        print(f"Error loading music: {e}")
else:
    print(f"Music file not found at {music_path}")

mouseX, mouseY = -1, -1

# Vòng lặp chính
while True:
    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()

    # Check for button clicks
    button_width = 400
    button_height = 55
    button_x = (WINDOW_WIDTH - button_width) // 2
    button_y1 = (WINDOW_HEIGHT - button_height) // 2 - 50  # Play with human
    button_y2 = (WINDOW_HEIGHT - button_height) // 2 + 50  # Play with AI

    # Kiểm tra xem có bấm vào button "PLAY WITH HUMAN"
    if button_x <= mouseX <= button_x + button_width and button_y1 <= mouseY <= button_y1 + button_height:
        pygame.quit()
        run_another_script("UI.py")  # Chạy script cho chế độ chơi với người
        sys.exit()

    # Kiểm tra xem có bấm vào button "PLAY WITH AI"
    elif button_x <= mouseX <= button_x + button_width and button_y2 <= mouseY <= button_y2 + button_height:
        pygame.quit()
        run_another_script("main.py")  # Chạy script cho chế độ chơi với người vs AI
        sys.exit()

    # Vẽ nền trắng
    screen.fill(WHITE)

    # Vẽ hai nút trung tâm
    pygame.draw.rect(screen, GRAY, (button_x, button_y1, button_width, button_height))
    pygame.draw.rect(screen, GRAY, (button_x, button_y2, button_width, button_height))

    # Vẽ văn bản cho các nút
    text_reset = font.render("PLAY WITH HUMAN", True, BLACK)
    text_ai = font.render("PLAY WITH AI", True, BLACK)

    screen.blit(text_reset, (button_x + (button_width - text_reset.get_width()) // 2, button_y1 + (button_height - text_reset.get_height()) // 2))
    screen.blit(text_ai, (button_x + (button_width - text_ai.get_width()) // 2, button_y2 + (button_height - text_ai.get_height()) // 2))

    # Vẽ nhãn (label) cho thông tin chào mừng
    text_label = big_font.render("TRI TUE NHAN TAO", True, BLACK)
    label_rect = text_label.get_rect(center=(WINDOW_WIDTH // 2, 50))
    screen.blit(text_label, label_rect)

    # Tải hình ảnh logo
    logo_img_path = os.path.join(os.path.dirname(__file__), "logo.png")
    if os.path.exists(logo_img_path):
        logo_img = pygame.image.load(logo_img_path)
        logo_width, logo_height = logo_img.get_size()

        # Vẽ logo dưới nhãn chào mừng
        logo_x = (WINDOW_WIDTH - logo_width) // 2
        logo_y = label_rect.bottom + 30  # Khoảng cách 30 pixel dưới nhãn chính
        screen.blit(logo_img, (logo_x, logo_y))
    else:
        print(f"Logo image not found at {logo_img_path}")

    # Vẽ nhãn (label) cho thông tin thành viên và mã số sinh viên
    member_info_surface1 = member_info_font.render(member_info_text1, True, member_info_color)
    member_info_rect1 = member_info_surface1.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 200))
    screen.blit(member_info_surface1, member_info_rect1)

    member_info_surface2 = member_info_font.render(member_info_text2, True, member_info_color)
    member_info_rect2 = member_info_surface2.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 150))
    screen.blit(member_info_surface2, member_info_rect2)

    member_info_surface3 = member_info_font.render(member_info_text3, True, member_info_color)
    member_info_rect3 = member_info_surface3.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT - 100))
    screen.blit(member_info_surface3, member_info_rect3)

    # Cập nhật màn hình
    pygame.display.flip()
