import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()
font = pygame.font.Font('./fonts/arial.ttf', 25)
game_over_font = pygame.font.Font('./fonts/game_over_font.ttf', 70)
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y') 

WHITE = (255, 255, 255)
FOODCOLOR = (200, 0, 0)
SNAKECOLOR1 = (50, 50, 255)
SNAKECOLOR2 = (150, 150, 255)
BGCOLOR = (0, 20, 25)

BLOCK_SIZE = 20
SPEED = 5

class SnakeGame:
    def __init__(self, w=800, h=800):
        self.w = w
        self.h = h
        self.display = pygame.display.set_mode((self.w, self.h))
        pygame.display.set_caption('Snake')
        self.clock = pygame.time.Clock()
        self.direction = Direction.RIGHT
        self.head = Point(self.w / 2, self.h / 2)
        self.snake = [self.head, Point(self.head.x - BLOCK_SIZE, self.head.y), Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]
        self.score = 0
        self.food = None
        self._place_food()
        self.game_over = False

    def _place_food(self):
        x = random.randint(0, (self.w - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        y = random.randint(0, (self.h - BLOCK_SIZE) // BLOCK_SIZE) * BLOCK_SIZE
        self.food = Point(x, y)
        if self.food in self.snake:
            self._place_food()

    def play_step(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.direction != Direction.RIGHT:
                    self.direction = Direction.LEFT
                elif event.key == pygame.K_RIGHT and self.direction != Direction.LEFT:
                    self.direction = Direction.RIGHT
                elif event.key == pygame.K_UP and self.direction != Direction.DOWN:
                    self.direction = Direction.UP
                elif event.key == pygame.K_DOWN and self.direction != Direction.UP:
                    self.direction = Direction.DOWN
                elif event.key == pygame.K_r and self.game_over:
                    self.restart_game()

        if not self.game_over:
            self._move(self.direction)
            self.snake.insert(0, self.head)

            if self._is_collision():
                self.game_over = True

            if self.head == self.food:
                self.score += 1
                self._place_food()
            else:
                self.snake.pop()

            self._update_ui()
            self.clock.tick(SPEED)

        return self.game_over, self.score

    def _is_collision(self):
        if self.head.x > self.w - BLOCK_SIZE or self.head.x < 0 or self.head.y > self.h - BLOCK_SIZE or self.head.y < 0:
            return True
        if self.head in self.snake[1:]:
            return True
        return False

    def _update_ui(self):
        self.display.fill(BGCOLOR)
        for pt in self.snake:
            pygame.draw.rect(self.display, SNAKECOLOR1, pygame.Rect(pt.x, pt.y, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.display, SNAKECOLOR2, pygame.Rect(pt.x + 4, pt.y + 4, 12, 12))
        pygame.draw.rect(self.display, FOODCOLOR, pygame.Rect(self.food.x, self.food.y, BLOCK_SIZE, BLOCK_SIZE))

        if self.game_over:
            self._show_game_over_screen()
        else:
            text = font.render("Score: " + str(self.score), True, WHITE)
            self.display.blit(text, [0, 0])

        pygame.display.flip()

    def _move(self, direction):
        x = self.head.x
        y = self.head.y
        if direction == Direction.RIGHT:
            x += BLOCK_SIZE
        elif direction == Direction.LEFT:
            x -= BLOCK_SIZE
        elif direction == Direction.DOWN:
            y += BLOCK_SIZE
        elif direction == Direction.UP:
            y -= BLOCK_SIZE
        self.head = Point(x, y)

    def _show_game_over_screen(self):
        
        game_over_text = game_over_font.render("Game Over!", True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(self.w // 2, self.h // 2 - 100))
        self.display.blit(game_over_text, game_over_rect)

        score_text = font.render("Your Score: " + str(self.score), True, WHITE)
        score_rect = score_text.get_rect(center=(self.w // 2, self.h // 2))
        self.display.blit(score_text, score_rect)

        restart_text = font.render("Press R to Restart", True, WHITE)
        restart_rect = restart_text.get_rect(center=(self.w // 2, self.h // 2 + 50))
        self.display.blit(restart_text, restart_rect)



    def restart_game(self):
        self.direction = Direction.RIGHT
        self.head = Point(self.w / 2, self.h / 2)
        self.snake = [self.head, Point(self.head.x - BLOCK_SIZE, self.head.y), Point(self.head.x - (2 * BLOCK_SIZE), self.head.y)]
        self.score = 0
        self._place_food()
        self.game_over = False

if __name__ == '__main__':
    game = SnakeGame()

    while True:
        game_over, score = game.play_step()

        if game_over:
            pygame.display.flip()  # Update display to show game over screen
            pygame.time.wait(500)  # Wait for a short time to prevent instant restart if 'R' key is held down
