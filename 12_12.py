import pygame

pygame.init()
pygame.mixer.init()  # Inicializa o mixer de áudio

pygame.mixer.music.load('oi.mp3')  # Carrega a música
pygame.mixer.music.play()  # Toca a música

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)  # Espera enquanto a música toca
