
# [Step 1]: Import a module.
#           The first thing you need to do is import Python's Random module. To import the whole
#           module, you simply need to type import followed by the name of the module. We'll use Random in a couple
#           of functions later in the code.

import random
import pgzrun


# [Step 2]: Declare the constants
#           Constants are variables that are usually declared at the start of a program. 
#           They are called constants because their values shouldn't change throughout the program.
#           Programmers use capital letters when naming them to let other programmers know not to change their values.
#           This is known as a "naming convention" - a rule that most programmers agree on, so that everyone's code
#           looks imilar and is easier to understand.

FONT_COLOR = (255, 255, 255)    # This sets the font color of the message that is displayed at the end of the game
WIDTH = 800                     # Size (width) of the game window
HEIGHT = 600                    # Size (height) of the game window
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTRE = (CENTER_X, CENTER_Y)
FINAL_LEVEL = 6                 # This contant defines the number of levels in the game
START_SPEED = 10                # This sets the speed at which the stars move down the screen
COLORS = ["green", "blue"]      # This line sets the color of the stars that should not be clicked


# [Step 3]: Declare the global variables
#           Like constants, global variables are usually declared at the top of the program, but unlike constants,
#           their values can change throughout the code. In this game, you'll use these global variables to track
#           the game's progress.
game_over = False       # this variable will keep track of if the game is over or not
game_complete = False   # this variable will keep track of if the game is over or not
current_level = 1       # this variable will keep track of what level the player is on
stars = []              # this list will keep track of the stars on the screen
animations = []         # this list will keep track of the stars on the screen


# [Step 4]: Draw the stars
#           Now it's time to defin the first function. You'll use the draw() function to add some stars and display
#           messages on the screen.

def draw():
    global stars, current_level, game_over, game_complete # these are the global variables used in this function
    
    screen.clear()
    
    screen.blit("space", (0, 0))    # this adds a background image to the game window
    # when the game is over or complete, the following two blocks display the relevant message on the screen
    if game_over:
        display_message("GAME OVER!", "Try again.")
    elif game_complete:
        display_message("YOU WON!", "Well done.")
    # this block draws the stars on the screen
    else:
        for star in stars:
            star.draw() 


# [Step 5]: Define the update() function
#           The draw() function that you defined above will have nothing to draw unless you create the stars.
#           Define the update() function next to check if there are nay stars in the stars list. If there 
#           aren't, it should call the make_stars() function.
def update():
    global stars
    if len(stars) == 0:
        stars = make_stars(current_level)



# [Step 6]: Define the make_stars() function
#           This function creates the stars. The function calls some of the other functions in the game.
def make_stars(number_of_extra_stars):

    # Get a list of colors that will be used to draw the stars
    colors_to_create = get_colors_to_create(number_of_extra_stars)

    # create_stars() function uses the list of colors as a parameter and creates Actors for each star
    new_stars = create_stars(colors_to_create)

    # this function puts the stars in the right position on the screen
    layout_stars(new_stars)

    # this function makes the stars move down the screen
    animate_stars(new_stars)
    
    return new_stars




# [Step 7]: Add placeholders
#           You'll need to define all the functions created in the previous step before you can test the game.
#           For now, use return[] for the get_colors_to_create() and create_stars() functions to make empty
#           lists, then write placeholders for the layout_stars() and animate_stars() functions by using the 
#           pass keyword.

def get_colors_to_create(number_of_extra_stars):
    return []


def create_stars(colors_to_create):
    return []

def layout_stars(stars_to_layout):
    pass

def animate_stars(stars_to_animate):
    pass


pgzrun.go()
