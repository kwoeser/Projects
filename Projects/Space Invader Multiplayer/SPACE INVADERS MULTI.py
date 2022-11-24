 # Karma Woeser
# Space Invaders Multiplayer 

import pygame, random
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 219, 77)
ORANGE = (255, 163, 26)
PINEGREEN = (0, 230, 115)
BEIGE = (233, 233, 175)
PURPLE = (115, 0, 153)
GRAYBLUE = (92, 92, 138)

pygame.init()
 
# Set the height and width of the screen
size = [600, 500]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Space Invaders Multiplayer")
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

done = True
page_number = 1

while done:
    '''
      When MOUSEBUTTONDOWN is clicked it will add 1 to page_number. Then when page_number 3 equals 3 then the while loop will end and you won't be able to click any more.
    '''
    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
          page_number += 1
          if page_number == 3:
              done = False
 

    # Set the screen background
    screen.fill(BLACK)
 
    if page_number == 1:
        # FONTS
        font = pygame.font.SysFont('ITC Machine Font', 30, True, False)

        bigFont = pygame.font.SysFont('ITC Machine Font', 70, True, False)

        smallFont = pygame.font.SysFont('ITC Machine Font', 20, True, False)

        # TITLE
        text = bigFont.render("SPACE INVADERS", True, GRAYBLUE)
        screen.blit(text, [60, 40])
        
        text = bigFont.render("SPACE INVADERS", True, PURPLE)
        screen.blit(text, [60, 45])

        text = bigFont.render("SPACE INVADERS", True, BEIGE)
        screen.blit(text, [60, 50])

        text = font.render("CLICK ANYWHERE TO START", True, WHITE)
        screen.blit(text, [130, 130])

        

        # INSTRUCTIONS 
        instructions1 = "This is a multiplayer game. One person can play as the red alien. As the"
        
        instructions2 = "other plays as the spaceship. Red alien user will use ASD for controls. " 
        
        instructions3 = "A will move them left, D will move them right and S will shoot lazers at  "

        instructions4 = "the enemy. Spaceship user will use the key buttons. Left key will move them"
        
        instructions5 = "left, right key will move them right and the space bar will shoot lazers at the "

        instructions6 = "enemies. The goal is to defeat the opposing team before they defeat you. "

        instructions7 = "Red alien will have allies defending him but will have less health. The"

        instructions8 = "aliens's allies will have random spawns everytime you play. The spaceship"

        instructions9 = "will have no allies defending him but will have more health and faster bullets."
      
        text = font.render("Game Instructions", True,WHITE)
        screen.blit(text, [182,220])

        text = smallFont.render(instructions1, True,WHITE)
        screen.blit(text, [26,260])
        text = smallFont.render(instructions2, True,WHITE)
        screen.blit(text, [26,280])
        text = smallFont.render(instructions3, True,WHITE)
        screen.blit(text, [26,300])
        text = smallFont.render(instructions4, True,WHITE)
        screen.blit(text, [26,320])
        text = smallFont.render(instructions5, True,WHITE)
        screen.blit(text, [26,340])
        text = smallFont.render(instructions6, True,WHITE)
        screen.blit(text, [26,360])
        text = smallFont.render(instructions7, True,WHITE)
        screen.blit(text, [26,380])
        text = smallFont.render(instructions8, True,WHITE)
        screen.blit(text, [26,400])
        text = smallFont.render(instructions9, True,WHITE)
        screen.blit(text, [26,420])

        text = smallFont.render('© KARMA W 2021', True, WHITE)
        screen.blit(text, [230,480])


    # CREDITS
    if page_number == 2:
        text = bigFont.render("CREDITS", True, WHITE)
        screen.blit(text, [170, 50])

        text = font.render("CLICK ANYWHERE TO START", True, WHITE)
        screen.blit(text, [125, 140])

        text = font.render("Game Designed by: Karma Woeser", True,WHITE)
        screen.blit(text, [80, 225])
 
        text = font.render("Written by: Karma Woeser", True, WHITE)
        screen.blit(text, [80, 250])
        text = font.render("Special Effects by: Karma Woeser", True, WHITE)
        screen.blit(text, [80, 275])

        text = font.render("Animations/Graphics by: Karma Woeser", True, WHITE)
        screen.blit(text, [80, 300])

        

    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
 
 


