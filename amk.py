
# Her importerer vi de moduler som vi skal bruge såsom random, ursina ,fxxa_shader og lit_with_shadows_shader

import random

from ursina import *  # type: ignore
from ursina.shaders import fxaa_shader,  lit_with_shadows_shader

# Vi sætter vinduet til ”borderless = False” på denne måde åbner vi den med borders
# Her bestemmer vi  vindue titlen til ”Shut Da Bux”
# Her bestemmer vi så at der er antialiasing i spillet for at gøre spillet bedre at kigge på
# Her sætter vi en variabel til ursina() for at senere kunne kalde på den via app.run()
# Her sætter vi noget belysning op da vi gerne ville have skygger i spillet

window.borderless = False
window.title = "Shut Da Bux"
camera.shader = fxaa_shader
window.icon = "Delacro-Id-Games.ico"
app = Ursina()


DirectionalLight(y=3, z=3, shadows=True)


table = Entity(model='Table.obj',
               texture='Table.png', shader=lit_with_shadows_shader,  scale=2)

table.position = Vec3(0.5, -0.3, 0)
table.rotation = (0, 270, -45)


'''
Først definer vi vores 3d objekter og her bruger man klassen Entity.

Vi vælger først modellen (model='modelnavn.fil').
Vi giver den noget texture for at give den nogen farver osv. (texture = modeletstext.fil) 

så har vi også shader som i denne situation gøre så vi har skygger osv.
 
(shader=lit_with_shadows_shader) og scale hvis det er nødvendigt (scale=int/float)


Vi har vec3 hvilke er x, y, z som er punkter i en 3d verden.
Vi sat værdien til at den at skulle være indenfor Kameras synsfelt

Her har vi definer rotationen så table vender mod os 

Vi sat værdien til at den at skulle være indenfor tables spille areal

her definer vi terning position 

her definer vi terning rotation



'''

Brick_1 = Entity(model='1.obj', parent=table,
                 texture='1.png', shader=lit_with_shadows_shader,)

Brick_1.position = (2.13781, 0.404592, 2.39383)


Brick_2 = Entity(model='2.obj', parent=table,
                 texture='2.png', shader=lit_with_shadows_shader,)

Brick_2.position = (2.13781, 0.404592, 1.63796)

Brick_3 = Entity(model='3.obj', parent=table,
                 texture='3.png', shader=lit_with_shadows_shader
                 )


Brick_3.position = (2.13781, 0.404592, 1.07682)

Brick_4 = Entity(model='4.obj', parent=table,
                 texture='4.png', shader=lit_with_shadows_shader,)


Brick_4.position = (2.13781, 0.404592, 0.529744)

Brick_5 = Entity(model='5.obj', parent=table,
                 texture='5.png', shader=lit_with_shadows_shader, )


Brick_5.position = (2.13781, 0.404592, -0.024968)

Brick_6 = Entity(model='6.obj', parent=table,
                 texture='6.png', shader=lit_with_shadows_shader,)


Brick_6.position = (2.13781, 0.404592, -0.562679)

Brick_7 = Entity(model='7.obj', parent=table,
                 texture='7.png', shader=lit_with_shadows_shader,)

Brick_7.position = (2.13781, 0.404592, -1.12461)


Brick_8 = Entity(model='8.obj', parent=table,
                 texture='8.png', shader=lit_with_shadows_shader
                 )

Brick_8.position = (2.13781, 0.404592, -1.67182)

Brick_9 = Entity(model='9.obj', parent=table,
                 texture='9.png', shader=lit_with_shadows_shader,)

Brick_9.position = (2.13781, 0.404592, -2.22621)

Terning = Entity(model='dice.obj',
                 texture='dice.png', shader=lit_with_shadows_shader,  scale=0.3)
Terning.rotation = (0, 270, -45)
Terning.position = (0, 0, -1.03368)

Terning_2 = Entity(model='dice.obj',
                   texture='dice.png', shader=lit_with_shadows_shader,  scale=0.3)
Terning_2.rotation = (0, 270, -45)
Terning_2.position = (0, 0.862854, -0.47929)


#  Terning_tal_rot listen bruger vi til at definer rotations værdier i forhold til tallet som skal vises

Terning_tal_rot = {1: {'x': '0', 'y': '270', 'z': '-45'},
                   2: {'x': '45', 'y': '360', 'z': '-270'},
                   3: {'x': '-180', 'y': '95', 'z': '30'},
                   4: {'x': '-407', 'y': '359', 'z': '90'},
                   5: {'x': '-500', 'y': '360', 'z': '90'},
                   6: {'x': '-128', 'y': '180', 'z': '1'}, }


