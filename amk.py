import random

from ursina import *  # type: ignore
from ursina.shaders import fxaa_shader,  lit_with_shadows_shader


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

Terning2 = Entity(model='dice.obj',
                  texture='dice.png', shader=lit_with_shadows_shader,  scale=0.3)
Terning2.rotation = (0, 270, -45)
Terning2.position = (0, 0.862854, -0.47929)

Terning_tal_rot = {1: {'x': '0', 'y': '270', 'z': '-45'},
                   2: {'x': '45', 'y': '360', 'z': '-270'},
                   3: {'x': '-180', 'y': '95', 'z': '30'},
                   4: {'x': '-407', 'y': '359', 'z': '90'},
                   5: {'x': '-500', 'y': '360', 'z': '90'},
                   6: {'x': '-128', 'y': '180', 'z': '1'}, }


# tal_text = Text(text='tal:0')
# tal_text.position = (-0.067835, -0.13382, 0.0839725)

stat_text = Text(text='')
stat_text.position = (0, -0.38, -0.250944)

CykaBlyat = InputField(default_value='', label='', limit_content_to=',0123456789',
                       max_lines=1, character_limit=24)


CykaBlyat.position = (0, -0.30, -0.250944)


submit_b = Button(text='Submit ', color=color.black,
                  scale=.125, text_origin=(0, 0))

submit_b.position = (0.4, -0.30, -0.250944)

roll_b = Button(text='Roll', color=color.black,
                scale=.125, text_origin=(0, 0))

roll_b.position = (-0.4, -0.30, -0.250944)


global brick_stats

brick_stats = [False, False, False, False, False, False, False, False, False]


global dicestat
dicestat = 0

bricks = [Brick_1, Brick_2, Brick_3, Brick_4,
          Brick_5, Brick_6, Brick_7, Brick_8, Brick_9]
global Blyat

Blyat = set(range(1, 10))


closewp_b = Button(text='Ok!', color=color.azure, )


wp = WindowPanel(
    title='Rules',
    content=(
        closewp_b, Text("""
    Rules:
    A round begins with all the tiles in the down position. 
    A player will roll two dice and add them together. 
    The player will then lower an equal amount of tiles. 
    For example, if the player rolls a total of 9, 
    he/she can lower any tiles to 9.

    * 9
    * 8 and 1
    * 7 and 2
    * 6 and 3
    * 5 and 4
    * 6, 2 and 1
    *4, 3, and 2
    
    The player continues to roll as long as 
    he/she has an equal number of tiles to lower.
    When no more tiles can be lowered the game is over. 
    The player will win by closing the box!
        """, scale=0.7)

    ),
    popup=True,
    enabled=True
)

wp.position = (0, 0.30, -0.250944)

submit_b.enabled = False
roll_b.enabled = False
CykaBlyat.enabled = False


def disable_wp():
    wp.enabled = False
    submit_b.enabled = True
    roll_b.enabled = True
    CykaBlyat.enabled = True


def reset():
    global Blyat
    Blyat = set(range(1, 10))
    Terning.animate_x(-0.067835, duration=1, loop=False)
    Terning2.animate_x(-0.067835, duration=1, loop=False)
    Terning.animate_rotation(Vec3(0, 270, -45), 0.1)
    Terning2.animate_rotation(Vec3(0, 270, -45), 0.1)


def roll1():

    global dicestat
    dicestat = 900
    Terning.animate_x(-4.6, duration=1, loop=False)
    Terning2.animate_x(4.6, duration=1, loop=False)


def Bricks_update():
    for i in range(9):
        if brick_stats[i] == True:
            bricks[i].animate_rotation_z(0, 1)
        else:
            bricks[i].animate_rotation_z(150, 1)
    print(brick_stats)


def roll2():
    Terning.animate_x(4.6, duration=1, loop=False)
    Terning2.animate_x(-4.6, duration=1, loop=False)


def rollran():
    global dicestat
    global diceRolled
    dice_x = random.uniform(-4, 4)
    dice_x_2 = random.uniform(-4, 4)

    Terning.animate_x(dice_x, duration=1, loop=False)
    Terning2.animate_x(dice_x_2, duration=1, loop=False)

    dicestat = 0

    Terning.animate_rotation(Vec3(0, 270, -45), 0.1)
    Terning2.animate_rotation(Vec3(0, 270, -45), 0.1)

    diceroll_1 = random.randint(1, 6)
    Terning.animate_rotation(Vec3(float((Terning_tal_rot[diceroll_1])['x']),
                                  float((Terning_tal_rot[diceroll_1])['y']),
                                  float((Terning_tal_rot[diceroll_1])['z'])), 1)

    diceroll_2 = random.randint(1, 6)
    Terning2.animate_rotation(Vec3(float((Terning_tal_rot[diceroll_2])['x']),
                                   float((Terning_tal_rot[diceroll_2])['y']),
                                   float((Terning_tal_rot[diceroll_2])['z'])), 1)

    diceRolled = diceroll_1 + diceroll_2


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
    except:
        stat_text.text = "input numbers"


def roll():
    invoke(roll1)
    invoke(roll2, delay=1.25)
    invoke(rollran, delay=2.5)


submit_b.on_click = test
roll_b.on_click = roll

wp.on_click = disable_wp
closewp_b.on_click = disable_wp

Bricks_update()


def update():

    Terning.rotation_z += time.dt * dicestat  # type: ignore
    Terning.rotation_y -= time.dt * dicestat  # type: ignore
    Terning.rotation_x += time.dt * dicestat  # type: ignore
    Terning2.rotation_z += time.dt * dicestat   # type: ignore
    Terning2.rotation_y -= time.dt * dicestat   # type: ignore
    Terning2.rotation_x += time.dt * dicestat   # type: ignore


app.run()
