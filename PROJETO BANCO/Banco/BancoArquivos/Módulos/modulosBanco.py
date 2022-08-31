import os
import random
from random import randint
from time import sleep
from BancoArquivos.Módulos.colors import *
from BancoArquivos.Módulos.funs import *
import datetime
import pygame


def clean():
    os.system("Cls")


def music(mp3):
    pygame.init()
    pygame.mixer.music.load(f'{mp3}')
    pygame.mixer.music.play()