'''
 Her definer vi tekst felter  

 Her definer vi tekst felternes positioner
'''
tal_text2 = Text(text='Terning #2:  0')
tal_text2.position = (0.047835, -0.2382, 0.0839725)

tal_text = Text(text='Terning #1:  0')
tal_text.position = (-0.177835, -0.2382, 0.0839725)

stat_text = Text(text='')
stat_text.position = (0, -0.38, -0.250944)


# Her definer vi inputfelt hvor vi kan tast dit svar ind


# Her definer vi position

CykaBlyat = InputField(default_value='', label='', limit_content_to=',0123456789',
                       max_lines=1, character_limit=24)


CykaBlyat.position = (0, -0.30, -0.250944)


#  Her definer vi knapper til at spille spillet

#  Her definer vi positioner til knapperne
submit_b = Button(text='Submit ', color=color.black,
                  scale=.125, text_origin=(0, 0))

submit_b.position = (0.4, -0.30, -0.250944)

roll_b = Button(text='Roll', color=color.black,
                scale=.125, text_origin=(0, 0))

roll_b.position = (-0.4, -0.30, -0.250944)

# her definer vi en liste som vi bruger til at kontroleere om vi skal åbne eller lukke
global brick_stats

brick_stats = [False, False, False, False, False, False, False, False, False]


# dicestats bruges til at definer om den rotere lidt randomly når den er på 0 så rotere i
global dicestat
dicestat = 0


# her har vi bricks varieabler sat inde i ind liste for at gøre det næmære
bricks = [Brick_1, Brick_2, Brick_3, Brick_4,
          Brick_5, Brick_6, Brick_7, Brick_8, Brick_9]

# blyat er vores mpde at sætte et tal række op  det den basically gøre er at lave en liste fra 1 til 9
global Blyat

Blyat = set(range(1, 10))

# her definer vi knapper
closewp_b = Button(text='Ok!', color=color.azure, )

closego_b = Button(text='Try again?', color=color.azure, )
game_won_b = Button(text='Try again?', color=color.azure, )


#  her definer vi paneler ligesom game over rules og game won og det er pop ups som kommer i staten fx rules
game_won = WindowPanel(
    title='You Won!',
    content=(
        game_won_b, Text("""
        ZAAAAAMN YOU WON
        """, scale=0.7)

    ),
    popup=True,
    enabled=True)


wp = WindowPanel(
    title='Rules',
    content=(
        closewp_b, Text("""
    Rules:
    A round begins with all the tiles in the up position.
    A player will roll two dice and add them together.
    The player will then lower an equal amount of tiles.
    For example, if the player rolls a total of 9,
    he/she can lower any tiles equal 9.

    * 9
    * 8, 1
    * 7, 2
    * 6, 3
    * 5, 4
    * 6, 2, 1
    * 4, 3, 2

    The player continues to roll as long as
    he/she has an equal number of tiles to lower.
    When no more tiles can be lowered the game is over.
    The player will win by closing the box!



    Do NOT use other letters than english letters. it Will crash
        """, scale=0.7)

    ),
    popup=True,
    enabled=True

)

game_over = WindowPanel(
    title='Game over',
    content=(
        closego_b, Text("""
   L + ratio + wrong + get a job + unfunny + 

   you fell off + never liked you anyway + cope 
   
   + ur allergic to gluten + don't care + cringe ur a kid + 
   
   literally shut the fuck up + galileo did it better + 
   
   your avi was made in MS Excel + 
   
   ur bf is kinda ugly + i have more subscribers + 
   
   owned + ur a toddler + reverse double take back + 
   
   u sleep in a different bedroom from your wife + 
   
   get rekt + i said it better + u smell + copy + 
   
   who asked + dead game + seethe + ur a coward + 
   
   stay mad + you drive a fiat 500 + yo mama + 
   
   plus ur mind numbingly stupid 
        """, scale=0.7)

    ),
    popup=True,
    enabled=True
)

# game  won paneeled er slået fra hvilke er false
game_won.enabled = False

wp.position = (0, 0.30, -0.250944)
game_over.position = (0, 0.30, -0.250944)
game_over.enabled = False


submit_b.enabled = False
roll_b.enabled = False
CykaBlyat.enabled = False


# her har vi en funkton som lukker for rules

def disable_wp():
    wp.enabled = False
    submit_b.enabled = True
    roll_b.enabled = True
    CykaBlyat.enabled = True


# denne funktion resetter bricksne til deres start position

