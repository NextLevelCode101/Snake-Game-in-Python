import pygame
import random
# Initialize Pygame
pygame.init()
# Set up display
WIDTH, HEIGHT = 600, 600
BLOCK_SIZE = 20
GRID_WIDTH, GRID_HEIGHT = WIDTH // BLOCK_SIZE, HEIGHT // BLOCK_SIZE
BG_COLOR = (0, 0, 0)
FOOD_COLOR = (255, 0, 0)
SNAKE_COLOR = (0, 255, 0)
GRID_COLOR = (50, 50, 50)
FONT_COLOR = (255, 255, 255)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
# Define directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
# Snake class
class Snake:
def __init__(self):
self.length = 1
self.positions = [((GRID_WIDTH // 2) * BLOCK_SIZE, (GRID_HEIGHT // 2) *
BLOCK_SIZE)]
self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
self.color = SNAKE_COLOR
def get_head_position(self):
return self.positions[0]
def move(self):
cur = self.get_head_position()
x, y = self.direction
new = (((cur[0] + (x * BLOCK_SIZE)) % WIDTH), (cur[1] + (y *
BLOCK_SIZE)) % HEIGHT)
if len(self.positions) > 2 and new in self.positions[2:]:
return True
else:
self.positions.insert(0, new)
if len(self.positions) > self.length:
self.positions.pop()
return False
def reset(self):
self.length = 1
BLOCK_SIZE)]
self.positions = [((GRID_WIDTH // 2) * BLOCK_SIZE, (GRID_HEIGHT // 2) *
self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
def draw(self, surface):
for p in self.positions:
r = pygame.Rect((p[0], p[1]), (BLOCK_SIZE, BLOCK_SIZE))
pygame.draw.rect(surface, self.color, r)
pygame.draw.rect(surface, BG_COLOR, r, 1)
def handle_keys(self, keys):
if keys[pygame.K_UP] and self.direction != DOWN:
self.direction = UP
elif keys[pygame.K_DOWN] and self.direction != UP:
self.direction = DOWN
elif keys[pygame.K_LEFT] and self.direction != RIGHT:
self.direction = LEFT
elif keys[pygame.K_RIGHT] and self.direction != LEFT:
self.direction = RIGHT
# Food class
class Food:
def __init__(self):
self.position = (0, 0)
self.color = FOOD_COLOR
self.randomize_position()
def randomize_position(self):
self.position = (random.randint(0, GRID_WIDTH - 1) * BLOCK_SIZE,
random.randint(0, GRID_HEIGHT - 1) * BLOCK_SIZE)
def draw(self, surface):
r = pygame.Rect((self.position[0], self.position[1]), (BLOCK_SIZE,
BLOCK_SIZE))
pygame.draw.rect(surface, self.color, r)
pygame.draw.rect(surface, BG_COLOR, r, 1)
# Draw grid
def draw_grid(surface):
for x in range(0, WIDTH, BLOCK_SIZE):
pygame.draw.line(surface, GRID_COLOR, (x, 0), (x, HEIGHT))
for y in range(0, HEIGHT, BLOCK_SIZE):
pygame.draw.line(surface, GRID_COLOR, (0, y), (WIDTH, y))
# Draw start screen
def draw_start_screen(surface):
title_font = pygame.font.Font(None, 50)
title_text = title_font.render("Snake Game", True, FONT_COLOR)
title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
button_font = pygame.font.Font(None, 30)
button_text = button_font.render("Play", True, FONT_COLOR)
button_rect = button_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
surface.blit(title_text, title_rect)
surface.blit(button_text, button_rect)
pygame.draw.rect(surface, FONT_COLOR, button_rect, 1)
# Draw victory screen
def draw_victory_screen(surface):
victory_font = pygame.font.Font(None, 50)
victory_text = victory_font.render("You Win!", True, FONT_COLOR)
victory_rect = victory_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
surface.blit(victory_text, victory_rect)
# Draw score
def draw_score(surface, score):
score_font = pygame.font.Font(None, 30)
score_text = score_font.render(f"Score: {score}", True, FONT_COLOR)
score_rect = score_text.get_rect(topright=(WIDTH - 20, 20))
surface.blit(score_text, score_rect)
# Main function
def main():
start_screen = True
game_running = False
while start_screen:
screen.fill(BG_COLOR)
draw_start_screen(screen)
pygame.display.update()
for event in pygame.event.get():
if event.type == pygame.QUIT:
start_screen = False
elif event.type == pygame.MOUSEBUTTONDOWN:
if event.button == 1: # Left mouse button
x, y = event.pos
button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT // 2 - 20,
100, 40)
if button_rect.collidepoint(x, y):
game_running = True
start_screen = False
if game_running:
snake = Snake()
food = Food()
score = 0
running = True
while running:
screen.fill(BG_COLOR)
draw_grid(screen)
snake.handle_keys(pygame.key.get_pressed())
# Check if snake collides with itself or edges
if snake.move() or snake.get_head_position()[0] < 0 or
snake.get_head_position()[0] >= WIDTH or snake.get_head_position()[1] < 0 or
snake.get_head_position()[1] >= HEIGHT:
running = False
# Check if snake eats food
if snake.get_head_position() == food.position:
snake.length += 1
food.randomize_position()
score += 1
# Draw elements
snake.draw(screen)
food.draw(screen)
draw_score(screen, score)
pygame.display.update()
clock.tick(10)
# Check for victory condition
if score >= 50:
running = False
screen.fill(BG_COLOR)
draw_victory_screen(screen)
pygame.display.update()
pygame.time.delay(2000) # Delay for 2 seconds before quitting
# Event handling
for event in pygame.event.get():
if event.type == pygame.QUIT:
running = False
pygame.quit()
if __name__ == "__main__":
main()
