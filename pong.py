import pygame
from time import sleep

pygame.init()

#TODO: Use common class for both Player and Enemy, inherit and then only customize specialized methods
class Player():
	def __init__(self):
		self.x, self.y = 0, ScreenHeight/2
		self.speed = 6
		self.padWid, self.padHei = 15, 84
		self.score = 0
		self.scoreFont = pygame.font.SysFont("calibri", 63)
	
	#TODO: use this method only to get the scores (consider writing getter/setter here). How to display shouldn't be managed here
	#TODO: Instead, write a separate class to manage how to display...
	def scoring(self):
		plw = self.scoreFont.render('player wins',1,(255,255,255))
		scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
		screen.blit(scoreBlit, (32, 16))
		if self.score == 10:
			screen.blit(plw,(32,16))
			exit()

			
	
	def movement(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_w]:
			self.y -= self.speed
		elif keys[pygame.K_s]:
			self.y += self.speed
	
		if self.y <= 0:
			self.y = 0
		elif self.y >= ScreenHeight-84:
			self.y = ScreenHeight-84
	
	def draw(self):
		pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.padWid, self.padHei))

class Enemy():
	def __init__(self):
		self.x, self.y = ScreenWidth-16, ScreenHeight/2
		self.speed = 6
		self.padWid, self.padHei = 15, 84
		self.score = 0
		self.scoreFont = pygame.font.SysFont("calibri", 63)
	
	def scoring(self):
		plw = self.scoreFont.render('player wins',1,(255,255,255))
		scoreBlit = self.scoreFont.render(str(self.score), 1, (255, 255, 255))
		screen.blit(scoreBlit, (ScreenHeight+92, 16))
		if self.score == 2:
			screen.blit(plw,(32,16))
			sleep(2)
			exit()
	
	def movement_Ai(self):
		
		difference = ball.y - self.y
		if ball.speed_x > 0:
			if difference >= 5 or difference <=-5:
				if difference > 5:
					self.y -= self.speed
				else:
					self.y += self.speed	
				
		if self.y <= 0:
		 	self.y = 0
		 	self.speed *= -1
		elif self.y >= ScreenHeight-84:
		 	self.y = ScreenHeight-84
		 	
		 	#self.speed *= -1

	def movement(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_UP]:
			self.y -= self.speed
		elif keys[pygame.K_DOWN]:
			self.y += self.speed
		if self.y <= 0:
		 	self.y = 0
		 	
		elif self.y >= ScreenHeight-84:
		 	self.y = ScreenHeight-84	
	
		
	
	def draw(self):
		pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.padWid, self.padHei))

class Ball():
	def __init__(self):
		self.x, self.y = ScreenWidth/2, ScreenHeight/2
		self.speed_x = -5
		self.speed_y = 5
		self.size = 20
		#half = int(self.width / 2)
	
	def movement(self):
		self.x += self.speed_x
		self.y += self.speed_y

		#wall col
		if self.y <= 0:
			self.speed_y *= -1
		elif self.y >= ScreenHeight-self.size:
			self.speed_y *= -1

		if self.x <= 0:
			enemy.score += 1
			self.__init__()
			sleep(1)
			
		elif self.x >= ScreenWidth-self.size:
			player.score += 1
			self.__init__()
			sleep(1)
			self.speed_x = 3
			
		##wall col
		#paddle col
		#player
		for n in range(-self.size, player.padHei):
			if self.y == player.y + n:
				if self.x <= player.x + player.padWid:
					self.speed_x *= -1
					break
			#n += 1
		#enemy
		for n in range(-self.size, enemy.padHei):
			if self.y == enemy.y + n:
				if self.x >= enemy.x - enemy.padWid:
					self.speed_x *= -1
					break
			#n += 1
		##paddle col

	def draw(self):
		pygame.draw.rect(screen, (50,10,255), (self.x, self.y, 20, 20))
		#pygame.draw.circle(screen,[34,95,200],[self.x, self.y], self.size)


def text_to_screen(screen, text, x, y, size = 15, color = (255,255,255), font_type = 'calibri'):

    text = str(text)
    font = pygame.font.SysFont(font_type, size)
    text = font.render(text, True, color)
    screen.blit(text, (x,y))

ScreenWidth, ScreenHeight = 960, 480

screen = pygame.display.set_mode((ScreenWidth, ScreenHeight))
pygame.display.set_caption("Pong - MURTAZA")
pygame.font.init()
clock = pygame.time.Clock()
FPS = 60

ball = Ball()
player = Player()
enemy = Enemy()
#background = pygame.image.load("pong_b.jpg")

while True:
	#process
	for event in pygame.event.get():
			keys = pygame.key.get_pressed()
			if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
				#print 'Game exited by user'
				exit()
	##process
	#logic
	
	ball.movement()
	player.movement()
	enemy.movement_Ai()
		
	#enemy.movement_Ai()
			

		
		
	##logic
	#draw
	#screen.blit(background,(0,0))
	screen.fill((0, 245, 0))
	text_to_screen(screen, text = 'PONG Game', x = 270, y = 1, size=20, color=(255, 0, 0), font_type='calibri')
	text_to_screen(screen, text = 'Created by MURTAZA ROONDIWALA', x = 200, y = 460, size = 20, color=(0, 0, 255), font_type='Aparajita')

    

	ball.draw()
	player.draw()
	player.scoring()
	enemy.draw()
	enemy.scoring()
	##draw
	#_______
	pygame.display.flip()
	clock.tick(FPS)