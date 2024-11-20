from math import inf as infinity
from Settings.gamesettings import X, O, EMPTY

# ALPHA BETA PRUNING SETTINGS
# Cấu hình cho thuật toán cắt tỉa Alpha-Beta

MAX_TREE_DEPTH_LEVEL = 2  # Mức độ sâu tối đa của cây tìm kiếm
EXPANSION_RANGE = 2  # Phạm vi mở rộng để tạo các nước đi có thể

# EVALUATION SCORES
# Điểm đánh giá cho các mẫu thế cờ

SCORE_4_UNBLOCKED_PIECES = 50_007  # Điểm cho 4 quân không bị chặn
SCORE_3_UNBLOCKED_PIECES = 5_005   # Điểm cho 3 quân không bị chặn
SCORE_2_UNBLOCKED_PIECES = 103     # Điểm cho 2 quân không bị chặn
SCORE_1_UNBLOCKED_PIECES = 11      # Điểm cho 1 quân không bị chặn

SCORE_5_BLOCKED_PIECES = 1_000_009 # Điểm cho 5 quân bị chặn (chiến thắng)
SCORE_4_BLOCKED_PIECES = 6_007     # Điểm cho 4 quân bị chặn
SCORE_3_BLOCKED_PIECES = 185       # Điểm cho 3 quân bị chặn

# CHECK BEFORE ALPHA BETA PRUNING
# Kiểm tra trước khi áp dụng thuật toán cắt tỉa Alpha-Beta

ENABLE_HIGH_IMPACT_MOVE = True  # Kích hoạt kiểm tra nước đi có tác động lớn
# Giảm giá trị này có thể giảm thời gian suy nghĩ của AI nhưng cũng giảm chất lượng nước đi
HIGH_IMPACT_MOVE_THRESHOLD = 15440  # Ngưỡng để xác định nước đi có tác động lớn

# EVALUATION PATTERNS
# Các mẫu thế cờ để đánh giá

# Mẫu thế cờ cho X (6 ô)
X_6_PATTERNS = [
    [EMPTY, X, X, X, X, EMPTY],
    [EMPTY, X, X, X, EMPTY, EMPTY],
    [EMPTY, EMPTY, X, X, X, EMPTY],
    [EMPTY, X, X, EMPTY, X, EMPTY],
    [EMPTY, X, EMPTY, X, X, EMPTY],
    [EMPTY, EMPTY, X, X, EMPTY, EMPTY],
    [EMPTY, EMPTY, X, EMPTY, X, EMPTY],
    [EMPTY, X, EMPTY, X, EMPTY, EMPTY],
    [EMPTY, X, EMPTY, EMPTY, X, EMPTY],
    [EMPTY, EMPTY, X, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, X, EMPTY, EMPTY]
]

X_6_PATTERNS_SCORES = [
    SCORE_4_UNBLOCKED_PIECES, 
    SCORE_3_UNBLOCKED_PIECES, 
    SCORE_3_UNBLOCKED_PIECES, 
    SCORE_3_UNBLOCKED_PIECES, 
    SCORE_3_UNBLOCKED_PIECES, 
    SCORE_2_UNBLOCKED_PIECES, 
    SCORE_2_UNBLOCKED_PIECES, 
    SCORE_2_UNBLOCKED_PIECES, 
    SCORE_2_UNBLOCKED_PIECES, 
    SCORE_1_UNBLOCKED_PIECES, 
    SCORE_1_UNBLOCKED_PIECES
]

# Mẫu thế cờ cho X (5 ô)
X_5_PATTERNS = [
    [X, X, X, X, X],
    [X, X, X, X, EMPTY],
    [EMPTY, X, X, X, X],
    [X, X, EMPTY, X, X],
    [X, EMPTY, X, X, X],
    [X, X, X, EMPTY, X],
    [X, EMPTY, X, EMPTY, X],
    [X, X, EMPTY, EMPTY, X],
    [X, EMPTY, EMPTY, X, X],
    [EMPTY, X, X, EMPTY, X],
    [X, EMPTY, X, X, EMPTY],
    [EMPTY, X, X, X, EMPTY],
    [X, X, X, EMPTY, EMPTY],
    [EMPTY, EMPTY, X, X, X]
]

X_5_PATTERNS_SCORES = [
    SCORE_5_BLOCKED_PIECES, 
    SCORE_4_BLOCKED_PIECES, 
    SCORE_4_BLOCKED_PIECES, 
    SCORE_4_BLOCKED_PIECES,
    SCORE_4_BLOCKED_PIECES, 
    SCORE_4_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES
]

X_END_GAME_PATTERN = [X, X, X, X, X]  # Mẫu thế cờ kết thúc game cho X

# Mẫu thế cờ cho O (6 ô)
O_6_PATTERNS = [
    [EMPTY, O, O, O, O, EMPTY],
    [EMPTY, O, O, O, EMPTY, EMPTY],
    [EMPTY, EMPTY, O, O, O, EMPTY],
    [EMPTY, O, O, EMPTY, O, EMPTY],
    [EMPTY, O, EMPTY, O, O, EMPTY],
    [EMPTY, EMPTY, O, O, EMPTY, EMPTY],
    [EMPTY, EMPTY, O, EMPTY, O, EMPTY],
    [EMPTY, O, EMPTY, O, EMPTY, EMPTY],
    [EMPTY, O, EMPTY, EMPTY, O, EMPTY],
    [EMPTY, EMPTY, O, EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY, O, EMPTY, EMPTY]
]

O_6_PATTERNS_SCORES = [
    SCORE_4_UNBLOCKED_PIECES, 
    SCORE_3_UNBLOCKED_PIECES, 
    SCORE_3_UNBLOCKED_PIECES, 
    SCORE_3_UNBLOCKED_PIECES, 
    SCORE_3_UNBLOCKED_PIECES, 
    SCORE_2_UNBLOCKED_PIECES, 
    SCORE_2_UNBLOCKED_PIECES, 
    SCORE_2_UNBLOCKED_PIECES, 
    SCORE_2_UNBLOCKED_PIECES, 
    SCORE_1_UNBLOCKED_PIECES, 
    SCORE_1_UNBLOCKED_PIECES
]

# Mẫu thế cờ cho O (5 ô)
O_5_PATTERNS = [
    [O, O, O, O, O],
    [O, O, O, O, EMPTY],
    [EMPTY, O, O, O, O],
    [O, O, EMPTY, O, O],
    [O, EMPTY, O, O, O],
    [O, O, O, EMPTY, O],
    [O, EMPTY, O, EMPTY, O],
    [O, O, EMPTY, EMPTY, O],
    [O, EMPTY, EMPTY, O, O],
    [EMPTY, O, O, EMPTY, O],
    [O, EMPTY, O, O, EMPTY],
    [EMPTY, O, O, O, EMPTY],
    [O, O, O, EMPTY, EMPTY],
    [EMPTY, EMPTY, O, O, O]
]

O_5_PATTERNS_SCORES = [
    SCORE_5_BLOCKED_PIECES, 
    SCORE_4_BLOCKED_PIECES, 
    SCORE_4_BLOCKED_PIECES, 
    SCORE_4_BLOCKED_PIECES,
    SCORE_4_BLOCKED_PIECES, 
    SCORE_4_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES, 
    SCORE_3_BLOCKED_PIECES
]

O_END_GAME_PATTERN = [O, O, O, O, O]  # Mẫu thế cờ kết thúc game cho O
