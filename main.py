import pygame, sys

# import numpy as np

pygame.init()

window_width = 500
window_height = 500
WINNER_FONT = pygame.font.SysFont('comicsans', 40)

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Tic-Tac-Toe')
rows = 3
cols = 3
turn = 0
run = True
game_over = False

black = (0, 0, 0)
white = (255, 255, 255)
circle_radius = 35
circle_width = 5
background_image = pygame.image.load('background image.jpg')
# game_board = np.zeros((rows, cols))
game_board = list(map(lambda x: [0] * 3, range(3)))
print(game_board)
background = (50, 70, 150)
grid_colour = (255, 255, 255)
grid_thickness = 3


def create_board():
    window.fill(background)
    window.blit(background_image, (0, 0))
    pygame.draw.line(window, grid_colour, (100, 100), (400, 100), grid_thickness)
    pygame.draw.line(window, grid_colour, (100, 100), (100, 400), grid_thickness)
    pygame.draw.line(window, grid_colour, (100, 400), (400, 400), grid_thickness)
    pygame.draw.line(window, grid_colour, (400, 400), (400, 100), grid_thickness)
    pygame.draw.line(window, grid_colour, (200, 100), (200, 400), grid_thickness)
    pygame.draw.line(window, grid_colour, (300, 100), (300, 400), grid_thickness)
    pygame.draw.line(window, grid_colour, (100, 200), (400, 200), grid_thickness)
    pygame.draw.line(window, grid_colour, (100, 300), (400, 300), grid_thickness)
    # pygame.draw.circle(window, black, (int(3 * 100 + 50), int(3 * 100 + 50)), circle_radius, circle_width)


def insert_char(row, col, player):
    game_board[row][col] = player
    #game_objects()


def available_cells(row, col):
    if game_board[row][col] == 0:
        return True
    else:
        return False


def is_board_complete():
    for row in range(rows):
        for col in range(cols):
            if game_board[row][col] == 0:
                return False
    return True


def game_objects():
    for row in range(rows):
        for col in range(cols):
            if game_board[row][col] == 1:
                pygame.draw.circle(window, black, (int(col * 100 + 150), int(row * 100 + 150)), circle_radius,
                                   circle_width)
                pygame.display.update()
            elif game_board[row][col] == 2:
                pygame.draw.line(window, grid_colour, (col * 100 + 110, row * 100 + 190),
                                 (col * 100 + 190, row * 100 + 110), grid_thickness)
                pygame.draw.line(window, grid_colour, (col * 100 + 110, row * 100 + 110),
                                 (col * 100 + 190, row * 100 + 190), grid_thickness)
                pygame.display.update()

def vertical_win_line(col, player):
    x_posn = col * 100 + 150
    if player == 1:
        pygame.draw.line(window, grid_colour, (x_posn,110),(x_posn, window_height - 110), grid_thickness)
        pygame.display.update()
    elif player == 2:
        pygame.draw.line(window, black, (x_posn, 110), (x_posn, window_height - 110), grid_thickness)
        pygame.display.update()

def horizontal_win_line(row,player):
    y_posn = row * 100 + 150
    if player == 1:
        pygame.draw.line(window, grid_colour, (110, y_posn),(window_height - 110, y_posn), grid_thickness)
        pygame.display.update()
    elif player == 2:
        pygame.draw.line(window, black, (110, y_posn), (window_height - 110, y_posn), grid_thickness)
        pygame.display.update()

#diag line working
#Still need to draw over elements
def diag_win_line(player, down_slope=True):
    if down_slope:
        if player == 1:
            pygame.draw.line(window, grid_colour, (125, 125), (window_height - 125, window_height - 125), grid_thickness)
            pygame.display.update()
        else:
            pygame.draw.line(window, black, (125, 125), (window_height - 125, window_height - 125), grid_thickness)
            pygame.display.update()
    else:
        if player == 1:
            pygame.draw.line(window, grid_colour, (125, window_height - 125), (window_height - 125, 125), grid_thickness)
            pygame.display.update()
        else:
            pygame.draw.line(window, black, (125, window_height - 125), (window_height - 125, 125), grid_thickness)
            pygame.display.update()

def row_equivalence(player):
    for i in range(len(game_board)):
        if game_board[i][0] == player and game_board[i][1] == player and game_board[i][2] == player:
            horizontal_win_line(i, player)
            return True
    return False

def col_equivalence(player):
    for i in range(len(game_board)):
        if game_board[0][i] == player and game_board[1][i] == player and game_board[2][i] == player:
            vertical_win_line(i,player)
            return True
    return False

