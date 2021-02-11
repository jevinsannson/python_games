import pygame, sys
import random
import math
import pygame_gui
import game_db

pygame.init()
pygame.display.set_caption('Robo Tube')
window_surface = pygame.display.set_mode((800, 600))
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#ffffff'))
logged_user = ""

manager = pygame_gui. UIManager((800, 600))

panel_select= pygame_gui.elements.ui_panel.UIPanel (pygame.Rect((150, 200), (550, 150)),
                                               manager= manager, starting_layer_height=3)


btn_show_login= pygame_gui.elements.UIButton (relative_rect=pygame.Rect((100, 50), (100, 25)),
 text='Login',manager=manager, container=panel_select)

             
btn_show_register= pygame_gui.elements.UIButton (relative_rect=pygame.Rect((300, 50), (100, 25)),
 text='Register',manager=manager, container=panel_select)
                                             
# Registration form
panel_reg = pygame_gui.elements.ui_panel.UIPanel(pygame.Rect((150, 100), (550, 350)), 
                                                manager= manager, starting_layer_height=2)

lbl_name = pygame_gui.elements.ui_label.UILabel(relative_rect= pygame.Rect((50, 50), (200, 25)), 
                                                manager= manager, text="Full name", container=panel_reg)
txt_name = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect= pygame.Rect((300,50), (200, 50)), 
                                                                manager= manager, container=panel_reg)

lbl_uname = pygame_gui.elements.ui_label.UILabel(relative_rect= pygame.Rect((50, 100), (200, 25)), container=panel_reg,
                                                manager= manager, text="Email/ Username" )
txt_username = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect= pygame.Rect((300, 100), (200, 50)), 
                                                manager= manager, container=panel_reg)

lbl_passwrod = pygame_gui.elements.ui_label.UILabel(relative_rect= pygame.Rect((50, 150), (200, 25)), container=panel_reg,
                                                manager= manager, text="Password")
txt_password = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect= pygame.Rect((300, 150), (200, 50)), 
                                                manager= manager, container=panel_reg)

lbl_gender = pygame_gui.elements.ui_label.UILabel(relative_rect= pygame.Rect((50, 200), (200, 25)), container=panel_reg,
                                                manager= manager, text="Gender")
dd_lst_gender = pygame_gui.elements.ui_drop_down_menu.UIDropDownMenu(relative_rect= pygame.Rect((300, 200), (200, 25)), 
                                                manager= manager, options_list=["male", "female"],
                                                starting_option="male", container=panel_reg)
btn_signup = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 250), (100, 25)), text='Sign up',
                                                manager=manager, container=panel_reg)



panel_reg_msg = pygame_gui.elements.ui_panel.UIPanel(pygame.Rect((40, 280), (450, 50)), 
                                                manager= manager, starting_layer_height=3, container=panel_reg)
lbl_reg_message = pygame_gui.elements.ui_label.UILabel(relative_rect= pygame.Rect((5, 5), (300, 25)), container=panel_reg_msg,
                                                manager= manager, text="You have registered successfully")
#This line should be corrected
lbl_reg_error_message = pygame_gui.elements.ui_label.UILabel(relative_rect= pygame.Rect((5, 5), (400, 25)), container=panel_reg_msg,
                                                manager= manager, text="")
btn_play_game = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((300, 5), (100, 25)), text='Play game',
                                                manager=manager, container=panel_reg_msg)
panel_reg_msg.hide()
panel_reg.hide()
                                                                                   

# Login panel
panel_login = pygame_gui.elements.ui_panel.UIPanel(pygame.Rect((150, 100), (550, 250)), 
                                                manager= manager, starting_layer_height=1)

lbl_luname = pygame_gui.elements.ui_label.UILabel(relative_rect= pygame.Rect((50, 50), (200, 25)), container=panel_login,
                                                manager= manager, text="Email/ Username" )
txt_lusername = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect= pygame.Rect((300, 50), (200, 50)), 
                                                manager= manager, container=panel_login)
lbl_lpasswrod = pygame_gui.elements.ui_label.UILabel(relative_rect= pygame.Rect((50, 100), (200, 25)), container=panel_login,
                                                manager= manager, text="Password")
txt_lpassword = pygame_gui.elements.ui_text_entry_line.UITextEntryLine(relative_rect= pygame.Rect((300, 100), (200, 50)), 
                                                manager= manager, container=panel_login)
btn_login = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((250, 150), (100, 25)), text='Login',
                                                manager=manager, container=panel_login)
lbl_login_msg = pygame_gui.elements.ui_label.UILabel(relative_rect= pygame.Rect((100, 200), (250, 25)), container=panel_login,
                                                manager= manager, text="Incorrect username or password")
                                                
panel_login.hide()

# Player spaceship
playerImg = pygame.image.load("images/spaceship.png")
#for changing the image space ship

playerImg = pygame.transform.scale(playerImg, (64, 128))
playerX = 0
playerY = 430
playerX_change = 0


# Player enemy
enemyImg = pygame.image.load("images/enemy1.png")
enemyImg = pygame.transform.scale(enemyImg, (64, 64))
enemyX = random.randint(0,735)
enemyY = random.randint(100,200)
enemyX_change = 1
enemyY_change = 30

# Bullet
bulletImg = pygame.image.load("Bullet.png")
#this is the code for importing the bullet

bulletImg = pygame.transform.scale(bulletImg, (50, 50))
bulletX = 0
bulletY = 540
bulletX_change = 0
bulletY_change = 10 #Speed of the bullet
bullet_state = "ready" # Ready - Can't see bullet, Fire - Bullet is moving

