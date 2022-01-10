import pygame
import config as c
import robot
import cards

pygame.init()

"""
windowSize = [700, 700]
background = (76, 255, 51)
black = (0, 0, 0)
Font = pygame.font.SysFont('Calibri', 32, False, False)
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption('RoboRally')
gameBoard = pygame.image.load('graphics/2016doodle.jpg')
"""

robot1 = robot.Robot('UR', 0, 0)
robot1.img = pygame.image.load('graphics/UR1.png')
robot2 = robot.Robot('UB', 0, 46)
robot2.img = pygame.image.load('graphics/UB1.png')
whitePic = pygame.image.load('graphics/white.png')
"c.screen.fill(c.background)"
card1T = cards.d.printCard()
card2T = cards.d.printCard()
card3T = cards.d.printCard()
card4T = cards.d.printCard()
card5T = cards.d.printCard()
card1 = pygame.font.Font.render(c.Font,str(card1T),True, c.black)
card2 = pygame.font.Font.render(c.Font,str(card2T),True, c.black)
card3 = pygame.font.Font.render(c.Font,str(card3T),True, c.black)
card4 = pygame.font.Font.render(c.Font,str(card4T),True, c.black)
card5 = pygame.font.Font.render(c.Font,str(card5T),True, c.black)
"""
pygame.draw.line(c.screen, c.black, [135,460], [135,695],3)
pygame.draw.line(c.screen, c.black, [273,460], [273,695],3)
pygame.draw.line(c.screen, c.black, [411,460], [411,695],3)
pygame.draw.line(c.screen, c.black, [549,498], [549,695],3)
pygame.draw.line(c.screen, c.black, [0,498], [700, 498],3)
"""
"Screen blit shit"
c.screen.blit(c.gameBoard, (0, 0))
c.screen.blit(robot1.img, (robot1.x, robot1.y))
c.screen.blit(robot2.img, (robot2.x, robot2.y))
"card 1"
c.screen.blit(card1, dest = (20,500))
c.screen.blit(c.ONE, dest = (50, 600))
cards.o.addToHand(card1T)
"card 2"
c.screen.blit(card2, dest= (155, 500))
c.screen.blit(c.TWO, dest = (185, 600))
cards.o.addToHand(card2T)
"card3"
c.screen.blit(card3, dest = (293, 500))
c.screen.blit(c.THREE, dest = (323, 600))
cards.o.addToHand(card3T)
"card4"
c.screen.blit(card4, dest = (431, 500))
c.screen.blit(c.FOUR, dest = (461, 600))
cards.o.addToHand(card4T)
"card5"
c.screen.blit(card5, dest = (569, 500))
c.screen.blit(c.FIVE, dest = (599, 600))
cards.o.addToHand(card5T)

def reprint():
    c.screen.fill(c.background)
    pygame.draw.line(c.screen, c.black, [135,460], [135,695],3)
    pygame.draw.line(c.screen, c.black, [273,460], [273,695],3)
    pygame.draw.line(c.screen, c.black, [549,498], [549,695],3)
    pygame.draw.line(c.screen, c.black, [411,460], [411,695],3)
    pygame.draw.line(c.screen, c.black, [0,498], [700, 498],3)
    "Card 1"
    card1T = cards.d.printCard()
    card1 = pygame.font.Font.render(c.Font,str(card1T),True, c.black)
    "Card 2"
    card2T = cards.d.printCard()
    card2 = pygame.font.Font.render(c.Font,str(card2T),True, c.black)
    "Card 3"
    card3T = cards.d.printCard()
    card3 = pygame.font.Font.render(c.Font,str(card3T),True, c.black)
    "Card 4"
    card4T = cards.d.printCard()
    card4 = pygame.font.Font.render(c.Font,str(card4T),True, c.black)
    "Card 5"
    card5T = cards.d.printCard()
    card5 = pygame.font.Font.render(c.Font,str(card5T),True, c.black)

    c.screen.blit(card1, dest = (20,500))
    c.screen.blit(c.ONE, dest = (50, 600))
    c.screen.blit(card2, dest= (155, 500))
    c.screen.blit(c.TWO, dest = (185, 600))
    c.screen.blit(card3, dest = (293, 500))
    c.screen.blit(c.THREE, dest = (323, 600))
    c.screen.blit(card4, dest = (431, 500))
    c.screen.blit(c.FOUR, dest = (461, 600))
    c.screen.blit(card5, dest = (569, 500))
    c.screen.blit(c.FIVE, dest = (599, 600))
    c.screen.blit(c.gameBoard, (0, 0))
    c.screen.blit(robot1.img, (robot1.x, robot1.y))
    c.screen.blit(robot2.img, (robot2.x, robot2.y))


done = False
keyPressed = False