# --- Classes
'''
This class respersents a block. This block will be the small white aliens
'''
class Block(pygame.sprite.Sprite):
    """ This class represents the little Alien's The ones that protect the Alien Player. """
    def __init__(self, color):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        image = pygame.image.load("smallAlien.png").convert()
        image.set_colorkey(BLACK)

        self.image = pygame.transform.scale(image, (50, 50))
        
        self.rect = self.image.get_rect()


'''
This class respersents a player. This player will be the big red alien.
'''
class Alien(pygame.sprite.Sprite):
    """ This class represents the Alien Player. """
    def __init__(self, x, y, health):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 

        player_image = pygame.image.load("alienBoss.png").convert()
        player_image.set_colorkey(BLACK)

        self.image = pygame.transform.scale(player_image, (150, 100))
        # self.image = pygame.Surface([20, 20])
        # self.image.fill(RED)
 
        self.rect = self.image.get_rect()
 
        self.rect.x = x
        self.rect.y = y
 
        # Speed vector
        self.change_x = 0
        self.change_y = 0

        self.health = health


    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y




'''
This class respersents a player. This player will be the spaceship.
''' 
class Player(pygame.sprite.Sprite):
    """ This class represents the Spaceship Player. """
 
    def __init__(self, x, y, health):
        """ Set up the player on creation. """
        # Call the parent class (Sprite) constructor
        super().__init__()
 

        player_image = pygame.image.load("space-invaders.png").convert()
        player_image.set_colorkey(BLACK)

        self.image = pygame.transform.scale(player_image, (60, 60))
        # self.image = pygame.Surface([20, 20])
        # self.image.fill(RED)
 
        self.rect = self.image.get_rect()
        

        self.rect.x = x
        self.rect.y = y
 
        # Speed vector
        self.change_x = 0
        self.change_y = 0

        self.health = health
        
        # if x == 600:
        #   self.change_x = 0
        # elif y == 100:
        #   self.change_y = 0

    def changespeed(self, x, y):
        """ Change the speed of the player"""
        self.change_x += x
        self.change_y += y
 
    def update(self):
        """ Find a new position for the player"""
        self.rect.x += self.change_x
        self.rect.y += self.change_y




'''
This class respersents the bullet that is shot from the spaceship. 
'''
class Bullet(pygame.sprite.Sprite):
    """ This class represents the Spaceships bullet . """
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([4,8])

        self.image.fill(GREEN)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.y -= 3


        '''
        If the bullet collides with the alien it removes 10 from the alien_players health. While also removing the bullet from the game. But this makes it so the alien isn't removed from the game.
        '''
        if pygame.sprite.spritecollide(self, alien_player_list, False):
          self.kill()
          alien_player.health -= 10

          if alien_player.health == 0:
            print("ALIEN LOSES!!! SPACESHIP WINS!!!")
            quit()

           



'''
This class respersents the bullet that is shot from the red alien. 
'''
class BadBullet(pygame.sprite.Sprite):
    """ This class represents the Alien's bullet"""
    def __init__(self):
        # Call the parent class (Sprite) constructor
        super().__init__()
 
        self.image = pygame.Surface([4,8])
        self.image.fill(RED)
 
        self.rect = self.image.get_rect()
 
    def update(self):
        """ Move the bullet. """
        self.rect.y += 2

        if pygame.sprite.spritecollide(self, player_list, False):
          self.kill()
          player.health -= 10

          if player.health == 0:
            print("SPACESHIP LOSES!!! ALIEN WINS!!!")
            quit()
           
            


screen = pygame.display.set_mode(size)
 

background_image = pygame.image.load("background.jpg").convert()
pygame.mouse.set_visible(False)
pygame.display.set_caption("Space Invaders Multiplayer")


# --- Sprite lists
# This is a list of every sprite. All blocks and the player block as well.
all_sprites_list = pygame.sprite.Group()
 