# Score
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 100
textY = 100

def show_score(x, y):
    display_score = font.render("Score: " + str(score), True, (0, 255, 0))
    window_surface.blit(display_score, (x,y))


def player(x, y):
    window_surface.blit(playerImg,(x, y))


def emeny(x, y):
    window_surface.blit(enemyImg,(x, y))


def fire_bullet(x, y): # Movement of bullet
    global bullet_state
    bullet_state = "fire"
    window_surface.blit(bulletImg,(x+16, y+10))


# Check bullet hits enemy
def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX,2)) + (math.pow(enemyY-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

play=0

is_running = True
clock = pygame.time.Clock()

while is_running:
    
    
    if play==1:

        window_surface.fill((0, 0, 0))
        # background
        window_surface.blit(background, (0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()


            # Handle key strokes left and right
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    print("Left arrow is pressed")
                    playerX_change = -5

                if event.key == pygame.K_RIGHT:
                    print("Right arrow is pressed")
                    playerX_change = 5

                if event.key == pygame.K_SPACE:
                    print("Space bar pressed")
                    if bullet_state is "ready":
                        bulletX = playerX
                        fire_bullet(playerX, bulletY)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    print("Keystorke has been released")
                    playerX_change = 0
        
        playerX += playerX_change

        # Set the movement limit to size of the window
        if playerX < 0: # Move the player to zero when the player goes beyond left edge
            playerX = 0
        elif playerX > 736: # Move the player inside the screen when the player goes beyond right edge
            playerX = 736

        # Enemy movement
        enemyX += enemyX_change
        if enemyX < 0:
            enemyX_change = 1  # Change the direction of movement to right when reaches at left side
            enemyY += enemyY_change # Change Y position of the enemy
        elif enemyX > 736:
            enemyX_change = -1 # Change the direction of movement to left when reaches at right side
            enemyY += enemyY_change

        # Bullet movement
        if bulletY < 0:
            bulletY = 480
            bullet_state = "ready"

        if bullet_state is "fire":
            fire_bullet(bulletX, bulletY)
            bulletY -= bulletY_change

        #Collision
        collision = isCollision(enemyX, enemyY, bulletX, bulletY)
        # Reset the bullet and update score after hitting the emeny
        if collision:
            bulletY = 480
            bullet_state = "ready"
            score += 1
            print(score)
            enemyX = random.randint(0,735)
            enemyY = random.randint(100,200)

        # show the  score
        show_score(textX, textY)

        # Update positions
        player(playerX, playerY)
        emeny(enemyX, enemyY)
        pygame.display.update()




    else:  
        
        time_delta = clock.tick(60)/1000.0
        #print('Inside Else')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                pygame.quit()

            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == btn_show_login:
                        panel_select.hide()
                        panel_login.show()
                        lbl_login_msg.hide()
                    if event.ui_element == btn_play_game:
                        background = pygame.image.load("images/background.png")
                        play=1    
                    if event.ui_element == btn_show_register:
                        panel_select.hide()
                        panel_reg.show()
                        panel_reg_msg.hide()    
                    if event.ui_element == btn_signup:
                        name = txt_name.get_text()
                        username = txt_username.get_text()
                        user_password = txt_password.get_text()
                        gender = dd_lst_gender.selected_option
                        print(name, username, user_password, gender)
                        #result= game_db.register (username, user_password, name, gender) 
                        
                        check=1
                        message='Please Enter'

                        if not username:
                            print('Please Enter Username') 
                            message=message+' Username'
                            check=0

                        if not user_password:
                            print('Please Enter Password')
                            message=message+' Password'   
                            check=0

                        if not name:
                            print('Please Enter Fullname')
                            message=message+' Fullname'
                            check=0

                        if check==1:
                            result=game_db.register(username, user_password, name, gender)
                            if result:
                                #logged_user = username
                                panel_reg_msg.show()
                                lbl_reg_message.show()
                                btn_play_game.show()
                                lbl_reg_error_message.hide()
                                print('Registration Sucessfull')
                                logged_user = username
                                
                        else:
                            print(message)
                            panel_reg_msg.show()
                            lbl_reg_message.hide()
                            btn_play_game.hide()
                            lbl_reg_error_message.set_text(message)
                            lbl_reg_error_message.show()
                                

                        

                    if event.ui_element == btn_login:
                        username = txt_lusername.get_text() #store username in the textbox into a variable
                        user_password = txt_lpassword.get_text() #store password in the textbox into a variable
                        print(username, user_password)
                        
                        status=1
                        message="Please Enter"
                        if not username:
                            print('Please Enter Username')
                            message=message+' Username'
                            status=0    

                        if not user_password:
                            print(' Password')
                            message=message+' Password'
                            status=0    

                        if status==1:
                            result=game_db.login(username, user_password) # calling a function named login inside the module game_db
                            if result:
                                print("Login Success")
                                background = pygame.image.load("images/background.png")
                                play = 1
                                logged_user = username
                                lbl_login_msg.set_text("Correct Username And Password") 
                            else:
                                lbl_login_msg.show()
                                print("Login Fail")
                        else: 
                            lbl_login_msg.set_text(message)
                            lbl_login_msg.show()

            manager.process_events(event)    
        manager.update(time_delta)
        window_surface.blit(background, (0, 0))
        manager.draw_ui(window_surface)
    pygame.display.update()