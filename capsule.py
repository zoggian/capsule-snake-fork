import pygame
import random
import pyganim
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()

#Standard color -- todo: dictionary
white = (255, 255, 255)
bg = (103, 244, 251)
purple = (255, 45, 137)
yellow = (255, 180, 0)
red = (255, 89, 118)
orange = (255, 178, 89)
green = (76,  217, 123)
menuRed = (255, 48, 46)
splashBlue = (31, 101, 171)
superYellow = (255, 222, 0)

#Health Bar color progression -- todo: dictionary
healthRed = (255, 89, 118)
healthPink = (255, 89, 171)
healthPink1 = (255, 89, 222)
healthPurple = (218, 89, 255)
healthPurple1 = (187, 89, 255)
healthPurple2 = (144, 89, 255)
healthBlue1 = (89, 89, 255)
healthBlue2 = (89, 152, 255)
healthBlue3 = (89, 198, 255)
healthBlue4 = (89, 253, 255)
healthOrange = (255, 132, 89)
healthOrange1 = (255, 194, 89)
healthYellow = (255, 234, 89)
healthYellow1 = (255, 249, 89)
healthGreen = (187, 255, 89)
healthGreen1 = (132, 255, 89)
healthGreen2 = (0, 255, 54)

#Specify screen h/w
display_width = 800
display_height = 600

#In-game boundry specification
boundary_width = 750
boundary_height = 550

#Master display var
gameDisplay = pygame.display.set_mode((display_width, display_height))

pygame.display.set_caption('CAPSULE: A Snake Fork')

#best size for icon is 32x32.
icon = pygame.image.load('assets/cube.png')
pygame.display.set_icon(icon)


#All available sprites/images/UI -- todo: encap to dictionary?
img = pygame.image.load('assets/snake_head.png')
apple_img = pygame.image.load('assets/cube.png')
instructA = pygame.image.load('assets/wasd_w.png')
instructB = pygame.image.load('assets/arrows_w.png')
instructC = pygame.image.load('assets/space_w.png')
title = pygame.image.load('assets/title.png')
titleInvert = pygame.image.load('assets/title_invert.png')
titleController = pygame.image.load('assets/title_controller.png')
cursor = pygame.image.load('assets/cursor.png')
splash = pygame.image.load('assets/splash.png')
driveTrail = pygame.image.load('assets/drive_trail.png')
block = pygame.image.load('assets/blocky.png')
bgMain = pygame.image.load('assets/bg_main.png')
tapesOne = pygame.image.load('assets/tapes1.png')
tapesTwo = pygame.image.load('assets/tapes2.png')
tapesThree = pygame.image.load('assets/tapes3.png')
tapesFour = pygame.image.load('assets/tapes4.png')
tapesFive = pygame.image.load('assets/tapes5.png')
tapesSix = pygame.image.load('assets/tapes6.png')
tapeSelect = pygame.image.load('assets/tapeSelect.png')
storyPanel = pygame.image.load('assets/story.png')

#Pyganim for opening menu animation
animObj = pyganim.PygAnimation([('assets/Untitled-1.png', 400), ('assets/Untitled-2.png', 500), ('assets/Untitled-3.png', 550)])
animObj.play()

#Controls speed of game
clock = pygame.time.Clock()

#Misc variables determining, you know, the var names
boundaryThickness = 20
appleThickness = 30
block_size = 20
FPS = 30

#Start position of the capsule
direction = "right"

#Font method initialization and available fonts in game
pygame.font.init()
fontPath = "assets/accid__.ttf"
fontPath1 = "assets/big_noodle_titling.ttf"
fontPath2 = "assets/pixel_maz.ttf"

#Available fonts and sizes -- todo: dictionary
smallFont = pygame.font.Font(fontPath1, 15)
small2Font = pygame.font.Font(fontPath1, 17)
smallerFont = pygame.font.Font(fontPath1, 25)
smallishFont = pygame.font.Font(fontPath1, 45)
menuFont = pygame.font.Font(fontPath2, 50)
freemFont = pygame.font.Font(fontPath2, 25)
medFont = pygame.font.SysFont("Arial", 25)
largeFont = pygame.font.Font(fontPath, 50)
superLargeFont = pygame.font.Font(fontPath, 150)

#SFX -- short
splashSound = pygame.mixer.Sound("assets/smw_message_block.wav")
deathSound = pygame.mixer.Sound("assets/death_rattle.ogg")
freemSound = pygame.mixer.Sound("assets/freemGet.ogg")

