import pygame
import os
import time

pygame.init()
caminho_musica = os.path.expanduser('~/Músicas/tesla.mp3')
pygame.mixer.init()
pygame.mixer.music.load(caminho_musica)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    time.sleep(1)
