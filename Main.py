import random

from ursina import *  # type: ignore
from ursina.shaders import fxaa_shader,  lit_with_shadows_shader


window.borderless = False
window.title = "Shut Da Bux"
camera.shader = fxaa_shader
app = Ursina()

DirectionalLight(y=3, z=3, shadows=True)


# først definer vi vores 3d objektor og der bruger man klassen Entity
# Vi vælger først modelet (model='modeltsnavn.fil') også noget texture for at give den nogen farver osv (texture = modeletstext.fil) 
# så har vi også shader som i denne kontext gøre så vi har skygger osv(shader=lit_with_shadows_shader) og scale hvis det er nødvendigt (scale=int/float)

table = Entity(model='Table.obj',
               texture='Table.png', shader=lit_with_shadows_shader,  scale=2)

Brick_1 = Entity(model='1.obj', parent=table,
                 texture='1.png', shader=lit_with_shadows_shader,)

Brick_2 = Entity(model='2.obj', parent=table,
                 texture='2.png', shader=lit_with_shadows_shader,)

Brick_3 = Entity(model='3.obj', parent=table,
                 texture='3.png', shader=lit_with_shadows_shader
                 )

Brick_4 = Entity(model='4.obj', parent=table,
                 texture='4.png', shader=lit_with_shadows_shader,)


Brick_5 = Entity(model='5.obj', parent=table,
                 texture='5.png', shader=lit_with_shadows_shader, )


Brick_6 = Entity(model='6.obj', parent=table,
                 texture='6.png', shader=lit_with_shadows_shader,)


Brick_7 = Entity(model='7.obj', parent=table,
                 texture='7.png', shader=lit_with_shadows_shader,)


Brick_8 = Entity(model='8.obj', parent=table,
                 texture='8.png', shader=lit_with_shadows_shader
                 )

Brick_9 = Entity(model='9.obj', parent=table,
                 texture='9.png', shader=lit_with_shadows_shader,)

Terning = Entity(model='dice.obj',
                 texture='dice.png', shader=lit_with_shadows_shader,  scale=0.3)

Terning_2 = Entity(model='dice.obj',
                   texture='dice.png', shader=lit_with_shadows_shader,  scale=0.3)


# her definer vi nogle tekst felter 


tal_text = Text(text='Terning #1:  0')

tal_text2 = Text(text='Terning #2:  0')

stat_text = Text(text='')

# her definer vi en inputfelt for at skrive svaret ind 
CykaBlyat = InputField(default_value='', label='', limit_content_to=',0123456789',
                       max_lines=1, character_limit=24)


# her definer vi par knapper til at inpute med

submit_b = Button(text='Submit ', color=color.black,
                  scale=.125, text_origin=(0, 0))

roll_b = Button(text='Roll', color=color.black,
                scale=.125, text_origin=(0, 0))

closewp_b = Button(text='Ok!', color=color.azure, )

closego_b = Button(text='Try again?', color=color.azure, )

game_won_b = Button(text='Try again?', color=color.azure, )

# postion og rotation 
# vi har vec3 hvilke er x,y,z som er punkter i 3d verden 
#
table.position = Vec3(0.5, -0.3, 0)
table.rotation = (0, 270, -45)

Brick_1.position = (2.13781, 0.404592, 2.39383)

Brick_2.position = (2.13781, 0.404592, 1.63796)

Brick_3.position = (2.13781, 0.404592, 1.07682)

Brick_4.position = (2.13781, 0.404592, 0.529744)

Brick_5.position = (2.13781, 0.404592, -0.024968)

Brick_6.position = (2.13781, 0.404592, -0.562679)

Brick_7.position = (2.13781, 0.404592, -1.12461)

Brick_8.position = (2.13781, 0.404592, -1.67182)

Brick_9.position = (2.13781, 0.404592, -2.22621)

Terning.rotation = (0, 270, -45)
Terning.position = (0, 0, -1.03368)

Terning_2.rotation = (0, 270, -45)
Terning_2.position = (0, 0.862854, -0.47929)


# her definer vi lister

# Terning_tal_rot listen bruger vi til at definer rotations værdier i forhold til talet som skal vises 
Terning_tal_rot = {1: {'x': '0', 'y': '270', 'z': '-45'},
                   2: {'x': '45', 'y': '360', 'z': '-270'},
                   3: {'x': '-180', 'y': '95', 'z': '30'},
                   4: {'x': '-407', 'y': '359', 'z': '90'},
                   5: {'x': '-500', 'y': '360', 'z': '90'},
                   6: {'x': '-128', 'y': '180', 'z': '1'}, }

global brick_stats

brick_stats = [False, False, False, False, False, False, False, False, False]

bricks = [Brick_1, Brick_2, Brick_3, Brick_4,
          Brick_5, Brick_6, Brick_7, Brick_8, Brick_9]

# her definer vi  blyat hvilke er vores måde at have et "bord" med 9 elementer dette bruges for spil logiken 
global Blyat

Blyat = set(range(1, 10))



