from plane_sprites import *


class PlaneGame(object):
	"""docstring for PlaneGame"""
	def __init__(self):
		print("游戏初始化！！！")
		#1.设置游戏窗口
		self.screen = pygame.display.set_mode(SECREEN_RECT.size)
		#2.设置游戏时钟
		self.clock = pygame.time.Clock()
		#3.初始化精灵组
		self.__creat_sprites()
		#4.自定义事件
		pygame.time.set_timer(CREAT_ENEMY_EVENT,1000)
		pygame.time.set_timer(HERO_FIRE_EVENT,500)

	def __creat_sprites(self):
		bg1 = Background()
		bg2 = Background(True)

		self.back_group = pygame.sprite.Group(bg1,bg2)

		self.enemy_group = pygame.sprite.Group()

		self.hero = Hero()

		self.hero_group = pygame.sprite.Group(self.hero)

	def start_game(self):
		print("开始游戏！！！")
		while True:
			#1.设置游戏刷新频率
			self.clock.tick(FRAME_RES_SEC)
			#2.事件监听
			self.__event_handler()
			#3.碰撞检测
			self.__check_collide()
			#4.更新/绘制精灵
			self.__update_sprite()
			#5.更新显示
			pygame.display.update()

	def __event_handler(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				PlaneGame.game_over()
			elif event.type == CREAT_ENEMY_EVENT:
				#print("敌机出现了！！！")
				enemy = Enemy()
				self.enemy_group.add(enemy)
			#elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
			#	print("飞机向右移动。。。")
			elif event.type == HERO_FIRE_EVENT:
				self.hero.fire()

			keys_pressed = pygame.key.get_pressed()
			if keys_pressed[pygame.K_RIGHT]:
				# print("飞机向右移动。。。")
				self.hero.speed = 2
			elif keys_pressed[pygame.K_LEFT]:
				self.hero.speed = -2
			else:
				self.hero.speed = 0

	def __check_collide(self):
		pygame.sprite.groupcollide(self.hero.bullet_group, self.enemy_group, True, True)
		enemy_list = pygame.sprite.spritecollide(self.hero,self.enemy_group,True)
		if len(enemy_list)>0:
			self.hero.kill()

			PlaneGame.game_over()

	def __update_sprite(self):
		self.back_group.update()
		self.back_group.draw(self.screen)

		self.enemy_group.update()
		self.enemy_group.draw(self.screen)

		self.hero_group.update()
		self.hero_group.draw(self.screen)

		self.hero.bullet_group.update()
		self.hero.bullet_group.draw(self.screen)

	@staticmethod
	def game_over():
		print("游戏结束！！！")

		pygame.quit()
		exit()

def main():
	game = PlaneGame()

	game.start_game()

if __name__ == '__main__':
	main()