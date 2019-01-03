
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
import game_functions as gf
from random import randint

def run_game():
	
	pygame.init()
	ai_settings = Settings()
	screen=pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	ship = Ship(ai_settings, screen)
	bullets = Group()
	aliens = Group()
	gf.create_fleet(ai_settings, screen, ship, aliens)
	while True:
		bg_color = (225+randint(-100,10),225+randint(-100,10),225+randint(-100,10))
		gf.check_events(ai_settings, screen, ship, bullets)
		ship.update()
		bullets.update()
		for bullet in bullets.copy():
			if bullet.rect.bottom <= 0:
				bullets.remove(bullet)
		print(len(bullets))
		gf.update_screen(ai_settings, screen, ship, aliens, bullets)

run_game()