# List of each block in the game
block_list = pygame.sprite.Group()
player_list = pygame.sprite.Group()
alien_player_list = pygame.sprite.Group()

# List of each bullet
bullet_list = pygame.sprite.Group()
alien_bullets = pygame.sprite.Group()




# --- Create the sprites
for i in range(30):
    # This makes a block

    block = Block(BLACK)

    # Set a random location for the block
    block.rect.x = random.randrange(550)
    block.rect.y = random.randrange(150, 325)
 
    # Add the block to the list of objects
    block_list.add(block)
    all_sprites_list.add(block)


# Creates the alien_player
alien_player = Alien(215, 50, 100)
alien_player_list.add(alien_player)
all_sprites_list.add(alien_player)

# Creates the spaceship_player
player = Player(260, 425, 150)
player_list.add(player)
all_sprites_list.add(player)


# Loop until the user clicks the close button.
done = False
 

# -------- Main Program Loop -----------
while not done:
    # --- Event Processing
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # Set the speed based on the key pressed
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.changespeed(-10, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(10, 0)
            elif event.key == pygame.K_a:
                alien_player.changespeed(-10,0)
            elif event.key == pygame.K_d:
                alien_player.changespeed(10,0)


            #PLAYER BULLETS
            elif event.key == pygame.K_SPACE:
                # When the user clicks on the space bar it will fire a bullet from the ship
                bullet = Bullet()

                # Controls where the bullet comes from. 
                bullet.rect.x = player.rect.x + 29
                bullet.rect.y = player.rect.y 

                # Add the bullet to the lists
                all_sprites_list.add(bullet)
                bullet_list.add(bullet)

              
            #ALIEN BULLETS
            elif event.key == pygame.K_s:
                # When the user clicks on the s key it will fire a bullet from the ship
                alienBullet = BadBullet()


                # Controls where the bullet comes from. 
                alienBullet.rect.x = alien_player.rect.x + 73
                alienBullet.rect.y = alien_player.rect.y + 65


                # Add the bullet to the lists
                all_sprites_list.add(alienBullet)
                alien_bullets.add(alienBullet)

          
        # Reset speed when key goes up
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                player.changespeed(10, 0)
            elif event.key == pygame.K_RIGHT:
                player.changespeed(-10, 0)
            elif event.key == pygame.K_a:
                alien_player.changespeed(10,0)
            elif event.key == pygame.K_d:
                alien_player.changespeed(-10,0)            


    # --- Game logic
    # Call the update() method on all the sprites
    all_sprites_list.update()
 

    #PLAYER BULLET
    # Mechanics for player bullet; gets rid of the aliens when it collides with bullet
    for playerBullet in bullet_list:
      # See if it hit a block
      block_hit_list = pygame.sprite.spritecollide(playerBullet, block_list, True)

      # When the bullet hits the target it get removes from the sprite list; so it gets removed from the game
      for block in block_hit_list:
        all_sprites_list.remove(playerBullet)


    # SETS BOUNDARIES SO SHIPS DON'T MOVE OFF SCREEN
    if player.rect.x <= 0:
      player.rect.x = 0
    elif player.rect.x >= 540:
      player.rect.x = 540

    if alien_player.rect.x <= -25:
      alien_player.rect.x = -25
    elif alien_player.rect.x >= 475:
      alien_player.rect.x = 475



    screen.fill(BLACK)
    screen.blit(background_image, [0, 0])


    # Draws all the spites
    all_sprites_list.draw(screen)
 

    # ON SCREEN TEXT
    # SPACE SHIP HEALTH
    font = pygame.font.SysFont('ITC Machine Font', 25, True, False)
    text = font.render("Spaceship Health: {}".format(player.health),True, WHITE)
    screen.blit(text, [10, 15])


    # ALIEN HEALTH
    font = pygame.font.SysFont('ITC Machine Font', 25, True, False)
    text = font.render("Alien Health: {}".format(alien_player.health),True, WHITE)
    screen.blit(text, [430, 15])



    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)


pygame.quit()

