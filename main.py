import pygame as pg
from random import randint as ri


pg.init()
screen = pg.display.set_mode((400, 600))
clock = pg.time.Clock()
running = True
pg.display.set_caption("Gifts")

velocity = 5
speed = 5
score = 0
lives = 3
font = pg.font.Font(None, 36)
game_over = False


class GiftSprite(pg.sprite.Sprite):
    def __init__(self, png_path, position):
        super().__init__()
        self.image = pg.image.load(png_path).convert_alpha()
        self.image = pg.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect(topleft=position)


gift_sprite = GiftSprite("spirit.png", (165, 520))
gift_sprite.image = pg.transform.scale(gift_sprite.image, (75, 75))
pos_x, pos_y = 165, 520

full_heart = "heart.png"
empty_heart = "heart_lost.png"

heart_sprite1 = pg.image.load(full_heart).convert_alpha()
heart_sprite1 = pg.transform.scale(heart_sprite1, (50, 50))
heart_sprite2 = pg.image.load(full_heart).convert_alpha()
heart_sprite2 = pg.transform.scale(heart_sprite2, (50, 50))
heart_sprite3 = pg.image.load(full_heart).convert_alpha()
heart_sprite3 = pg.transform.scale(heart_sprite3, (50, 50))

arrow_image = "arrow.png"


class Arrow(pg.sprite.Sprite):
    def __init__(self, png_path, position, speed):
        super().__init__()  # Call the __init__ method of the parent class
        self.image = pg.image.load(png_path).convert_alpha()
        self.image = pg.transform.scale(self.image, (20, 60))
        self.rect = self.image.get_rect(topleft=position)
        self.speed = speed

    def update(self):
        self.rect.y += self.speed


arrow_sprite = Arrow(arrow_image, (ri(0, 375), 65), speed)
arrow_sprite.image = pg.transform.scale(arrow_sprite.image, (20, 60))

arrow_group = pg.sprite.Group(arrow_sprite)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()

    # Update game logic based on keys
    if not game_over:
        if keys[pg.K_LEFT] and pos_x - velocity >= 5:
            pos_x -= velocity
        if keys[pg.K_RIGHT] and pos_x + velocity + 75 <= 395:
            pos_x += velocity

        if arrow_sprite.rect.bottom >= 600:
            score += 1
            arrow_sprite.rect.topleft = (ri(0, 375), 65)

        # Update the GiftSprite position
        gift_sprite.rect.topleft = (pos_x, pos_y)

        screen.fill((64, 179, 154))

        # Blit the GiftSprite image
        screen.blit(gift_sprite.image, gift_sprite.rect.topleft)
        screen.blit(arrow_sprite.image, arrow_sprite.rect.topleft)

        if pg.sprite.spritecollide(gift_sprite, arrow_group, True):
            lives -= 1
            if lives == 2:
                heart_sprite1 = pg.image.load(empty_heart).convert_alpha()
                heart_sprite1 = pg.transform.scale(heart_sprite1, (50, 50))
            elif lives == 1:
                heart_sprite2 = pg.image.load(empty_heart).convert_alpha()
                heart_sprite2 = pg.transform.scale(heart_sprite1, (50, 50))
            elif lives == 0:
                game_over = True
                heart_sprite3 = pg.image.load(empty_heart).convert_alpha()
                heart_sprite3 = pg.transform.scale(heart_sprite1, (50, 50))
                game_over_font = pg.font.Font(None, 64)
                game_over_text = game_over_font.render("Game Over", True, (255, 0, 0))
                game_over_rect = game_over_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
                screen.blit(game_over_text, game_over_rect)
                pg.display.flip()

            arrow_sprite = Arrow(arrow_image, (ri(0, 375), 65), speed)
            arrow_sprite.image = pg.transform.scale(arrow_sprite.image, (20, 60))

            arrow_group = pg.sprite.Group(arrow_sprite)

        if score == 10:
            speed = 7
        if score == 25:
            speed = 10
        if score == 50:
            speed = 20
        if score == 75:
            speed = 25
        if score == 100:
            game_over = True
            score = 0
            lives = 3
            game_win_font = pg.font.Font(None, 64)
            game_win_text = game_win_font.render("You Won", True, (255, 0, 0))
            game_win_rect = game_win_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            screen.blit(game_win_text, game_win_rect)
            pg.display.flip()

        screen.blit(heart_sprite1, (400 - 165, 10))
        screen.blit(heart_sprite2, (400 - 110, 10))
        screen.blit(heart_sprite3, (400 - 55, 10))

        arrow_group.update()

        # RENDER YOUR GAME HERE
        pg.draw.rect(screen, (245, 131, 122), (10, 10, 150, 50), border_radius=10)


        score_text = font.render("{}".format(score), True, (255,255,255))
        score_text_rect = score_text.get_rect(center=((10) + 150 // 2, 10 + 50 // 2))
        screen.blit(score_text, score_text_rect.topleft)

        pg.display.flip()

        clock.tick(60)

    else:
        if keys[pg.K_r]:
            game_over = False
            velocity = 5
            speed = 5
            score = 0
            lives = 3
            heart_sprite1 = pg.image.load(full_heart).convert_alpha()
            heart_sprite1 = pg.transform.scale(heart_sprite1, (50, 50))
            screen.blit(heart_sprite1, (400 - 165, 10))
            heart_sprite2 = pg.image.load(full_heart).convert_alpha()
            heart_sprite2 = pg.transform.scale(heart_sprite2, (50, 50))
            screen.blit(heart_sprite2, (400 - 110, 10))
            heart_sprite3 = pg.image.load(full_heart).convert_alpha()
            heart_sprite3 = pg.transform.scale(heart_sprite3, (50, 50))
            screen.blit(heart_sprite3, (400 - 55, 10))

pg.quit()
