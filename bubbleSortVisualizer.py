import pygame

pygame.init()

win = pygame.display.set_mode((500, 400))

pygame.display.set_caption("Bubble sort")

x = 40
y = 40

width = 20

height = [195, 80, 130, 90, 175, 55, 75,
			81, 51, 80, 82, 159, 96, 14]

run = True
execute = False

font = pygame.font.SysFont('Arial', 20)

def show(height):
	for i in range(len(height)):
		pygame.draw.rect(win, (255, 0, 0), (x + 30 * i, y, width, height[i]))

while run:
	pygame.time.delay(10)
	keys = pygame.key.get_pressed()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	if keys[pygame.K_SPACE]:
		execute = True
	if execute == False:
		win.fill((0, 0, 0))
		show(height)
		text = font.render("Press SPACE to start sorting", True, (255, 255, 255))
		win.blit(text, (120, 350))
		pygame.display.update()

	else:

		for i in range(len(height) - 1):
			for j in range(len(height) - i - 1):
				if height[j] > height[j + 1]:
					t = height[j]
					height[j] = height[j + 1]
					height[j + 1] = t
				win.fill((0, 0, 0))
				show(height)
				pygame.time.delay(50)
				pygame.display.update()
pygame.quit()
