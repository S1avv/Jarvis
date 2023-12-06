import pygame
import random

def play_mp3(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


def play():
    a = ['a', 'b', 'c']
    j = random.choice(a)

    mp3_file_path = "../voice_acting/request_completed_" + j + ".wav"
    play_mp3(mp3_file_path)