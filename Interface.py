pygame

class Interface:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("NovaMind AI Interface")

    def display_welcome_message(self):
        font = pygame.font.Font(None, 36)
        text = font.render("Welcome to NovaMind AI Solutions!", True, (255, 255, 255))
        self.screen.blit(text, (100, 100))
        pygame.display.flip()
        pygame.time.wait(2000)
    pygame.quit()