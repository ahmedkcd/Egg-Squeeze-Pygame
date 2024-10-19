import pygame
import sys
from StopWatch import StopWatch
from scripts.utilities import load_music, load_sound, load_image, load_images

#Created off of example from Benjamin Widener
class Game:
    timesPlayed = 0
    timesSqueezed = 0
    timesCracked = 0
    def __init__(self):
        pygame.init() #Initiate game

        pygame.display.set_caption('Egg Squeeze') #Name

        scr_res = (640, 480)
        self.screen = pygame.display.set_mode(scr_res)

        self.display = pygame.Surface((320, 240))

        self.egg_image_org = load_image('eggs/egg.png')
        self.egg_image = load_image('eggs/egg.png')
        self.cracked_egg_image = pygame.transform.scale(load_image('eggs/cracked_egg.png'), (60, 80))
        #self.egg = pygame.Rect(130, 60, 50, 70)
        self.egg = self.egg_image.get_rect().move(130, 120)
        self.cursor_rectangle = pygame.Rect(0, 0, 0, 0)
        #self.splash_text = SplashText() Random texts

        self.clock = pygame.time.Clock()

        self.watch =  StopWatch()
        self.times = [4.5, 6.3, 2.5, 8, 5] # Random times to use as target times
        self.targetTime = self.times[Game.timesPlayed % 5]
        self.scoreRatio = 0;
        self.egg_inflated = False
        self.egg_inflating = True

        self.splash_texts = [" EGGS SQUEEZED: " + str(Game.timesSqueezed) + " EGGS", "Don't squeeze me I'm scared", "What's the deal with eggs?", "This is an egg", "DONT LET GO "]
        
        self.crack_sound_effect = load_sound('egg_cracking.mp3')
        self.music_track = load_music('wheel_fortune.mp3')
        self.victory_sound_effect = load_sound('ff7_victory.mp3')

        self.font = pygame.font.SysFont("comicsansms", 20)
        self.welcome = self.font.render("Press space to take a crack at it", True, "white")
        self.cracked_text = self.font.render("You cracked the egg :(", True, "white")
        self.winner_text = self.font.render("Winner winner no chicken dinner!", True, "white")
        self.try_again_text = self.font.render("Press space again or beat it.", True, "white")
        
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.cursor_rectangle.colliderect(self.egg):
                        self.watch.startWatch()
                        print("Hold this egg!")
                        Game.timesSqueezed = Game.timesSqueezed + 1
                        self.splash_texts[0] = "  EGGS SQUEEZED: " + str(Game.timesSqueezed) + " EGGS."
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.watch.running:
                        self.watch.stopWatch()
                        print("%.2f" % (self.watch.returnTotalTime()) + " / " + "%.2f" % (self.targetTime))
                        self.scoreRatio = (self.watch.returnTotalTime() / self.targetTime) * 100
                        
                        if(self.watch.returnTotalTime() > self.targetTime):
                            self.crack_sound_effect.play()
                            print("You broke the egg! " + "%.2f" % (self.scoreRatio) + "%")
                            Game.timesPlayed = Game.timesPlayed + 1
                            Game.timesCracked = Game.timesCracked + 1
                            self.targetTime = self.times[Game.timesPlayed % 5] # New time to beat
                            Game().loss_screen()
                        if(self.scoreRatio > 50 and self.scoreRatio <= 99.99): #Get at least 50% to "win"
                            Game.timesPlayed = Game.timesPlayed + 1
                            self.targetTime = self.times[Game.timesPlayed % 5] # New time to beat
                            self.victory_sound_effect.play()
                            Game().victory_screen()
                            



                
                if self.cursor_rectangle.colliderect(self.egg):
                    if(not self.egg_inflated):
                        self.egg.inflate_ip(10, 10)
                        self.egg_inflated = True
                        self.egg_image = pygame.transform.scale(self.egg_image_org, (60, 80))
                else:
                    if(self.egg_inflated):
                        self.egg.inflate_ip(-10, -10)
                        self.egg_inflated = False
                        self.egg_image = pygame.transform.scale(self.egg_image_org, (50, 70))
            self.current_time = pygame.time.get_ticks()
            

            self.display.fill((0, 5, 0)) # Fill display each time

            #pygame.draw.rect(self.display, "white", self.egg)
            if(self.watch.running):
                self.display.blit(self.font.render(self.splash_texts[Game.timesPlayed % 3], True, "red"), (10, 60))
            self.display.blit(self.egg_image, (130, 120))
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
                        pygame.mixer.music.play(-1)
                        Game.run(self)

            self.display.fill((0, 10, 0)) # Fill display each time
            self.display.blit(self.welcome, (10, 185))


            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.update()
            self.clock.tick(60)

    def loss_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pygame.mixer.music.play()
                        Game.run(self)

            self.display.fill((0, 6, 0)) # Fill display each time
            self.display.blit(self.cracked_text, (45, 60))
            self.display.blit(self.try_again_text, (30, 200))

            self.display.blit(self.cracked_egg_image, (130, 120))
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.update()
            self.clock.tick(60)
    def victory_screen(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.victory_sound_effect.stop()
                        pygame.mixer.music.play()
                        Game.run(self)

            self.display.fill((0, 6, 0)) # Fill display each time
            self.display.blit(self.winner_text, (7, 60))
            self.display.blit(self.try_again_text, (35, 200))

            self.display.blit(pygame.transform.scale(self.egg_image_org, (60, 80)), (130, 120))
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            pygame.display.update()
            self.clock.tick(60)
            
        
        
Game().start_screen()


