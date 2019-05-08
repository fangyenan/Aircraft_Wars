import random

import pygame

SECREEN_RECT = pygame.Rect(0,0,480,700)
FRAME_RES_SEC = 60
CREAT_ENEMY_EVENT = pygame.USEREVENT
HERO_FIRE_EVENT = pygame.USEREVENT + 1 

class GameSprite(pygame.sprite.Sprite):
	"""飞机大战游戏精灵"""

	def __init__(self,image_name,speed=1):

		super().__init__()

		self.image = pygame.image.load(image_name)
		self.rect = self.image.get_rect()
		self.speed = speed


	def update(self):

		self.rect.y += self.speed

class Background(GameSprite):
	"""背景类"""
	def __init__(self, is_alt=False):
		super().__init__("./images/background.png")

		if is_alt:
			self.rect.y = -self.rect.height

	def update(self):
		super().update()

		if self.rect.y >= SECREEN_RECT.height:
			self.rect.y = -self.rect.height
		
class Enemy(GameSprite):
	"""敌机类"""
	def __init__(self):
		#1.调用父类方法，并指定敌机图片
		super().__init__("./images/enemy1.png")
		#2.设定敌机随机速度
		self.speed = random.randint(1,3)
		#3.设机敌机随机位置
		max_x = SECREEN_RECT.width - self.rect.width
		self.rect.x = random.randint(0,max_x)
	
	def update(self):
		super().update()


		if self.rect.y >= SECREEN_RECT.height:
			#print("敌机飞出屏幕需要从精灵组删除！！！")
			self.kill()

	def __del__(self):
		#print("敌机从内存中删除！！！")
		pass

class Hero(GameSprite):
	"""英雄精灵"""
	def __init__(self):
		super().__init__("./images/me1.png",0)
		self.rect.centerx = SECREEN_RECT.centerx
		self.rect.bottom = SECREEN_RECT.bottom - 120
		self.bullet_group = pygame.sprite.Group()

	def update(self):
		self.rect.x += self.speed

		if self.rect.x < 0:
			self.rect.x = 0
		elif self.rect.right > SECREEN_RECT.right:
			self.rect.right = SECREEN_RECT.right

	def fire(self):
		print("发射子弹。。。")
		for i in (1,2,3):
			#1.创建子弹精灵
			bullet = Bullet()
			#2.设置子弹精灵的位置
			bullet.rect.bottom = self.rect.y - i*20
			bullet.rect.centerx = self.rect.centerx
			#3.将子弹精灵加入精灵组
			self.bullet_group.add(bullet)

class Bullet(GameSprite):
		"""子弹精灵"""
		def __init__(self):
			super().__init__("./images/bullet1.png",-2)

		def update(self):
			super().update()

			if self.rect.bottom <=0:
				self.kill()
		
		def __del__(self):
			print("子弹精灵在内存中被销毁了！！！！")