import pygame
import sys

#Created off of example from Benjamin Widener

class Game:
    def __init__(self):
        pygame.init() #Initiate game

        pygame.display.set_caption('Egg Squeeze') #Name

        scr_res = (640, 480)
        self.screen = pygame.display.set_mode(scr_res)

        self.display = pygame.Surface((320, 240))
        
        self.egg = pygame.Rect(130, 60, 50, 70)
        self.cursor_rectangle = pygame.Rect(0, 0, 0, 0)

        self.clock = pygame.time.Clock()        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.cursor_rectangle.colliderect(self.egg):
                        print("stop touching this egg!")
            
            self.display.fill((0, 5, 0)) # Fill display each time
            pygame.draw.rect(self.display, "white", self.egg)
            pygame.draw.rect(self.display, "yellow", self.cursor_rectangle)
            self.cursor_rectangle.update((pygame.mouse.get_pos()[0]/2, pygame.mouse.get_pos()[1]/2), (16, 16)) # Move the mouse rectangle to the mouse pos

            

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.update()


            
            self.clock.tick(60)
        
Game().run()      