def reset():
    roll_b.enabled = True

    global Blyat
    Blyat = set(range(1, 10))
    Terning.animate_x(-0.067835, duration=1, loop=False)
    Terning_2.animate_x(-0.067835, duration=1, loop=False)
    Terning.animate_rotation(Vec3(0, 270, -45), 0.1)
    Terning_2.animate_rotation(Vec3(0, 270, -45), 0.1)
    game_over.enabled = True

# roll1 rykker terning 1 til venstre og terning 2 til højre


def roll1():

    global dicestat
    dicestat = 900
    Terning.animate_x(-4.6, duration=1, loop=False)
    Terning_2.animate_x(4.6, duration=1, loop=False)

# bricks_update funktionen tjekker om listen brick_stat er ændret vis 1 værdi i listen er true og lukker for det


def Bricks_update():
    for i in range(9):
        if brick_stats[i] == True:
            bricks[i].animate_rotation_z(0, 1)
        else:
            bricks[i].animate_rotation_z(150, 1)
    print(brick_stats)
    if brick_stats == [True, True, True, True, True, True, True, True]:
        game_won.enabled = True
    else:
        game_won.enabled = False
        pass


# roll2 rykker terning 2 til venstre og terning 1 til højre

def roll2():
    Terning.animate_x(4.6, duration=1, loop=False)
    Terning_2.animate_x(-4.6, duration=1, loop=False)

   # det er her hvor vi har tilfældigheder via random modulet


def rollran():
    global dicestat
    global diceRolled
    dice_x = random.uniform(-4, 4)
    dice_x_2 = random.uniform(-4, 4)

    Terning.animate_x(dice_x, duration=1, loop=False)
    Terning_2.animate_x(dice_x_2, duration=1, loop=False)

    dicestat = 0

    Terning.animate_rotation(Vec3(0, 270, -45), 0.1)
    Terning_2.animate_rotation(Vec3(0, 270, -45), 0.1)

    diceroll_1 = random.randint(1, 6)
    Terning.animate_rotation(Vec3(float((Terning_tal_rot[diceroll_1])['x']),
                                  float((Terning_tal_rot[diceroll_1])['y']),
                                  float((Terning_tal_rot[diceroll_1])['z'])), 1)
    tal_text.text = ("Terning 1: "+str(diceroll_1))

    diceroll_2 = random.randint(1, 6)
    Terning_2.animate_rotation(Vec3(float((Terning_tal_rot[diceroll_2])['x']),
                                    float((Terning_tal_rot[diceroll_2])['y']),
                                    float((Terning_tal_rot[diceroll_2])['z'])), 1)

    tal_text2.text = ("Terning 2: "+str(diceroll_2))

    diceRolled = diceroll_1 + diceroll_2

    roll_b.enabled = False


# test tjekker for om der er tomt i input feltet så det ikke crasher
# den tjekker også om du prøver at snyde
def test():

    try:
        stat_text.text = ""
        Numbers = [int(i) for i in (CykaBlyat.text).split(',')]
        print(Numbers)
        if sum(Numbers) != diceRolled:
            print("Your number doesnt add up to ", str(diceRolled))
            for l in range(len(brick_stats)):
                brick_stats[l-1] = False
            invoke(Bricks_update)
            invoke(reset)
            return
        else:
            for n in Numbers:
                if n not in Blyat:
                    print(n, " is not in your board")
                    for l in range(len(brick_stats)):
                        brick_stats[l-1] = False
                    invoke(Bricks_update)
                    invoke(reset)

                    return
            for i in Numbers:
                Blyat.discard(i)
                brick_stats[i-1] = True
                invoke(Bricks_update)
        CykaBlyat.text = ''
        roll_b.enabled = True
    except:
        stat_text.text = "input numbers"

# roll tager alle roll funktioner og sætter dem sammen til at bruge det til en knap


def roll():
    invoke(roll1)
    invoke(roll2, delay=1.25)
    invoke(rollran, delay=2.5)


submit_b.on_click = test
roll_b.on_click = roll

wp.on_click = disable_wp

game_over.on_click = game_over.disable
closewp_b.on_click = disable_wp
closego_b.on_click = game_over.disable

game_won_b.on_click = game_won.disable


Bricks_update()

# denne funktion burde kører vær frame det bruges til at rotere tærningen lidt randomt


def update():

    Terning.rotation_z += time.dt * dicestat  # type: ignore
    Terning.rotation_y -= time.dt * dicestat  # type: ignore
    Terning.rotation_x += time.dt * dicestat  # type: ignore
    Terning_2.rotation_z += time.dt * dicestat   # type: ignore
    Terning_2.rotation_y -= time.dt * dicestat   # type: ignore
    Terning_2.rotation_x += time.dt * dicestat   # type: ignore


def input(key):
    if key == 'enter':
        test()


app.run()