def pause():
    
    #Pause screen. Look, feel, function.
    
    paused = True

    message_to_screen("PAUSED", yellow, -200, size="large")
    message_to_screen("SELECT A NEW TRACK", white, 175, size="large")


    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = False

        gameDisplay.blit(tapesOne, (235, 150))
        gameDisplay.blit(tapesTwo, (455, 150))
        gameDisplay.blit(tapesThree, (235, 250))
        gameDisplay.blit(tapesFour, (455, 250))
        gameDisplay.blit(tapesFive, (235, 350))
        gameDisplay.blit(tapesSix, (455, 350))

        pauseButton(235, 150, 140, 50, action = "tapeOne")
        pauseButton(455, 150, 140, 50, action = "tapeTwo")
        pauseButton(235, 250, 140, 50, action = "tapeThree")
        pauseButton(455, 250, 140, 50, action = "tapeFour")
        pauseButton(235, 350, 140, 50, action = "tapeFive")
        pauseButton(455, 350, 140, 50, action = "tapeSix")

        pygame.display.update()
        clock.tick(15)

def healthBar(capsuleHealth):
    
    #Controlls the look and feel of the healthbar. Its position, how it progresses, etc.

    #Is this shit loopable? Probably. Figure it out. Encapsulate it in a function or SOMETHING. Looks dirty and gross. DRY.
    if capsuleHealth <= 50:
        capsuleHealth_color = healthRed
    elif capsuleHealth <= 100:
        capsuleHealth_color = healthPink
    elif capsuleHealth <= 150:
        capsuleHealth_color = healthPink1
    elif capsuleHealth <= 200:
        capsuleHealth_color = healthPurple
    elif capsuleHealth <= 250:
        capsuleHealth_color = healthPurple1
    elif capsuleHealth <= 300:
        capsuleHealth_color = healthPurple2
    elif capsuleHealth <= 350:
        capsuleHealth_color = healthBlue1
    elif capsuleHealth <= 400:
        capsuleHealth_color = healthBlue2
    elif capsuleHealth <= 450:
        capsuleHealth_color = healthBlue3
    elif capsuleHealth <= 500:
        capsuleHealth_color = healthBlue4
    elif capsuleHealth <= 550:
        capsuleHealth_color = healthOrange
    elif capsuleHealth <= 600:
        capsuleHealth_color = healthOrange1
    elif capsuleHealth <= 620:
        capsuleHealth_color = healthYellow
    elif capsuleHealth <= 640:
        capsuleHealth_color = healthYellow1
    elif capsuleHealth <= 660:
        capsuleHealth_color = healthGreen
    elif capsuleHealth <= 700:
        capsuleHealth_color = healthGreen1
    else:
        capsuleHealth_color = healthGreen2

    pygame.draw.rect(gameDisplay, capsuleHealth_color, (0, 0, capsuleHealth, 15))

def score(score):

    #Score display only. How score calculates is in the main game loop.

    text = freemFont.render("FREEM LEVELS " + str(score), True, white)
    gameDisplay.blit(text, [355, 1])

def randAppleGen():

    #Random "apple" generator. Get an "apple" and a new one randomly appears within the game boundry.
    
    randAppleX = round(random.randrange(50, boundary_width - appleThickness))
    randAppleY = round(random.randrange(50, boundary_height - appleThickness))

    return randAppleX, randAppleY

def splashScreen():

    #Look and feel of the starting splash screen. Timed.

    startTime = pygame.time.get_ticks()
    splashSound.play(0)

    while pygame.time.get_ticks() < startTime + 2000:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(splashBlue)

        gameDisplay.blit(splash, (200, 250))

        #Todo: Find a aetter way to initialize this. Bug where the menu song starts and stutters.
        pygame.mixer.music.load("assets/menu_muzak.ogg")
        pygame.mixer.music.play(-1)
        pygame.mixer.music.pause()

        pygame.display.update()
        clock.tick(15)

def game_intro():

    #Look and feel for the main menu.

    intro = True

    pygame.mixer.music.unpause()

    while intro:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    intro = False
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load("assets/Platformer2.mp3")
                    gameLoop()


        gameDisplay.fill(bg)

        gameDisplay.blit(title, (-190, 75))

        button("PLAY", 100, 500, 140, 50, cursor, menuRed, action = "play")
        button("CONTROLS", 330, 500, 140, 50, cursor, menuRed, action = "controls")
        button("'STORY'", 570, 500, 140, 50, cursor, menuRed, action = "story")

        animObj.blit(gameDisplay, (250, 240))

        pygame.display.update()
        clock.tick(15)