def diag_equivalence(player):
    if (game_board[0][0] == player and game_board[1][1] == player and game_board[2][2] == player):
        diag_win_line(player, True)
        return True
    elif game_board[0][2] == player and game_board[1][1] == player and game_board[2][0] == player:
        diag_win_line(player, False)
        return True
    else:
        return False

def determine_winner(player):
    if row_equivalence(player) or col_equivalence(player) or diag_equivalence(player):
        player = "Player " + str(player) + " has won"
        draw_text = WINNER_FONT.render(player,1,(31,217,230))
        window.blit(draw_text , (window_width//2 - draw_text.get_width()//2, window_height//2 - draw_text.get_height()//2))
        pygame.display.update()
        pygame.time.delay(2000)
        return True
    else:
        return False


#this is a button function to create buttons with
def buttons(mes, x, y, width, height, interactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()#gets the mouse position
    click = pygame.mouse.get_pressed()#gets the mouse click
    buttonShape = pygame.Rect(x,y,width,height)

    if x+width > mouse[0] > x and y+height > mouse[1] > y:
        pygame.draw.rect(window, interactive_color, buttonShape)#drawing a rectangle with a change in color
        if click[0] == 1 and action != None: #checking for a click and action
            action()#action is a function object
    else:
        pygame.draw.rect(window, active_color, buttonShape)#drawing a rectangle

    smallText =pygame.font.Font("freesansbold.ttf", 20)
    textSurface = smallText.render(mes, 1 ,black)
    textRect = textSurface.get_rect()
    textRect.center = (x+ width/2,y+ height/2)
    window.blit(textSurface, textRect)

def gameOverFunction():

    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 

        #window.fill(white)
        window.blit(background_image, (0, 0))
        largeText = pygame.font.Font('freesansbold.ttf', 75)
        TextSurface = largeText.render("TIC TAC TOE", 1, black)
        textRect = TextSurface.get_rect()
        textRect.center = (250,50)
        window.blit(TextSurface,textRect)
        buttons("MAIN MENU",180,150,160,50,(20,49,250),(100,67,198),main)
        buttons("PLAY AGAIN",180,250,160,50,(20,49,250),(100,67,198),single_player)
        buttons("QUIT",180,350,160,50,(20,49,250),(100,67,198),quitGame)
        
        # draw in game objects that were previously inputted
            
            
            
        
        pygame.display.update()
    pygame.quit()
    sys.exit()

def playAgain():
    for i in range(rows):
        for j in range(cols):
            game_board[i][j] = 0

    single_player() 

def single_player():
    game_over = False
    turn = 0
    run = True
    for i in range(rows):
        for j in range(cols):
            game_board[i][j] = 0

    while run:
        create_board()       
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN and game_over == False:
                x_posn = event.pos[0]
                y_posn = event.pos[1]
                clicked_row = int(y_posn // 100) - 1
                clicked_col = int(x_posn // 100) - 1
                
                if turn % 2 == 0:
                    if available_cells(clicked_row, clicked_col):
                        insert_char(clicked_row, clicked_col, 1)
                else:
                    if available_cells(clicked_row, clicked_col):
                        insert_char(clicked_row, clicked_col, 2)

                game_objects()
                if determine_winner(turn%2 + 1):
                    game_over = True
                    

                turn += 1

                if is_board_complete():
                    player = "THE GAME HAS TIED"
                    draw_text = WINNER_FONT.render(player,1,(31,217,230))
                    window.blit(draw_text , (window_width//2 - draw_text.get_width()//2, window_height//2 - draw_text.get_height()//2))
                    pygame.display.update()
                    pygame.time.delay(2000)
                    game_over = True
            
            if game_over == True:
                gameOverFunction()
                    
            game_objects()
            pygame.display.update()


def quitGame():
    pygame.quit()
    quit()

def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 

        #window.fill(white)
        window.blit(background_image, (0, 0))
        largeText = pygame.font.Font('freesansbold.ttf', 75)
        TextSurface = largeText.render("TIC TAC TOE", 1, black)
        textRect = TextSurface.get_rect()
        textRect.center = (250,50)
        window.blit(TextSurface,textRect)
        buttons("SINGLE PLAYER",180,150,160,50,(20,49,250),(100,67,198),None)
        buttons("MULTIPLAYER",180,250,160,50,(20,49,250),(100,67,198),single_player)
        buttons("QUIT",180,350,160,50,(20,49,250),(100,67,198),quitGame)
        
        # draw in game objects that were previously inputted
            
            
            
        
        pygame.display.update()
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()