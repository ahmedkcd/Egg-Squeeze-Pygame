import pygame
import os

BASE_IMG_PATH = 'data/images/'
BASE_SOUND_PATH = 'data/sounds/'

def load_image(path):
    img = pygame.image.load(BASE_IMG_PATH + path).convert()
    img.set_colorkey((237,0,237))
    return img

def load_images(path):
    images = []
    for img_name in os.listdir(BASE_IMG_PATH + path):
        images.append(load_image(path + '/' + img_name))
    return images

def load_sound(path):
    sound = pygame.mixer.Sound(BASE_SOUND_PATH + path)
    return sound

def load_music(path):
    music = pygame.mixer.music.load(BASE_SOUND_PATH + path)
    return music