def snake(block_size, snakeList):

    #Function to reorient the capsule "head" by direction

    if direction == "right":
        head = pygame.transform.rotate(img, 270)
    if direction == "left":
        head = pygame.transform.rotate(img, 90)
    if direction == "up":
        head = img
    if direction == "down":
        head = pygame.transform.rotate(img, 180)
        
    #Code for making the head lead the capsule segments
    gameDisplay.blit(head, (snakeList[-1][0], snakeList[-1][1]))


    #Logic on how the segments function (change direction, trail the head, etc.)
    #Todo: Figure out corner cases. Bug where the drive tail does not align all the time. Looks weird 
    if direction == "right":
        drive = pygame.transform.rotate(driveTrail, 270)
    if direction == "left":
        drive = pygame.transform.rotate(driveTrail, 90)
    if direction == "up":
        drive = driveTrail
    if direction == "down":
        drive = pygame.transform.rotate(driveTrail, 180)

    #Logic for the capsule segments
    for XnY in snakeList[:-1]:
        #pygame.draw.rect(gameDisplay, purple, [XnY[0], XnY[1], block_size, block_size])
        gameDisplay.blit(drive, [XnY[0], XnY[1], block_size, block_size])

def text_objects(text, color, size):

    #Function and parameters for text objects reuse.
    
    if size == "small":
        textSurf = smallFont.render(text, True, color)
    if size == "small2":
        textSurf = small2Font.render(text, True, color)
    elif size == "smaller":
        textSurf = smallerFont.render(text, True, color)
    elif size == "smallish":
        textSurf = smallishFont.render(text, True, color)
    elif size == "menuFont":
        textSurf = menuFont.render(text, True, color)
    elif size == "medium":
        textSurf = medFont.render(text, True, color)
    elif size == "large":
        textSurf = largeFont.render(text, True, color)
    elif size == "superLarge":
        textSurf = superLargeFont.render(text, True, color)
    return textSurf, textSurf.get_rect()

def textToButton(msg, color, buttonX, buttonY, buttonWidth, buttonHeight, size="small2"):

    #Button UI
    
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonX + buttonWidth/2), (buttonY + buttonHeight/2))
    gameDisplay.blit(textSurf, textRect)


def message_to_screen(msg, color, y_displace=0, size = "small"):

    #Determines how non-blit images and messages are displayed.
    
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (display_width/2), (display_height/2) + y_displace
    gameDisplay.blit(textSurf, textRect)


def gameControls():

    #Screen for game controls

    gameCont = True

    while gameCont:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_intro()

        gameDisplay.fill(yellow)

        gameDisplay.blit(titleController, (-190, 75))

        button("PLAY", 100, 500, 140, 50, cursor, menuRed, action = "play")
        button("CONTROLS", 330, 500, 140, 50, cursor, white, action = "controls")
        button("'STORY'", 570, 500, 140, 50, cursor, menuRed, action = "story")

        gameDisplay.blit(instructA, (195, 330))
        gameDisplay.blit(instructB, (515, 330))
        gameDisplay.blit(instructC, (320, 366))

        message_to_screen("<= move w/ either of these =>", white, 20, "smaller")

        pygame.display.update()
        clock.tick(15)

def gameStories():

    #Screen for instructions aka game story

    gameStor = True

    while gameStor:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_intro()

        gameDisplay.fill(purple)

        gameDisplay.blit(titleInvert, (-190, 75))
        gameDisplay.blit(storyPanel, (100, 240))

        button("PLAY", 100, 500, 140, 50, cursor, white, action = "play")
        button("CONTROLS", 330, 500, 140, 50, cursor, white, action = "controls")
        button("'STORY'", 570, 500, 140, 50, cursor, yellow, action = "story")

        pygame.display.update()
        clock.tick(15)

