# Olivia Bicks ohb3fs and Charlotte Searle css7kv

import pygame
import gamebox
import random

camera = gamebox.Camera(800,600)
sheet = gamebox.load_sprite_sheet("animation_sheet.png", 5, 6)
frame = 0
direction = 0
character = gamebox.from_image(200, 200, sheet[frame])
#character = gamebox.from_image(100, 200, "game_man.png")
character.yspeed = 0
walls = [
    gamebox.from_color(300, 500, "black", 10, 100),
    gamebox.from_color(600, 500, "black", 10, 100)
]
coins = [
    gamebox.from_image(400, 450, "new_coin.png"),
    gamebox.from_image(200, 450, "new_coin.png")
]
ground = gamebox.from_color(-100, 600, "green", 300000000, 100)
time = 0
counter = 0
score = 0
jump_sound = gamebox.load_sound("jump.wav")
coin_sound = gamebox.load_sound("coin.wav")

def tick(keys):
    global counter
    global frame
    global direction
    global time
    global score
    if counter < 60:
        counter += 1
        camera.clear("blue")
        camera.draw(gamebox.from_text(camera.x, 100, "Get Ready...", "Arial", 40, "Orange", True))
        camera.draw(gamebox.from_text(camera.x, 300, "Catch the coins and hop the walls! Good luck!", "Arial",
                                      20, "Orange", True))
        camera.draw(gamebox.from_text(camera.x, 400, "Use the Spacebar or Up Key to Jump", "Arial", 15, "Orange"))
        camera.display()
    if counter >= 60:
        counter += 1
        frame += 1
        if frame == 10:
            frame = 0
        if counter % 1 == 0:
            character.image = sheet[frame+direction*10]
        if pygame.K_RIGHT in keys:
            character.x += 10
        if character.bottom_touches(ground):
            character.yspeed = 0
            if pygame.K_SPACE in keys or pygame.K_UP in keys:
                character.yspeed = -22
                jump_sound.play()
        character.yspeed += 1
        character.y = character.y + character.yspeed
        camera.clear("blue")
        camera.draw(character)
        camera.draw(ground)
        camera.x += 3
        if character.touches(ground):
            character.move_to_stop_overlapping(ground)
        if counter % 20 == 0:
            time += 1
        if counter % 2 == 0:
            score += 1
        camera.draw(gamebox.from_text(camera.x + 300, 100, "Time: " + str(time),"arial",12,"red", bold=True))
        camera.draw(gamebox.from_text(camera.x + 300, 75, "Score: " + str(score),"arial",12,"red", bold=True))
        leftmost_wall = gamebox.from_color(camera.x - 400, 600, "blue", 0, 800)
        camera.draw(leftmost_wall)
        if character.touches(leftmost_wall):
            camera.draw(gamebox.from_text(camera.x, 100, "Game Over!", "Arial", 40, "Red", True))
            gamebox.pause()
        divisor = 120
        if counter % divisor == 0:
            new_wall = gamebox.from_color(camera.x + 800, 500, "black", 10, random.randint(100, 250))
            walls.append(new_wall)
            divisor += 20
        for wall in walls:
            if character.touches(wall):
                camera.draw(gamebox.from_text(camera.x, 100, "Game Over!", "Arial", 40, "Red", True))
                gamebox.pause()
            camera.draw(wall)
        if counter % 200 == 0:
            new_coin = gamebox.from_image(camera.x + (random.randint(350, 600)), 350, "new_coin.png")
            coins.append(new_coin)
        for coin in coins:
            camera.draw(coin)
            if character.touches(coin):
                coins.remove(coin)
                score += 15
                coin_sound.play()
        camera.draw(ground)
        camera.display()

ticks_per_second = 30

gamebox.timer_loop(ticks_per_second, tick)