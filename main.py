import pygame
import time 
import random
pygame.font.init()


WIDTH, HEIGHT = 1000,800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hexa planet")

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

SHIPP = pygame.image.load("ship.jpeg")
SHIPP = pygame.transform.scale(
    SHIPP,
    (PLAYER_WIDTH, PLAYER_HEIGHT)
)

ENMY_IMG = pygame.image.load("enemy.jpeg")
ENMY_IMG = pygame.transform.scale( 
                            ENMY_IMG,
                            (40, 40)
)
    
BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))


PLAYER_VEL = 5
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3
# here i wanted to add bullet with th eplayer to kill the enemy
BULLET_VEL = 7
BULLET_WIDTH = 5
BULLET_HEIGHT = 10
ENEMY_VEL = 2
# here i wanted to add best score to the game 
best_score = 0
# here i wanted to add a boss to the game 
Hexor = None
Hexor_health = 0
hexor_bullets = []


FONT = pygame.font.SysFont("comicsans", 30)


# this is the fancution of the drawing of the characters of the game and what is them size
def draw(player, elapsed_time, stars, score, lives , best_score, bullets, levl, Hexor_health):
    WIN.blit(BG, (0, 0))
    
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))
    
    score_text = FONT.render(f"Score: {score}", 1, "white")
    WIN.blit(score_text, (10, 50))
    lives_text = FONT.render(f"Lives: {lives}", 1, "white")
    WIN.blit(lives_text, (10, 90))
    WIN.blit(SHIPP, (player.x, player.y))
    
    levl_text = FONT.render(
        f"level: {levl}",
        1,
        "white"
    )
    WIN.blit(levl_text, (10,170))
    
    best_text = FONT.render(
        f"Best: {best_score}",
        1,
        "white"
    )
    WIN.blit(best_text, (10, 130))
    
    if Hexor:
        pygame.draw.rect(
            WIN,
            "purple",
            Hexor
               
        )
        
    if Hexor:
        pygame.draw.rect(WIN,"red", (300,20,400,20))
        pygame.draw.rect( WIN, "green" , (300, 20 , 400 * (Hexor_health /20), 20) )
    
    for star in stars:
        pygame.draw.circle(WIN, "white", star.center, 5)
    
    for bullet in bullets:
        pygame.draw.rect(WIN, "yellow", bullet)
    
    for enemy in enemies:
        WIN.blit(
            ENMY_IMG,
            (enemy.x, enemy.y)
            
        )
    
    pygame.display.update()

# this is the fanction of the game over page with quit or play again

def game_over():
    while True:
        WIN.fill(( 0 , 0 , 0 ))
        
        text= FONT.render (" U lostt !!, Game is over -- press R to play again or press Q to Quit", 1, "white")
        WIN.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_r]:
            return True
        
        if keys[pygame.K_q]:
            return False

# this is the fanction of the start menu to make an awasome game

def strt_menu():
    while True:
        WIN.blit(BG, (0, 0))
        
        title = FONT.render("Hexa planet", 1, "white")
        start = FONT.render(" U caan start your Fight With ENTER", 1, "white")
        quit_text = FONT.render("Hexor awaits. Press Q to retreat.", 1, "white")
        
        WIN.blit(title, (WIDTH/2 - title.get_width()/2, 250))
        WIN.blit(start, (WIDTH/2 - start.get_width()/2, 320))
        WIN.blit(quit_text, (WIDTH/2 - quit_text.get_width()/2, 370))
        
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RETURN]:
            return True
        
        if keys[pygame.K_q]:
            return False

# this is fanction when user wanted to puase the game

def puse():
    
    pused = True
    while pused:
        text = FONT.render("Hexor await you  - click R > Resume -  or Q > Quit" , 1 , "white")
        
        WIN.blit(text, (200, 350))
        pygame.display.update()
    
        for event in pygame.event.get():
        
             if event.type == pygame.QUIT:
                 return False
             
        keys = pygame.key.get_pressed()
    
        if keys[pygame.K_r]:
            return True
        if keys[pygame.K_q]:
            return False

# this is the main fantiion that contains the most of the code of the game to control or laws
def main():
    run = True
    global bullets, enemies, best_score, Hexor, Hexor_health, Hexor_dir
    bullets= []
    enemies = []
    Hexor = None
    Hexor_health = 0
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT,
                         PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    
    star_add_increment = 2000
    star_count = 0
    
    
    stars = []
    hit = False
    score = 0
    levl = 1
    lives = 3
    
    def reset_game():
        return [], 0, 3, False, 0, time.time()
    shott_delay = 0
    while run:
        if shott_delay > 0:
            shott_delay -= 1
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        curent_star_vel = STAR_VEL + min(6, int(elapsed_time // 15))
        
        if star_count > star_add_increment:
            enemy_x = random.randint(0, WIDTH - STAR_WIDTH)
            
            enemy = pygame.Rect(enemy_x, -20, 40, 40)
            enemies.append(enemy)
            
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT,
                                   STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
                
            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        for bullet in bullets[:]:
            bullet.y -= BULLET_VEL
    
            if bullet.y < 0:
                 bullets.remove(bullet)
                 continue
            
            if Hexor and bullet.colliderect(Hexor):
                bullets.remove(bullet)
                
                Hexor_health -=1
                
                if Hexor_health <= 0:
                    Hexor = None
                    score += 20
                    levl = score // 10 + 1
                continue
            for enemy in enemies[:]:
                if bullet.colliderect(enemy):
                    enemies.remove(enemy)
                    bullets.remove(bullet)
                    score+= 1
                    levl = score // 10 + 1
                    if score > best_score:
                        best_score = score 
                    if score > 0 and score % 20 == 0 and Hexor is None: 
                        Hexor = pygame.Rect(
                            WIDTH // 2 - 75,
                            50,
                            150,
                            80
                        )
                        Hexor_health = 20    
                        Hexor_dir = 1  
                    
                    break
                     

        
        for enemy in enemies[:]:
            enemy.y+= ENEMY_VEL + (levl - 1)
            
            if enemy.y > HEIGHT:
                enemies.remove(enemy)
            
            if enemy.colliderect(player):
                lives -= 1
                enemies.remove(enemy)
                
                if lives <= 0:
                    hit = True
                    break 
        
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_ESCAPE]:
            if puse():
                pass
        
            else:
                run = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and shott_delay == 0:
            bullet = pygame.Rect(
                player.x + player.width // 2,
                player.y,
                BULLET_WIDTH,
                BULLET_HEIGHT
            )
            bullets.append(bullet)
            shott_delay = 15
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
                player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
                player.x += PLAYER_VEL
        
        if Hexor:
            Hexor.x += Hexor_dir * 3
        
            
            if Hexor.x < 0:
                Hexor_dir = 1
                
            elif Hexor.x + Hexor.width >= WIDTH:
                Hexor_dir = -1
                
        for star in stars[:]:
                star.y += curent_star_vel
                if star.y > HEIGHT:
                    stars.remove(star)
                    
                elif star.colliderect(player):
                    lives -= 1
                    stars.remove(star)
                if lives <= 0:
                    hit = True
                    break
            
        if hit:
            
            if game_over():
                return main()
            else:
                run = False
                
            
        draw(player, elapsed_time, stars, score, lives , best_score, bullets, levl, Hexor_health)
            
    pygame.quit()
    
    
if __name__ == "__main__":
    if strt_menu():
        main()