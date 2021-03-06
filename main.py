import sys
import pygame
pygame.init()
game_active = False
screen = pygame.display.set_mode((800,600))
image = pygame.image.load("background/image4.jpg").convert_alpha()
image_rect = image.get_rect(center = (400,300))

test_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf', 30)
test_font1 = pygame.font.Font('Font/Pixeltype.ttf', 60)

snake = pygame.image.load("background/snakethumb.png").convert_alpha()
snake_rect = snake.get_rect(midbottom = (210,520))

runner = pygame.image.load("background/pixelrun.jpg").convert_alpha()
runner_rect = runner.get_rect(midbottom = (600,520))
music = pygame.mixer.Sound("background/intromusic.wav")
music.play(loops = -1)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1 or event.key == pygame.K_LEFT:
                music.fadeout(2)
                import snake
            if event.key == pygame.K_2 or event.key == pygame.K_RIGHT:
                music.fadeout(2)
                import runner_video
                


        
    screen.fill((204,229,253))
    screen.blit(image,image_rect)
    text = test_font1.render("WELCOME TO GAME WORLD",False,(250,2,20))
    text_rect = text.get_rect(center = (400,80))
    screen.blit(text,text_rect)
    text1 = test_font1.render("LET'S GET STARTED !!!",False,(250,2,20))
    text_rect1 = text1.get_rect(center = (400,150))
    screen.blit(text1,text_rect1)
    text2 = test_font.render("SELECT A GAME TO PLAY",False,(0,2,100))
    text_rect2 = text2.get_rect(center = (400,400))
    screen.blit(text2,text_rect2)
    screen.blit(snake,snake_rect)
    screen.blit(runner,runner_rect)
    text3 = test_font.render("Press 1 to play!",False,(0,2,1))
    text_rect3 = text3.get_rect(center = (210,560))
    screen.blit(text3,text_rect3)
    text4 = test_font.render("Press 2 to play!",False,(0,2,1))
    text_rect4 = text4.get_rect(center = (600,560))
    screen.blit(text4,text_rect4)
    text5 = test_font.render(">>>",False,(0,2,1))
    text_rect5 = text5.get_rect(center = (705,480))
    screen.blit(text5,text_rect5)
    text6 = test_font.render("<<<",False,(0,2,1))
    text_rect6 = text6.get_rect(center = (105,480))
    screen.blit(text6,text_rect6)
    pygame.display.update()
