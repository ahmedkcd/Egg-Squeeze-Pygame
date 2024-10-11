import pygame
import sys
from StopWatch import StopWatch

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

        self.watch =  StopWatch()
        self.targetTime = 4.5
        self.scoreRatio = 0;
        self.egg_inflated = False
        self.egg_inflating = True
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.cursor_rectangle.colliderect(self.egg):
                        self.watch.startWatch()
                        print("Hold this egg!")
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.watch.running:
                        self.watch.stopWatch()
                        print(self.watch.returnTotalTime())
                        self.scoreRatio = (self.watch.returnTotalTime() / self.targetTime) * 100
                        
                        if(self.watch.returnTotalTime() > self.targetTime):
                            print("You broke the egg! " + "%.2f" % (self.scoreRatio) + "%")


                if self.cursor_rectangle.colliderect(self.egg):
                    if(not self.egg_inflated):
                        self.egg.inflate_ip(10, 10)
                    self.egg_inflated = True
                else:
                    if(self.egg_inflated):
                        self.egg.inflate_ip(-10, -10)
                        self.egg_inflated = False

            self.current_time = pygame.time.get_ticks()
            
            
            self.display.fill((0, 5, 0)) # Fill display each time
            pygame.draw.rect(self.display, "white", self.egg)
            pygame.draw.rect(self.display, "yellow", self.cursor_rectangle)
            self.cursor_rectangle.update((pygame.mouse.get_pos()[0]/2, pygame.mouse.get_pos()[1]/2), (16, 16)) # Move the mouse rectangle to the mouse pos

            

            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.update()


            
            self.clock.tick(60)

    def start_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        Game.run(self)

            print("Welcome to the Egg Squeeze! Press space to begin.")

        self.display.fill(0, 5, 0)
        self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
        pygame.display.update()

    def loss_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            
        
        
Game().start_screen()      


