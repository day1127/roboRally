import pygame
import robot
import cards

pygame.init()

windowSize = [500, 500]
screen = pygame.display.set_mode(windowSize)
gameBoard = pygame.image.load('graphics/2016doodle.jpg')
robot1 = robot.Robot('Lloyd', 0, 0)
robot1.img = pygame.image.load('graphics/UR1.png')
screen.blit(gameBoard, (0, 0))
screen.blit(robot1.img, (robot1.x, robot1.y))

done = False
keyPressed = False

while not done:
    keys = pygame.key.get_pressed()
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

    if keys[pygame.K_q] and not keyPressed:
        keyPressed = True
        robot1.turnLeft()
        robot1.img = pygame.image.load(f"graphics/UR{str(robot1.dir)}.png")
        screen.blit(gameBoard, (0, 0))
        screen.blit(robot1.img, (robot1.x, robot1.y))
        print(robot1.x, robot1.y, robot1.dir)  # get rid of this

    if keys[pygame.K_e] and not keyPressed:
        keyPressed = True
        robot1.turnRight()
        robot1.img = pygame.image.load(f"graphics/UR{str(robot1.dir)}.png")
        screen.blit(gameBoard, (0, 0))
        screen.blit(robot1.img, (robot1.x, robot1.y))
        print(robot1.x, robot1.y, robot1.dir)  # get rid of this

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
