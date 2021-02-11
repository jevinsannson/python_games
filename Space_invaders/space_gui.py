import pygame
import pygame_gui
import game_db

pygame.init()
pygame.display.set_caption('Cybersquare')
window_surface = pygame.display.set_mode((800, 600))
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#ffffff'))

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


is_running = True
clock = pygame.time.Clock()

while is_running:
    time_delta = clock.tick(60)/1000.0

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

