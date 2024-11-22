import pygame
import time

pygame.init()

WIDTH=600
HEIGHT=500

#create a screen

screen = pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Birthday card animation") # sets the title of the screen

img = pygame.image.load("backroundone.jpg") # loading the picture from the path and saving ina a variable name



image = pygame.transform.scale(img,(WIDTH,HEIGHT)) # sets the image to the screen's width and height

while True:
    font = pygame.font.SysFont("Lobster",80)
    text = font.render("Happy", True, (255,255,0))
    text2 = font.render("Birthday", True, (255,255,0))

    screen.fill((255,20,147)) # this adds a pink backround colour
    screen.blit(image, (0,0)) # this adds image (backroundone) to the screen

    screen.blit(text,(210,180)) # this adds happy text text on the screen of the given position
    screen.blit(text2,(180,245)) # this adds birthday text text on the screen of the given position

    pygame.display.update()
    time.sleep(2) # this will pause the screen for 2 seconds
    
    img2 = pygame.image.load("backroundtwo.jpg")

    font = pygame.font.SysFont("Lobster",80)
    text3 = font.render("Wish you a", True, (255,255,0))
    text4 = font.render("bright future ahead", True, (255,255,0))

    screen.fill((255,20,147)) # this adds a pink backround colour
    screen.blit(img2, (0,0)) # this adds image (backroundone) to the screen

    screen.blit(text3,(210,180)) # this adds happy text text on the screen of the given position
    screen.blit(text4,(180,245)) # this adds birthday text text on the screen of the given position


    pygame.display.update()
    time.sleep(2)

    img3 = pygame.image.load("backroundthree.jpg")

    screen.fill
    screen.blit(img3, (0,0))

    pygame.display.update()
    time.sleep(2)