def button(text, x, y, width, height, activeColor, textColor, action=None, size = "menuFont"):

    #Button logic. Where to click, how click is detected, how click is registered and directed.
    
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        gameDisplay.blit(cursor, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "intro":
                game_intro()
            if action == "controls":
                gameControls()
            if action == "play":
                pygame.mixer.music.stop()
                pygame.mixer.music.load("assets/Platformer2.mp3")
                gameLoop()
            if action == "story":
                gameStories()

    textToButton(text, textColor, x, y, width, height, size="menuFont")

def pauseButton (x, y, width, height, action=None):

    #UI and UX for the pause menu music selection buttons
    
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + width > cur[0] > x and y + height > cur[1] > y:
        gameDisplay.blit(tapeSelect, (x, y, width, height))
        if click[0] == 1 and action != None:
            if action == "tapeOne":
                pygame.mixer.music.stop()
                pygame.mixer.music.load("assets/menu_muzak.ogg")
                pygame.mixer.music.play(-1)
            if action == "tapeTwo":
                pygame.mixer.music.stop()
                pygame.mixer.music.load("assets/crazybus.ogg")
                pygame.mixer.music.play(-1)
            if action == "tapeThree":
                pygame.mixer.music.stop()
                pygame.mixer.music.load("assets/Platformer2.mp3")
                pygame.mixer.music.play(-1)
            if action == "tapeFour":
                pygame.mixer.music.stop()
                pygame.mixer.music.load("assets/helixNebula.ogg")
                pygame.mixer.music.play(-1)
            if action == "tapeFive":
                pygame.mixer.music.stop()
                pygame.mixer.music.load("assets/anaconda.ogg")
                pygame.mixer.music.play(-1)
            if action == "tapeSix":
                pygame.mixer.music.stop()
                pygame.mixer.music.load("assets/seaOfLove.ogg")
                pygame.mixer.music.play(-1)

def loadMap (fileName):

    #Function to load level design from a text file.
    
    f = open(fileName)
    content = f.readlines()
    f.close()

    return content

def drawWalls (surface, img, map):

    #Companion function to loadMap. Determines HOW the map is created from the text file.
    
    row = 0
    for line in map:
        col = 0
        for char in line:
            if (char == '1'):
                imgRect = img.get_rect()
                imgRect.left = col * 14
                imgRect.top = row * 14
                gameDisplay.blit(block, imgRect)
            col += 1
        row += 1

def winCondition():

    #The very stupid and uneventful screen that happens when you win this impossible game. Spoiler alert.
    
    winning = True

    while winning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_intro()

        pygame.mixer.music.stop()
        gameDisplay.fill(splashBlue)

        message_to_screen("Contgratulatoin. You mad to Litspede! 8,000 punts to Gryffindor!", superYellow, -25, "smaller")
        message_to_screen("Mostly Coded by Ian Cho", white, 50, "smaller")
        message_to_screen("Graphics: Ian Cho", white, 75, "smaller")
        message_to_screen("Music: Anamanaguchi, PBS' Arthur, dl-sounds.com, SNES' Earthbound, TimeSplitters, The National", white, 100, "smaller")
        message_to_screen("(C) The Galactic Crayon", superYellow, 250, "small")

        pygame.display.update()
        clock.tick(15)

def gameLoop():

    #All the game logic.

    global direction

    direction = 'right'

    gameExit = False
    gameOver = False

    lead_x = display_width/2
    lead_y = display_height/2

    lead_x_change = 0
    lead_y_change = 0

    capsuleHealth = 0

    snakeList = []
    snakeLength = 1

    randAppleX, randAppleY = randAppleGen()

    pygame.mixer.music.play(-1)

    while not gameExit:

        #Game over logic

        if gameOver == True:

            message_to_screen("GAME OVER",
                              menuRed, -25,
                              size = "superLarge")

            message_to_screen("[SPACEBAR] to try again             or            [E] for Title Screen",
                              white, 150,
                              size = "small")

            pygame.mixer.music.stop()
            deathSound.play(0)
            pygame.display.update()


        while gameOver == True:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        gameLoop()
                    elif event.key == pygame.K_e:
                        game_intro()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    direction = "left"
                    lead_x_change = -block_size
                    #prevents diagonal
                    lead_y_change = 0
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    direction = "right"
                    lead_x_change = block_size
                    #prevents diagonal
                    lead_y_change = 0
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    direction = "up"
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    direction = "down"
                    lead_y_change = block_size
                    lead_x_change = 0
                elif event.key == pygame.K_SPACE:
                    pause()


            #Collision for the boundaries. Cross and you die. Not the best. Must recode.
            if lead_x >= boundary_width or lead_x < 25 or lead_y >= boundary_height or lead_y < 25:
                gameOver = True

            if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y < 0:
                gameOver = True

        #Change these for easier win.         
        if capsuleHealth >= 800:
            winCondition()

        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.blit(bgMain,(0, 0))

        #pygame.draw.rect(gameDisplay, purple, [25, 25, boundary_width, boundary_height], 5 )
        snakeMap = loadMap('assets/map.txt')
        drawWalls(gameDisplay, block, snakeMap)

        #collision boundary code
        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, appleThickness, appleThickness])
        gameDisplay.blit(apple_img, (randAppleX, randAppleY))

        healthBar(capsuleHealth)

        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        if len(snakeList) > snakeLength:
            del snakeList[0]

        for eachSegment in snakeList[:-1]:
            if eachSegment == snakeHead:
                del snakeList[0]
                capsuleHealth -= 10
                snakeLength -= 1

        #How the game speeds up with each "apple" get. This is a fucking mess. Todo: encapsulate into a function/loop:
        if capsuleHealth <= 10:
            clock.tick(20)
        elif capsuleHealth <= 20:
            clock.tick(20.5)
        elif capsuleHealth <= 30:
            clock.tick(21)
        elif capsuleHealth <= 40:
            clock.tick(21.5)
        elif capsuleHealth <= 50:
            clock.tick(22)
        elif capsuleHealth <= 60:
            clock.tick(22.5)
        elif capsuleHealth <= 70:
            clock.tick(23)
        elif capsuleHealth <= 80:
            clock.tick(23.5)
        elif capsuleHealth <= 90:
            clock.tick(24)
        elif capsuleHealth <= 100:
            clock.tick(24.5)
        elif capsuleHealth <= 110:
            clock.tick(25)
        elif capsuleHealth <= 120:
            clock.tick(25.5)
        elif capsuleHealth <= 130:
            clock.tick(26)
        elif capsuleHealth <= 140:
            clock.tick(26.5)
        elif capsuleHealth <= 150:
            clock.tick(27)
        elif capsuleHealth <= 160:
            clock.tick(27.5)
        elif capsuleHealth <= 170:
            clock.tick(28)
        elif capsuleHealth <= 180:
            clock.tick(28.5)
        elif capsuleHealth <= 190:
            clock.tick(29)
        elif capsuleHealth <= 200:
            clock.tick(29.5)
        elif capsuleHealth <= 210:
            clock.tick(30)
        elif capsuleHealth <= 220:
            clock.tick(30.5)
        elif capsuleHealth <= 230:
            clock.tick(31)
        elif capsuleHealth <= 240:
            clock.tick(31.5)
        elif capsuleHealth <= 250:
            clock.tick(32)
        elif capsuleHealth <= 260:
            clock.tick(32.5)
        elif capsuleHealth <= 270:
            clock.tick(33)
        elif capsuleHealth <= 280:
            clock.tick(33.5)
        elif capsuleHealth <= 290:
            clock.tick(34)
        elif capsuleHealth <= 300:
            clock.tick(34.5)
        elif capsuleHealth <= 310:
            clock.tick(35)
        elif capsuleHealth <= 320:
            clock.tick(35.5)
        elif capsuleHealth <= 330:
            clock.tick(36)
        elif capsuleHealth <= 340:
            clock.tick(36.5)
        elif capsuleHealth <= 350:
            clock.tick(37)
        elif capsuleHealth <= 360:
            clock.tick(37.5)
        elif capsuleHealth <= 370:
            clock.tick(38)
        elif capsuleHealth <= 380:
            clock.tick(38.5)
        elif capsuleHealth <= 390:
            clock.tick(39)
        elif capsuleHealth <= 400:
            clock.tick(39.5)
        elif capsuleHealth <= 420:
            clock.tick(40)
        elif capsuleHealth <= 440:
            clock.tick(41)
        elif capsuleHealth <= 460:
            clock.tick(42)
        elif capsuleHealth <= 480:
            clock.tick(43)
        elif capsuleHealth <= 500:
            clock.tick(44)
        elif capsuleHealth <= 520:
            clock.tick(45)
        elif capsuleHealth <= 540:
            clock.tick(46)
        elif capsuleHealth <= 560:
            clock.tick(47)
        elif capsuleHealth <= 580:
            clock.tick(48)
        elif capsuleHealth <= 590:
            clock.tick(49)
        elif capsuleHealth <= 600:
            clock.tick(50)
        elif capsuleHealth <= 650:
            clock.tick(55)
        else:
            clock.tick(60)

        snake(block_size, snakeList)
        score(snakeLength - 1)
        pygame.display.update()

        #Logic for how the "apple" is got and what happens after the "apple" is got.
        if lead_x > randAppleX and lead_x < randAppleX + appleThickness or lead_x + appleThickness > randAppleX and lead_x + appleThickness < randAppleX + appleThickness:
            if lead_y > randAppleY and lead_y < randAppleY + appleThickness or lead_y + appleThickness > randAppleY and lead_y + appleThickness < randAppleY + appleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1
                freemSound.play()
                capsuleHealth += 10
                
    #This quits the game.
    pygame.quit()
    quit()

splashScreen()
game_intro()
gameLoop()
