
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
CENTER = (CENTER_X, CENTER_Y)
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




# [Step 7]: Create stars: get color, create stars, and place stars on the screen.
#           You'll need to define all the functions created in the previous step before you can test the game.
#           For now, use return[] for the get_colors_to_create() and create_stars() functions to make empty
#           lists, then write placeholders for the layout_stars() and animate_stars() functions by using the 
#           pass keyword.

# Get a list of colors: red, blue, and green stars. The list stars with red, because you always need one - and
# only one - red star to appear
def get_colors_to_create(number_of_extra_stars):
    colors_to_create = ["red"]
    
    for i in range(0, number_of_extra_stars):
        random_color = random.choice(COLORS)
        colors_to_create.append(random_color)
        
    return colors_to_create


# Create the stars on the screen.
def create_stars(colors_to_create):
    new_stars = []

    for color in colors_to_create:
        star = Actor(color + "-star")
        new_stars.append(star)
    
    return new_stars


# Place the stars in the right position on the screen. First, you'll need to work out the numbe of gaps you need
# between the stars. This number will be one more than the number of stars on the screen, e.g. if there are two stars
# on the screen, there will be three gaps.
# The size of each gap can be worked out by dividing the width of the screen by the total number of gaps.
# You also need to shuffle the position of the stars so that the red star doesn't appear at the same position every time
def layout_stars(stars_to_layout):
    number_of_gaps = len(stars_to_layout) + 1
    gap_size = WIDTH / number_of_gaps
    random.shuffle(stars_to_layout)

    # Set the position of the curret star along the x-axis by multiplying the position of the star in the list
    # by the size of the gap
    for index, star in enumerate(stars_to_layout):
        new_x_pos = (index + 1) * gap_size
        star.x = new_x_pos



# [Step 8]: Animate the stars.
#           Now that you have a few stars on the screen, it's time to add animation and bring this game to life.
#           you need to write some code to move each star down the screen. You'll also have to define the duration
#           of the animation so that stars move faster as the levels progress.
#           You'll set the star's anchor to the bottom so that the animation stops as soon as the star reaches the
#           bottom of the screen.
def animate_stars(stars_to_animate):
    for star in stars_to_animate:
        duration = START_SPEED - current_level
        star.anchor = ("center", "bottom")

        animation = animate(star, duration=duration, on_finished=handle_game_over, y=HEIGHT)
        animations.append(animation)



# [Step 9(a)]: Click a red star
#           When the player clicks on a red star, the program stops the animation of the current set of stars on
#           the screen and moves the game to the next level. If the player is on the final level, game_complete is
#           set to True and the game ends.
def red_star_click():
    global current_level, stars, animations, game_complete
    stop_animations(animations)

    if current_level == FINAL_LEVEL:
        game_complete = True
    else:
        current_level = current_level + 1
        stars = []
        animations = []



# [Step 9(b)]: Handle mouse clicks
#              A function that allows the player to interact with the game.
#              Use Pygame Zero's on_mouse_down() function to do this. This function is called whenever a player
#              clicks the mouse. Then use the collidepoint() function to check if the player has clicked on a
#              star. If they have, the code will check whether that star was red or not.
def on_mouse_down(pos):
    global stars, current_level
    
    for star in stars:
        if star.collidepoint(pos):
            if "red" in star.image:
                red_star_click()
            else:
                handle_game_over()



# stop the animations
def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()



# Game over
def handle_game_over():
    global game_over
    game_over = True



# Display messages
def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text, fontsize=60, center=CENTER, color=FONT_COLOR)
    screen.draw.text(sub_heading_text, fontsize=30, center=(CENTER_X, CENTER_Y + 30), color=FONT_COLOR)



pgzrun.go()
