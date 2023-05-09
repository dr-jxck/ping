import pygame
import time
from sys import exit
import os
import random
 
#Setup
os.chdir(os.path.dirname(os.path.abspath(__file__)))
pygame.init()
screen = pygame.display.set_mode((800,425))
logo = pygame.image.load("assets/logo.ico")
pygame.display.set_icon(logo)
pygame.display.set_caption("Ping")
clock = pygame.time.Clock()

ball_dir = "left"
paddle_speed = 10
ball_speed = 10
hits = 1
left_points = 0
right_points = 0

#Loading assets
font = pygame.font.Font("assets/font.ttf",50)

floor = pygame.image.load("assets/border1.png")
floor_rec = floor.get_rect(bottomleft = (0,425))

rightwall = pygame.image.load("assets/border2.png")
rightwall_rec = rightwall.get_rect(topright = (800,0))

roof = pygame.image.load("assets/border1.png")
roof_rec = roof.get_rect(topleft = (0,0))

leftwall = pygame.image.load("assets/border2.png")
leftwall_rec = leftwall.get_rect(topleft = (0,0))

middle = pygame.image.load("assets/middle.png")
middle_rec = middle.get_rect(center = (400,212))

paddle1 = pygame.image.load("assets/paddle.png")
paddel1_rec = paddle1.get_rect(midleft = (10,212))

paddel2 = pygame.image.load("assets/paddle.png")
paddel2_rec = paddel2.get_rect(midright = (790,212))

ball = pygame.image.load("assets/ball.png")
ball_rec = ball.get_rect(center = (450,212.5))
 
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        key = pygame.key.get_pressed()

    left_points_counter = font.render(str(left_points), False, "White")
    left_points_counter_rec = left_points_counter.get_rect(center = (200,50))

    right_points_counter = font.render(str(right_points), False, "White")
    right_points_counter_rec = right_points_counter.get_rect(center = (600,50))

    screen.fill("Black")
    screen.blit(floor,floor_rec)
    screen.blit(rightwall,rightwall_rec)
    screen.blit(roof,roof_rec)
    screen.blit(leftwall,leftwall_rec)
    screen.blit(middle,middle_rec)
    screen.blit(paddle1,paddel1_rec)
    screen.blit(paddel2,paddel2_rec)
    screen.blit(ball,ball_rec)
    screen.blit(left_points_counter,left_points_counter_rec)
    screen.blit(right_points_counter,right_points_counter_rec)

    if ball_rec.colliderect(rightwall_rec):
        left_points += 1
        ball_rec.center = (400,212)
        ball_dir = "left"
    if ball_rec.colliderect(leftwall_rec):
        right_points += 1
        ball_rec.center = (400,212)
        ball_dir = "right"

    if paddel1_rec.colliderect(ball_rec):
        hits += 1
        if ball_speed < 30:
            ball_speed += (ball_speed*(hits/200))
        if key[pygame.K_a]:
            ball_dir = "upright"
        elif key[pygame.K_d]:
            ball_dir = "downright"
        elif ball_dir == "upleft":
                ball_dir = "upright"
        elif ball_dir == "downleft":
            ball_dir = "downright"
        else:
            ball_dir = "right"
    if paddel2_rec.colliderect(ball_rec):
        hits += 1
        if ball_speed < 30:
            ball_speed += (ball_speed*(hits/300))
        if key[pygame.K_RIGHT]:
            ball_dir = "downleft"
        elif key[pygame.K_LEFT]:
            ball_dir = "upleft"
        elif ball_dir == "upright":
            ball_dir = "upleft"
        elif ball_dir == "downright":
            ball_dir = "downleft"
        else:
            ball_dir = "left"

    if ball_dir == "right":
        ball_rec.right += ball_speed
    if ball_dir == "downright":
        ball_rec.right += ball_speed
        ball_rec.bottom += ball_speed
        if ball_rec.colliderect(floor_rec):
            ball_dir = "upright"
    if ball_dir == "upright":
        ball_rec.right += ball_speed
        ball_rec.top -= ball_speed
        if ball_rec.colliderect(roof_rec):
            ball_dir = "downright"

    if ball_dir == "left":
        ball_rec.left -= ball_speed
    if ball_dir == "downleft":
        ball_rec.left -= ball_speed
        ball_rec.bottom += ball_speed
        if ball_rec.colliderect(floor_rec):
            ball_dir = "upleft"
    if ball_dir == "upleft":
        ball_rec.left -= ball_speed
        ball_rec.top -= ball_speed
        if ball_rec.colliderect(roof_rec):
            ball_dir = "downleft"

    print(str(left_points)+" | "+str(right_points))
    #apaddel1_rec.y = ball_rec.y
    #paddel2_rec.y = ball_rec.y

    if key[pygame.K_a]:
        paddel1_rec.top -= paddle_speed
    if key[pygame.K_d]:
        paddel1_rec.bottom += paddle_speed
    if paddel1_rec.colliderect(roof_rec):
        paddel1_rec.top = 7
    if paddel1_rec.colliderect(floor_rec):
        paddel1_rec.bottom = 418

    if key[pygame.K_LEFT]:
        paddel2_rec.top -= paddle_speed
    if key[pygame.K_RIGHT]:
        paddel2_rec.bottom += paddle_speed
    if paddel2_rec.colliderect(roof_rec):
        paddel2_rec.top = 7
    if paddel2_rec.colliderect(floor_rec):
        paddel2_rec.bottom = 418

    pygame.display.update()
    clock.tick(30)