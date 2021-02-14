import pygame
import time
import random

pygame.init()

pygame.mixer.music.load("Behzad Leito & Sijal - Bahatam Dasham (IranTune).mp3")
width = 1350
hight = 850

black = (0,0,0)
red = (200,0,0)
white = (255,255,255)
green =(0,200,0)
bright_green=(0,255,0)
bright_red = (255,0,0)

game_display = pygame.display.set_mode((width,hight))
pygame.display.set_caption("vodo")

clock = pygame.time.Clock()
car_img = pygame.image.load("untitled-2.png")

car_width = 50
def butoon(msg,x,y,w,h,ia,ac,acshin=None):

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y :
        pygame.draw.rect(game_display, ac, (x, y, w, h))
        if click[0] == 1 and acshin != None:
            if acshin == "play":
                game_loop()
            elif acshin == "quit":
                pygame.quit()
                quit()

    else:
        pygame.draw.rect(game_display, ia, (x, y, w, h))
        smallTaxt = pygame.font.Font('freesansbold.ttf', 20)
        TextSurf, TextRect = text_objects(msg, smallTaxt)
        TextRect.center = (x +(w/ 2), y +(50 / 2))
        game_display.blit(TextSurf, TextRect)
        pygame.display.update()
def quitgame():
    pygame.quit()
    quit()

def game_intro():
    intro = True

    while intro :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        game_display.fill(white)
        largeTaxt = pygame.font.Font('freesansbold.ttf', 90)
        TextSurf, TextRect = text_objects("let 's play game", largeTaxt)
        TextRect.center = ((width / 2), (hight / 2))
        game_display.blit(TextSurf, TextRect)

        butoon("play", 150, 450, 100, 50, green, bright_green,"play")
        butoon("quit", 550, 450, 100, 50, red, bright_red,"quit")

        pygame.display.update()


def thing_score (count):
    font = pygame.font.SysFont(None , 25)
    text = font.render("score : "+str(count), True, red)
    game_display.blit(text,(0,0))

def thing (thing_x , thing_y , thing_w , thing_h , color):
    pygame.draw.rect(game_display, color, [thing_x ,thing_y ,thing_w ,thing_h])


def car(x, y):
    game_display.blit(car_img, (x, y))

def text_objects(text,font):
    textSurface = font.render(text,True,black)
    return textSurface, textSurface.get_rect()
def masage_display(text):
    largeTaxt = pygame.font.Font('freesansbold.ttf',105)
    TextSurf, TextRect = text_objects(text,largeTaxt)
    TextRect.center = ((width/2),(hight/2))
    game_display.blit(TextSurf,TextRect)
    pygame.display.update()

    time.sleep(2)
    game_loop()

def crash():
    pygame.mixer.music.stop()
    game_display.fill(white)
    largeTaxt = pygame.font.Font('freesansbold.ttf', 105)
    TextSurf, TextRect = text_objects("you crashed", largeTaxt)
    TextRect.center = ((width / 2), (hight / 2))
    game_display.blit(TextSurf, TextRect)
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        butoon("try again", 150, 450, 100, 50, green, bright_green, "play")
        butoon("quit", 550, 450, 100, 50, red, bright_red, "quit")
        pygame.display.update()

def game_loop():
    pygame.mixer.music.play(-1)

    x = (width * 0.45)
    y = (hight * 0.8)

    x_change = 0

    thing_thing_x = random.randrange(0 ,width)
    thing_thing_y = -600
    thing_speed =7
    thing_width =50
    thing_hight =50

    score = 0

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change


        game_display.fill(white)

        thing_score(score)

        car(x, y)

        if x > width - car_width or x < 0:
                crash()
        if thing_thing_y > hight:
            thing_thing_y = 0 - thing_hight
            thing_thing_x = random.randrange(0, width)
            score += 1

            if (score % 5 == 0):
                thing_speed += 1

        if y < thing_thing_y + thing_hight:

            if x > thing_thing_x and x < thing_thing_x + thing_width or x + car_width > thing_thing_x and x + car_width < thing_thing_x + thing_width:
                crash()

        #thing_x, thing_y, thing_w, thing_h, color
        thing(thing_thing_x ,thing_thing_y ,thing_width ,thing_hight ,red)
        thing_thing_y += thing_speed

        pygame.display.update()
        clock.tick(60)

game_intro()
game_loop()
pygame.quit()
quit()
