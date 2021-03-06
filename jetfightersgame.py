import pygame
import time
import random

pygame.init()

display_width=800
display_height=600

xback=0
yback=0

black=(0,0,0)
white=(255,255,255)

gameDisplay=pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Jet Fighters!')
clock=pygame.time.Clock()
clock2=pygame.time.Clock()
clock3=pygame.time.Clock()

cloudImg=pygame.image.load('cloudss.jpg')
fighterImg=pygame.image.load('fighterjet.png')
redjetImg=pygame.image.load('redfighterjet.png')
blackmissleImg=pygame.image.load('blackmissle.png')
redmissleImg=pygame.image.load('redmissle.png')
redfighterjet_width=50
redfighterjet_height=93
fighterjet_width=65
fighterjet_height=97
redmissle_width=23
redmissle_height=62

def background(xback,yback):
	gameDisplay.blit(cloudImg,(xback,yback))
def fighter (x,y):
	gameDisplay.blit(fighterImg,(x,y))

def redfighter1(xredstart1,yredstart1):
	gameDisplay.blit(redjetImg,(xredstart1,yredstart1))

def redfighter2(xredstart2,yredstart2):
	gameDisplay.blit(redjetImg,(xredstart2,yredstart2))

def redfighter3(xredstart3,yredstart3):
	gameDisplay.blit(redjetImg,(xredstart3,yredstart3))

def blackmissle(xblackmissile,yblackmissile):
	gameDisplay.blit(blackmissleImg,(xblackmissile,yblackmissile))

def redmissle (xredmissle,yredmissile):
	gameDisplay.blit(redmissleImg,(xredmissle,yredmissile))

def redmissle2 (xredmissile2,yredmissile2):
	gameDisplay.blit(redmissleImg,(xredmissile2,yredmissile2))

def redmissle3 (xredmissile3,yredmissile3):
	gameDisplay.blit(redmissleImg,(xredmissile3,yredmissile3))

def enemies_hit(score):
	font=pygame.font.SysFont(None,40)
	text=font.render('Enemies Hit:' + str(score),True,black)
	gameDisplay.blit(text,(0,0))

def text_objects(text,font):
	textSurface=font.render(text,True,black)
	return textSurface,textSurface.get_rect()

def message_display(text):
	largeText=pygame.font.Font('freesansbold.ttf',115)
	TextSurf,TextRect = text_objects(text,largeText)
	TextRect.center=((display_width/2),(display_height/2))
	gameDisplay.blit(TextSurf,TextRect)
	pygame.display.update()
	time.sleep(2)
	game_loop()

def crash():
	message_display('You Crashed!')

