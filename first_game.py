# Olivia Bicks ohb3fs

import pygame
import gamebox

camera = gamebox.Camera(800,600)
character = gamebox.from_color(50, 50, "red", 30, 60)
coin_1 = gamebox.from_image(400, 450, "http://www.psdgraphics.com/file/empty-gold-coin-icon.jpg")
coin_1.width = 20
coin_1.height = 20
coin_2 = gamebox.from_image(200, 450, "http://www.psdgraphics.com/file/empty-gold-coin-icon.jpg")
coin_2.width = 20
coin_2.height = 20
coin_3 = gamebox.from_image(600, 450, "http://www.psdgraphics.com/file/empty-gold-coin-icon.jpg")
coin_3.width = 20
coin_3.height = 20
coins = [coin_1, coin_2, coin_3]
walls = [gamebox.from_color(400,470, "black", 80, 10), gamebox.from_color(200,470, "black", 80, 10), gamebox.from_color(600,470, "black", 80, 10)]
character.yspeed = 0
ground = gamebox.from_color(-100, 600, "black", 3000, 100)
counter = 0
score = 0
time = 0

def tick(keys):
    global time
    global counter
    global coin_1
    global coin_2
    global coin_3
    global coins
    global score
    counter += 1
    if pygame.K_RIGHT in keys:
        character.x += 5
    if pygame.K_LEFT in keys:
        character.x -= 5
    camera.clear("cyan")
    camera.draw(character)
    camera.draw(ground)
    for coin in coins:
        camera.draw(coin)
        if character.touches(coin):
            coins.remove(coin)
            score += 1
    camera.draw(gamebox.from_text(50,100, "Score: " + str(score),"arial",12,"red", bold=True))
    if counter % 20 == 0:
        time += 1
    camera.draw(gamebox.from_text(750,100, "Time: " + str(time),"arial",12,"red", bold=True))
    character.yspeed += 1
    character.y = character.y + character.yspeed
    if character.bottom_touches(ground):
        character.yspeed = 0
        if pygame.K_SPACE in keys:
            character.yspeed = -15
    if character.touches(ground):
        character.move_to_stop_overlapping(ground)
    for wall in walls:
        if character.bottom_touches(wall):
            character.yspeed = 0
            if pygame.K_SPACE in keys:
                character.yspeed = -20
        if character.touches(wall):
            character.move_to_stop_overlapping(wall)
        camera.draw(wall)
    camera.display()
ticks_per_second = 30


gamebox.timer_loop(ticks_per_second, tick)