while not done:
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RETURN] and not keyPressed:
        keyPressed = True
        (cards.o.printHand())
    if keys[pygame.K_1] and not keyPressed:
        keyPressed = True
        print(card1T)
        reprint()

    if keys[pygame.K_2] and not keyPressed:
        keyPressed = True
        print(card2T)
        reprint()

    if keys[pygame.K_3] and not keyPressed:
        keyPressed = True
        print(card3T)
        reprint()

    if keys[pygame.K_4] and not keyPressed:
        keyPressed = True
        print(card4T)
        reprint()

    if keys[pygame.K_5] and not keyPressed:
        keyPressed = True
        print(card5T)
        reprint()



    if keys[pygame.K_w] and not keyPressed:
        robot1.moveForward()
        keyPressed = True
        c.screen.blit(c.gameBoard, (0, 0))
        c.screen.blit(robot1.img, (robot1.x, robot1.y))
        c.screen.blit(robot2.img, (robot2.x, robot2.y))
        print("R1",robot1.x, robot1.y, robot1.dir)

    if keys[pygame.K_s] and not keyPressed:
        robot1.moveBackward()
        keyPressed = True
        c.screen.blit(c.gameBoard, (0, 0))
        c.screen.blit(robot1.img, (robot1.x, robot1.y))
        c.screen.blit(robot2.img, (robot2.x, robot2.y))
        print("R1",robot1.x, robot1.y, robot1.dir)

    if keys[pygame.K_a] and not keyPressed:
        keyPressed = True
        robot1.turnLeft()
        robot1.img = pygame.image.load(f"graphics/UR{str(robot1.dir)}.png")
        c.screen.blit(c.gameBoard, (0, 0))
        c.screen.blit(robot1.img, (robot1.x, robot1.y))
        c.screen.blit(robot2.img, (robot2.x, robot2.y))
        print("R1",robot1.x, robot1.y, robot1.dir)  # get rid of this

    if keys[pygame.K_d] and not keyPressed:
        keyPressed = True
        robot1.turnRight()
        robot1.img = pygame.image.load(f"graphics/UR{str(robot1.dir)}.png")
        c.screen.blit(c.gameBoard, (0, 0))
        c.screen.blit(robot1.img, (robot1.x, robot1.y))
        c.screen.blit(robot2.img, (robot2.x, robot2.y))
        print("R1",robot1.x, robot1.y, robot1.dir)  # get rid of this

    if keys[pygame.K_i] and not keyPressed:
        robot2.moveForward()
        keyPressed = True
        c.screen.blit(c.gameBoard, (0, 0))
        c.screen.blit(robot1.img, (robot1.x, robot1.y))
        c.screen.blit(robot2.img, (robot2.x, robot2.y))
        print("R2",robot2.x, robot2.y, robot2.dir)

    if keys[pygame.K_k] and not keyPressed:
        robot2.moveBackward()
        keyPressed = True
        c.screen.blit(c.gameBoard, (0, 0))
        c.screen.blit(robot1.img, (robot1.x, robot1.y))
        c.screen.blit(robot2.img, (robot2.x, robot2.y))
        print("R2",robot2.x, robot2.y, robot2.dir)

    if keys[pygame.K_j] and not keyPressed:
        keyPressed = True
        robot2.turnLeft()
        robot2.img = pygame.image.load(f"graphics/UB{str(robot2.dir)}.png")
        c.screen.blit(c.gameBoard, (0, 0))
        c.screen.blit(robot1.img, (robot1.x, robot1.y))
        c.screen.blit(robot2.img, (robot2.x, robot2.y))
        print("R2",robot2.x, robot2.y, robot2.dir)  # get rid of this

    if keys[pygame.K_l] and not keyPressed:
        keyPressed = True
        robot2.turnRight()
        robot2.img = pygame.image.load(f"graphics/UB{str(robot2.dir)}.png")
        c.screen.blit(c.gameBoard, (0, 0))
        c.screen.blit(robot1.img, (robot1.x, robot1.y))
        c.screen.blit(robot2.img, (robot2.x, robot2.y))
        print("R2",robot2.x, robot2.y, robot2.dir)  # get rid of this


    """
    if keys[pygame.K_w] and not keyPressed and (robot1.dir == 0 or robot1.dir == 2):
        keyPressed = True
        robot1.moveUp()
        screen.blit(gameBoard, (0, 0))
        screen.blit(robot1.img, (robot1.x, robot1.y))
        print(robot1.x, robot1.y, robot1.dir)  # get rid of this
    if keys[pygame.K_a] and not keyPressed and (robot1.dir == 3 or robot1.dir == 1):
        keyPressed = True
        robot1.moveLeft()
        screen.blit(gameBoard, (0, 0))
        screen.blit(robot1.img, (robot1.x, robot1.y))
        print(robot1.x, robot1.y, robot1.dir)  # get rid of this

    if keys[pygame.K_s] and not keyPressed and (robot1.dir == 2 or robot1.dir == 0):
        keyPressed = True
        robot1.moveDown()
        screen.blit(gameBoard, (0, 0))
        screen.blit(robot1.img, (robot1.x, robot1.y))
        print(robot1.x, robot1.y, robot1.dir)  # get rid of this

    if keys[pygame.K_d] and not keyPressed and (robot1.dir == 1 or robot1.dir == 3):
        keyPressed = True
        robot1.moveRight()
        screen.blit(gameBoard, (0, 0))
        screen.blit(robot1.img, (robot1.x, robot1.y))
        print(robot1.x, robot1.y, robot1.dir)  # get rid of this
        """

# check for off the board 460
    """
    if robot1.x > 460:
        robot1.x = 460
        screen.blit(robot1.img, (robot1.x, robot1.y))

    if robot1.y > 460:
        robot1.y = 460
        screen.blit(robot1.img, (robot1.x, robot1.y))

    if robot1.y < 0:
        robot1.y = 0
        screen.blit(robot1.img, (robot1.x, robot1.y))

    if robot1.x < 0:
        robot1.x = 0
        screen.blit(robot1.img, (robot1.x, robot1.y))
    """
#cant move in direction its not faceing/behind itself
#fix jumpy thing


    if keyPressed and event.type == pygame.KEYUP:
        keyPressed = False

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


pygame.quit()
