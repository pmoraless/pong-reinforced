import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game screen
screen = pygame.display.set_mode((600, 400))
clock = pygame.time.Clock()

# Initialize Q-table for reinforcement learning
q_table = {}
for ball_x_offset in range(-10, 11):
    for ball_y_offset in range(-10, 11):
        for paddle1_y_offset in range(-10, 11):
            for paddle2_y_offset in range(-10, 11):
                q_table[(ball_x_offset, ball_y_offset, paddle1_y_offset, paddle2_y_offset)] = [random.uniform(0, 1) for _ in range(3)]

# Hyperparameters
learning_rate = 0.2
discount_factor = 0.8
exploration_probability = 0.2

# Initialize game variables
ball_position_x, ball_position_y = 300, 200
ball_velocity_x, ball_velocity_y = random.choice([-4, 4]), random.choice([-4, 4])
paddle1_position_y, paddle2_position_y = 150, 150
score_left, score_right = 0, 0
cumulative_wins_left, cumulative_wins_right = 0, 0

# Update game state function
def state(chosen_action):
    global ball_position_x, ball_position_y, ball_velocity_x, ball_velocity_y, paddle1_position_y, paddle2_position_y, score_left, score_right, cumulative_wins_left, cumulative_wins_right
    
    # Update left paddle position based on the chosen action
    if chosen_action == 0 and paddle1_position_y > 0:
        paddle1_position_y -= 5
    elif chosen_action == 2 and paddle1_position_y < 300:
        paddle1_position_y += 5
    
    # Update ball position
    ball_position_x += ball_velocity_x
    ball_position_y += ball_velocity_y
    
    # Reflect ball when it hits the top or bottom of the screen
    if ball_position_y < 0 or ball_position_y > 390:
        ball_velocity_y *= -1
    
    # Check if the ball hits the left paddle
    if ball_position_x < 20 and paddle1_position_y < ball_position_y < paddle1_position_y + 100:
        ball_velocity_x *= -1
        score_left += 1
    
    # Check if the ball hits the right paddle
    elif ball_position_x > 580 and paddle2_position_y < ball_position_y < paddle2_position_y + 100:
        ball_velocity_x *= -1
        score_right += 1
    
    # Check if the ball goes out of bounds on the left or right
    elif ball_position_x < 0 or ball_position_x > 600:
        ball_position_x, ball_position_y = 300, 200
        ball_velocity_x, ball_velocity_y = random.choice([-4, 4]), random.choice([-4, 4])
        
        # Update cumulative wins based on the game outcome
        if score_left > score_right:
            cumulative_wins_left += 1
        elif score_right > score_left:
            cumulative_wins_right += 1
        
        score_left, score_right = 0, 0
    
    # Update right paddle position based on the ball position
    if ball_position_y < paddle2_position_y + 50 and paddle2_position_y > 0:
        paddle2_position_y -= 5
    elif ball_position_y > paddle2_position_y + 50 and paddle2_position_y < 300:
        paddle2_position_y += 5

# Draw display function
def draw_display():
    screen.fill((0, 0, 0))
    
    # Draw left paddle
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(0, paddle1_position_y, 10, 100))
    
    # Draw right paddle
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(590, paddle2_position_y, 10, 100))
    
    # Draw ball
    pygame.draw.circle(screen, (255, 255, 255), (int(ball_position_x), int(ball_position_y)), 10)
    
    # Draw center line
    pygame.draw.line(screen, (255, 255, 255), (300, 0), (300, 400))
    
    # Draw scores
    font = pygame.font.SysFont(None, 30)
    score_text = font.render(f"{score_left} - {score_right}", True, (255, 255, 255))
    screen.blit(score_text, (260, 10))
    
    # Display cumulative wins
    wins_text = font.render(f"Wins: {cumulative_wins_left} - {cumulative_wins_right}", True, (255, 255, 255))
    screen.blit(wins_text, (200, 350))
    
    pygame.display.flip()

# Main game loop
while True:
    # Represent the current state as a tuple of offsets
    current_state = (
        int(ball_position_x / 10) - int(paddle1_position_y / 10),
        int(ball_position_y / 10),
        int(paddle2_position_y / 10),
        int(ball_velocity_x / abs(ball_velocity_x)),
        int(ball_velocity_y / abs(ball_velocity_y))
    )

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Get Q-values for the current state
    q_values = q_table.get(current_state)
    
    # Initialize new state with random Q-values if not present
    if q_values is None:
        q_table[current_state] = [random.uniform(0, 1) for _ in range(3)]

    # Choose action with the highest Q-value
    chosen_action = q_table[current_state].index(max(q_table[current_state]))

    # Update game state based on the chosen action
    state(chosen_action)

    # Introduce a delay to slow down the decision-making process
    pygame.time.delay(5)  # Adjust the delay time as needed

    # Draw game objects
    draw_display()

# Get new state and update Q-value
new_state = (
    int(ball_position_x / 10) - int(paddle1_position_y / 10),
    int(ball_position_y / 10),
    int(paddle2_position_y / 10),
    int(ball_velocity_x / abs(ball_velocity_x)),
    int(ball_velocity_y / abs(ball_velocity_y))
)

reward = score_left - score_right

# Get new state and update Q-value
new_state = (
    int(ball_position_x / 10) - int(paddle1_position_y / 10),
    int(ball_position_y / 10),
    int(paddle2_position_y / 10),
    int(ball_velocity_x / abs(ball_velocity_x)),
    int(ball_velocity_y / abs(ball_velocity_y))
)

reward = score_left - score_right
q_table[current_state][chosen_action] += learning_rate * (reward + discount_factor * max(q_table[new_state]) - q_table[current_state][chosen_action])

# Limit game to 10 frames per second
clock.tick(10)
