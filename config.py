import pygame

pygame.init()

windowSize = [700, 700]
background = (76, 255, 51)
black = (0, 0, 0)
Font = pygame.font.SysFont('Calibri', 32, False, False)
LargeFont = pygame.font.SysFont('calibri', 64, False, False)
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption('RoboRally')
gameBoard = pygame.image.load('graphics/2016doodle.jpg')
screen.fill(background)
pygame.draw.line(screen, black, [135,460], [135,695],3)
pygame.draw.line(screen, black, [273,460], [273,695],3)
pygame.draw.line(screen, black, [411,460], [411,695],3)
pygame.draw.line(screen, black, [549,498], [549,695],3)
pygame.draw.line(screen, black, [0,498], [700, 498],3)
ONE = pygame.font.Font.render(LargeFont,"1",True, black)
TWO = pygame.font.Font.render(LargeFont,"2",True, black)
THREE = pygame.font.Font.render(LargeFont,"3",True, black)
FOUR = pygame.font.Font.render(LargeFont,"4",True, black)
FIVE = pygame.font.Font.render(LargeFont,"5",True, black)
