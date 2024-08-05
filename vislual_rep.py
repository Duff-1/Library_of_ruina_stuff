import glob, pygame
from pygame.locals import *
pygame.init()
pygame.font.init()

pages = []

for filepath in glob.iglob('pages/*.txt'):
    pages.append(filepath)



# Aspects
BACKGROUND = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
FONT = pygame.font.SysFont('Arial', 20)
BLACK = (255,255,255)

# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400

WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Game')

class button: # Interactive buttons on the menus

    def __init__(self, pos, text, path): # Creates a button
        self.pos = pos # Button postion
        self.text = text # Display text on the button
        self.text_render = FONT.render(self.text, 1, BLACK) # Render for the text
        x, y, self.w , self.h = self.text_render.get_rect() # Size of the button
        self.hitbox = pygame.Rect(pos, [self.w, self.h]) # Hitbox for the button
    
    def display(self): # Displays a button
        x, y = self.pos
        w = self.w
        h = self.h
        pygame.draw.line(WINDOW, (150, 150, 150), (x, y), (x + w , y), 5)
        pygame.draw.line(WINDOW, (150, 150, 150), (x, y - 2), (x, y + h), 5)
        pygame.draw.line(WINDOW, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
        pygame.draw.line(WINDOW, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
        if self.hitbox.collidepoint(pygame.mouse.get_pos()): # Button has different responses when touching mouse
            if pygame.mouse.get_pressed()[0] == True: # On click
            pygame.draw.rect(WINDOW, (50, 50, 50), (x, y, w , h))
            else: # On hover
            pygame.draw.rect(WINDOW, (150, 150, 150), (x, y, w , h))
        else: # When not touching mouse
            pygame.draw.rect(WINDOW, (100, 100, 100), (x, y, w , h))
        return WINDOW.blit(self.text_render, (x, y))

def text_blit(words, colour, x, y):
    text = FONT.render(words, True, colour)
    pos = text.get_rect( centerx=x, centery=y )
    WINDOW.blit(text, pos)

def main():
    buttons = []
    scroll_max = len(pages)*30 if len(pages) > len(pages) else len(pages)*20
    scroll_value = 0

    while True:
        WINDOW.fill((255,255,255))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        
            if event.type == pygame.MOUSEWHEEL:
                if event.y == 1:
                    scroll_value -= 10 if scroll_value > 0 else 0
                elif event.y == -1:
                    scroll_value += 10 if scroll_value < scroll_max else 0


        for i,page in enumerate(pages):
            temp = page.removeprefix("pages\ ".removesuffix(" "))
            temp = temp.removesuffix(".txt")
            buttons.append(button((100, (25*i + 10) - scroll_value),temp,page))
            text_blit(temp,(0,0,0), 100, (25*i + 10) - scroll_value)

        
        pygame.display.update()
        fpsClock.tick(FPS)
        buttons = []

main()