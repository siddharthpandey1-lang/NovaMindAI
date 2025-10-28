import pygame

class Interface:
    def __init__(self):
        self.WIDTH = 800
        self.HEIGHT = 600
        pygame.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("NovaMind AI Interface")
        self.running = True

    def display_welcome_message(self):
        font = pygame.font.Font(None, 36)
        text = font.render("Welcome to NovaMind AI Solutions!", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.WIDTH // 2, self.HEIGHT // 2))
        self.screen.fill((0, 0, 0))  # Clear screen with black background
        self.screen.blit(text, text_rect)
        pygame.display.flip()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            self.display_welcome_message()
            pygame.time.delay(100)  # Add a small delay to prevent high CPU usage

        pygame.quit()