def game_loop():
	x=display_width*0.5
	y=display_height*0.8
	xredstart1=random.randrange(0,display_width)
	yredstart1=-100
	xredstart2=random.randrange(0,display_width)
	yredstart2=-100
	xredstart3=random.randrange(0,display_width)
	yredstart3=-1000
	xblackmissile=x+(fighterjet_width/2)
	yblackmissile=y
	xredmissle=xredstart1+(redfighterjet_width/2)
	yredmissile=yredstart1
	xredmissile2=xredstart2+(redfighterjet_width/2)
	yredmissile2=yredstart2
	xredmissile3=xredstart3+(redfighterjet_width/2)
	yredmissile3=yredstart3
	blackmissilespeed=0
	redmissilespeed1=0
	redmissilespeed2=0
	redmissilespeed3=0
	missilefired=False
	redmissilefired=False
	redmissilefired2=False
	redmissilefired3=False
	score=0
	time_elapsed_since_last_action=0
	time_elapsed_since_last_action2=0
	time_elapsed_since_last_action3=0

	x_change=0

	xred1change=7
	yred1change=1
	xred2change=10
	yred2change=2
	xred3change=5
	yred3change=3

	gameExit=False
	while not gameExit:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				gameExit=True
				pygame.quit()
				quit()
		if event.type==pygame.KEYDOWN:
			if event.key==pygame.K_LEFT:
				x_change=-10
				if missilefired==False:
					xblackmissile=x+(fighterjet_width/2)

			elif event.key==pygame.K_RIGHT:
				x_change=10
				if missilefired==False:
					xblackmissile=x+(fighterjet_width/2)

			elif event.key==pygame.K_SPACE:
				blackmissilespeed=-10
				missilefired=True

		if event.type==pygame.KEYUP:
			if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
				x_change=0

		x+=x_change
		background(xback,yback)
		#gameDisplay.fill(white)
		if missilefired==True:
			yblackmissile+=blackmissilespeed
			blackmissle(xblackmissile,yblackmissile)
			if yblackmissile==0:
				missilefired=False
				xblackmissile=x+(fighterjet_width/2)
				yblackmissile=y

		fighter(x,y)
		redfighter1(xredstart1,yredstart1)
		redfighter2(xredstart2,yredstart2)
		redfighter3(xredstart3,yredstart3)
		enemies_hit(score)

		dt=clock.tick()
		time_elapsed_since_last_action+=dt
		if redmissilefired==False:
			if time_elapsed_since_last_action > 1000:
				redmissilespeed1=10
				time_elapsed_since_last_action=0
				redmissilefired=True
		if redmissilefired==True:
			yredmissile+=redmissilespeed1
			redmissle(xredmissle,yredmissile)
			if yredmissile > display_height:
				redmissilefired=False
				xredmissle=xredstart1+(redfighterjet_width/2)
				yredmissile=yredstart1

		dt2=clock2.tick()
		time_elapsed_since_last_action2+=dt2
		if redmissilefired2==False:
			if time_elapsed_since_last_action2 > 2000:
				redmissilespeed2=10
				time_elapsed_since_last_action2=0
				redmissilefired2=True
		if redmissilefired2==True:
			yredmissile2+=redmissilespeed2
			redmissle2(xredmissile2,yredmissile2)
			if yredmissile2>display_height:
				redmissilefired2=False
				xredmissile2=xredstart2+(redfighterjet_width/2)
				yredmissile2=yredstart2

		dt3=clock3.tick()
		time_elapsed_since_last_action3+=dt3
		if redmissilefired3==False:
			if time_elapsed_since_last_action3 > 3000:
				redmissilespeed3=10
				time_elapsed_since_last_action3=0
				redmissilefired3=True
		if redmissilefired3==True:
			yredmissile3+=redmissilespeed3
			redmissle3(xredmissile3,yredmissile3)
			if yredmissile3>display_height:
				redmissilefired3=False
				xredmissile3=xredstart3+(redfighterjet_width/2)
				yredmissile3=yredstart3

		if xredstart1 > display_width-redfighterjet_width:
			xred1change=-7
		elif xredstart1 < 0:
			xred1change=+7
		xredstart1+=xred1change
		yredstart1+=yred1change

		if xredstart2 > display_width - redfighterjet_width:
			xred2change=-10
		elif xredstart2 < 0:
			xred2change=+10
		xredstart2+=xred2change
		yredstart2+=yred2change

		if xredstart3 > display_width - redfighterjet_width:
			xred3change=-5
		elif xredstart3 < 0:
			xred3change=+5
		xredstart3+=xred3change
		yredstart3+=yred3change


		if yblackmissile < yredstart1 + redfighterjet_height:
			if xblackmissile > xredstart1 and xblackmissile < xredstart1 + redfighterjet_width or xblackmissile + fighterjet_width > xredstart1 and xblackmissile + fighterjet_width < xredstart1 + redfighterjet_width:
				xredstart1=random.randrange(0,display_width)
				yredstart1=-100
				score+=1
				missilefired=False
				xblackmissile=x+(fighterjet_width/2)
				yblackmissile=y
		if yblackmissile < yredstart2 + redfighterjet_height:
			if xblackmissile > xredstart2 and xblackmissile < xredstart2 + redfighterjet_width or xblackmissile + fighterjet_width > xredstart2 and xblackmissile + fighterjet_width < xredstart2 + redfighterjet_width:
				xredstart2=random.randrange(0,display_width)
				yredstart2=-100
				score+=1
				missilefired=False
				xblackmissile=x+(fighterjet_width/2)
				yblackmissile=y
		if yblackmissile < yredstart3 + redfighterjet_height:
			if xblackmissile > xredstart3 and xblackmissile < xredstart3 + redfighterjet_width or xblackmissile + fighterjet_width > xredstart3 and xblackmissile + fighterjet_width < xredstart3 + redfighterjet_width:
				xredstart3=random.randrange(0,display_width)
				yredstart3=-100
				score+=1
				missilefired=False
				xblackmissile=x+(fighterjet_width/2)
				yblackmissile=y
#All crash possibilities
		if x > display_width-fighterjet_width or x<0 or yredstart1 > display_height:
			crash()
		if x > display_width-fighterjet_width or x<0 or yredstart2 > display_height:
			crash()
		if x > display_width-fighterjet_width or x<0 or yredstart3 > display_height:
			crash()
		if y < yredmissile + redmissle_height:
			if x > xredmissle and x < xredmissle + redmissle_width or x + fighterjet_width > xredmissle and x + fighterjet_width < xredmissle + redmissle_width:
				crash()
		if y < yredmissile2 + redmissle_height:
			if x > xredmissile2 and x < xredmissile2 + redmissle_width or x + fighterjet_width > xredmissile2 and x + fighterjet_width < xredmissile2 + redmissle_width:
				crash()
		if y < yredmissile3 + redmissle_height:
			if x > xredmissile3 and x < xredmissile3 + redmissle_width or x + fighterjet_width > xredmissile3 and x + fighterjet_width < xredmissile3 + redmissle_width:
				crash()
		pygame.display.update()
		clock.tick(60)


game_loop()
pygame.quit()
quit()
