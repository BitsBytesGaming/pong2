import pygame, sys, random
from pygame.locals import *

#window + game settings
fps = 30
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
ARENAWIDTH = 560
ARENAHEIGHT = 480
BALLSPEED = 0
BALLWIDTH = 20
PADDLEWIDTH = 15
PADDLEHEIGHT = 50

#init
pygame.init()
SCREEN = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption('Pong')

#paddle positions
LEFTPADDLEPOSITION = (BALLWIDTH,((ARENAHEIGHT/2)-PADDLEHEIGHT),BALLWIDTH,((ARENAHEIGHT/4)-(PADDLEHEIGHT/4)))
RIGHTPADDLEPOSITION = ((WINDOWWIDTH-(2*BALLWIDTH)),((ARENAHEIGHT/2)-PADDLEHEIGHT),BALLWIDTH,((ARENAHEIGHT/4)-(PADDLEHEIGHT/4)))
BALLPOSITION = ((WINDOWWIDTH/2)-(BALLWIDTH/2),((ARENAHEIGHT/2)-BALLWIDTH),BALLWIDTH,BALLWIDTH)

#colors      R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
BLACK    = (  0,   0,   0)

BGCOLOR = BLACK
BLOCKCOLOR = WHITE
	
def main():
	global clock, fps, SCREEN

	complete = False
	player_velocity = 0
	bot_velocity = 0
	ball_x_velocity = random.randint(-3,3)
	ball_y_velocity = random.randint(-2,2)

	while complete == False:
		clock.tick(fps)
		for event in pygame.event.get():
			if event.type == QUIT:
				complete = True
				pygame.quit()
				sys.exit()
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_DOWN:
					player_velocity -= 1
				elif event.key == pygame.K_UP:
					player_velocity += 1
				elif event.key == pygame.K_s:
					player_velocity -= 1
				elif event.key == pygame.K_w:
					player_velocity += 1

			SCREEN.fill(BGCOLOR)
			bot_paddle = pygame.draw.rect(SCREEN,BLOCKCOLOR,LEFTPADDLEPOSITION)
			#print(LEFTPADDLEPOSITION)
			player_paddle = pygame.draw.rect(SCREEN,BLOCKCOLOR,RIGHTPADDLEPOSITION)
			#print(RIGHTPADDLEPOSITION)
			ball = pygame.draw.rect(SCREEN,BLOCKCOLOR,BALLPOSITION)
			#print(BALLPOSITION)

			pygame.display.flip()

			player_paddle.move(0, player_velocity)

			pygame.display.update()

if __name__== '__main__':
	main()
